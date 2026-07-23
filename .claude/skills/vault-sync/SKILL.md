---
name: vault-sync
description: Đồng bộ và tái sinh dữ liệu phái sinh của learning-vault — MỌI domain active trong .claude/domains.yaml. Render bảng "Lịch sử xuất hiện" từ YAML appearances ra body note, tính role_ratio/distractor_count/correct_count, tái sinh 99_Dashboard/Pair_Matrix.md, Distractor_Stats.md, Topic_Stats.md, Trap_Stats.md, Seq_Stats.md, Blank_Stats.md và Adverb_Stats.md, kiểm tra tính toàn vẹn link và schema. Dùng skill này sau MỌI lần ghi batch (exam-analysis Phase 5 gọi tự động), khi người dùng nói "sync vault", "cập nhật dashboard", "kiểm tra vault", hoặc khi thấy số liệu bảng lệch với appearances.
---

# Vault Sync Skill

Idempotent: chạy N lần cho cùng kết quả. Khai danh tính trước khi ghi: `mkdir -p .claude/state && echo vault-sync > .claude/state/active_skill`; xóa file khi xong (sentinel TTL 30 phút).

## Phase 1 — Scan & Validate (five-check)

Đọc `.claude/domains.yaml`; với mỗi domain `status: active`, quét `note_dirs`, mỗi note kiểm:
1. Frontmatter đúng schema loại (schema_rule của domain trong manifest), enum hợp lệ.
2. Mọi `[[link]]` và tham chiếu trong `members/pair_with/group/pairs_inside` trỏ đến file tồn tại.
3. Mỗi entry `appearances`/`tested_directions`/`history` khớp với EXAM note tương ứng (exam tồn tại, số câu hợp lệ, role nhất quán với đáp án trong EXAM). **Ngoại lệ topic-note câu 9-10 (Q15):** entry `history` có `q` thuộc dạng `câu-giống-đoạn-văn`/`câu-giống-đồ-thị` chỉ verify exam+q tồn tại + dạng bài là dạng-sinh-topic — KHÔNG đòi `role` khớp một phương án đáp án cụ thể (chủ đề trích từ chất liệu đọc, không phải phương án). **Ngoại lệ sequence-note câu 13-15 (Q19):** tương tự — entry `history` có `q` thuộc dạng `sắp-xếp-thứ-tự` chỉ verify exam+q tồn tại + dạng bài đúng; `role: correct` = cue định vị mảnh trong chuỗi đúng (KHÔNG đòi khớp một phương án hoán vị cụ thể). **Ngoại lệ blank-note câu 16-18 (Q20):** tương tự — entry `history` có `q` thuộc dạng `điền-nội-dung` chỉ verify exam+q tồn tại + dạng bài đúng; `role: correct` = quan hệ suy luận quyết định đáp án đúng (KHÔNG đòi khớp một phương án mệnh đề cụ thể). **Ngoại lệ adverb-note câu 19 (Q21):** tương tự — entry `history` có `q` thuộc dạng `điền-phó-từ` chỉ verify exam+q tồn tại + dạng bài đúng; `role: correct` = chức năng phó từ quyết định đáp án đúng (KHÔNG đòi khớp một phương án phó từ cụ thể).
4. Grammar note có đủ cặp marker `%% compile:core-start %%` / `%% compile:core-end %%`.
5. PAIR `confidence: closed` phải có ≥2 `tested_directions` với prompt đảo nhau.

**Mọi vi phạm → ghi vào báo cáo ⚠️, KHÔNG tự sửa** (no silent assumption).

## Phase 2 — Compute

- `role_ratio` mỗi grammar note = `{n}C/{m}D` từ appearances.
- `distractor_count`/`correct_count` mỗi **DIS note, topic note, trap note, sequence note, blank note VÀ adverb note** từ history (cùng cơ chế — đếm role trong `history`).
- PAIR có tested_directions đủ 2 chiều mà còn `open` → đề xuất nâng `closed` (đưa vào diff, không tự nâng — thay đổi confidence cần người duyệt).

## Phase 3 — Render body sections

Trong mỗi grammar/pair/distractor/topic/trap/sequence/blank/adverb note, tìm block:

```
<!-- sync:appearances:start -->
...(nội dung cũ)...
<!-- sync:appearances:end -->
```

Thay nội dung giữa 2 marker bằng bảng Markdown render từ YAML (cột: Đề | Câu | Vai | Nguồn). Không đụng bất cứ thứ gì ngoài block. Note thiếu marker → báo ⚠️.

## Phase 4 — Regenerate dashboards

- `TOPIK/99_Dashboard/Pair_Matrix.md` [domain topik]: bảng mọi PAIR — thành viên | chiều đã thi | morph_note | confidence; sort: open trước (radar ôn tập).
- `TOPIK/99_Dashboard/Distractor_Stats.md` [domain topik]: bảng mọi DIS — pattern | nC/mD | kill_signal | select_signal; sort theo distractor_count giảm dần.
- `TOPIK/99_Dashboard/Topic_Stats.md` [domain topik]: bảng mọi topic note — topic (+topic_vi) | category | nC/mD | select_signal | kill_signal; sort theo (correct_count + distractor_count) giảm dần.
- `TOPIK/99_Dashboard/Trap_Stats.md` [domain topik]: bảng mọi trap note — trap_name | scope | category | nC/mD | kill_signal | select_signal; sort theo distractor_count giảm dần.
- `TOPIK/99_Dashboard/Seq_Stats.md` [domain topik]: bảng mọi sequence note — cue_name | category | role_in_order | nC/mD | select_signal | kill_signal; sort theo (correct_count + distractor_count) giảm dần. Thêm mục **"Candidate cue (1× — chưa tạo note)"** liệt kê cue mới xuất hiện 1× (chưa graduate) kèm exam/câu — nguồn: quét inline exam-note dạng `sắp-xếp-thứ-tự` (cue mô tả ở cột Căn cứ, chưa có `[[SEQ_*]]`).
- `TOPIK/99_Dashboard/Blank_Stats.md` [domain topik]: bảng mọi blank note — blank_name | category | role_in_para | nC/mD | select_signal | kill_signal; sort theo (correct_count + distractor_count) giảm dần. Thêm mục **"Candidate quan hệ (1× — chưa tạo note)"** liệt kê quan hệ suy luận mới xuất hiện 1× (chưa graduate) kèm exam/câu — nguồn: quét inline exam-note dạng `điền-nội-dung` (quan hệ mô tả ở cột "Căn cứ / Phân tích" và dòng `**Quan hệ:**`, chưa có `[[BLK_*]]`).
- `TOPIK/99_Dashboard/Adverb_Stats.md` [domain topik]: bảng mọi adverb note — adv_name | category | members | nC/mD | select_signal | kill_signal; sort theo (correct_count + distractor_count) giảm dần. Thêm mục **"Candidate chức năng (1× — chưa tạo note)"** liệt kê chức năng phó từ mới xuất hiện 1× (chưa graduate) kèm exam/câu — nguồn: quét inline exam-note dạng `điền-phó-từ` (chức năng mô tả ở dòng `**Chức năng:**` và cột "Căn cứ / Phân tích", chưa có `[[ADV_*]]`).
- Đầu mỗi file render: dòng cảnh báo `> RENDER tự sinh bởi vault-sync {ngày} — KHÔNG sửa tay` + thống kê nguồn.

## Phase 5 — Report

In: số note quét / số field cập nhật / số block render / danh sách ⚠️ theo mức (schema lỗi > link gãy > lệch dữ liệu > thiếu marker) / diff chờ duyệt (nâng confidence).
