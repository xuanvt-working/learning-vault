---
name: topik-grammar-compile
description: Tổng hợp toàn bộ ngữ pháp của learning-vault (domain: topik) thành MỘT file handbook duy nhất 99_Dashboard/GR_Compiled_Handbook.md gồm 5 section (metadata; ma trận khác biệt theo nhóm kèm cấp TOPIK + cách chia; bảng quy đổi hai chiều PAIR; bảng nhiễu; radar ôn tập). Dùng skill này khi người dùng nói "tổng hợp ngữ pháp", "compile handbook", "xuất bảng tra", "gom tất cả vào 1 file", hoặc trước kỳ ôn thi cần tài liệu tổng.
---

# Grammar Compile Skill

Output DUY NHẤT: `TOPIK/99_Dashboard/GR_Compiled_Handbook.md` (Q4: chỉ .md). Là RENDER — tái sinh được hoàn toàn từ atomic notes; muốn đổi nội dung → sửa note nguồn rồi chạy lại. Khai danh tính: `mkdir -p .claude/state && echo topik-grammar-compile > .claude/state/active_skill`; xóa khi xong.

## Phase 1 — Scan & Validate

Chạy đúng five-check của vault-sync (đọc `.claude/skills/vault-sync/SKILL.md` Phase 1). Bổ sung check riêng: grammar note thiếu marker compile hoặc chưa gán `group` → vẫn compile phần còn lại nhưng liệt kê trong §0 và báo cáo Phase 4.

## Phase 2 — Extract

- Grammar: lấy block giữa `%% compile:core-start %%` và `%% compile:core-end %%` (mục tiêu 8–12 dòng: nghĩa lõi, kết hợp, ràng buộc ⚠️, tín hiệu TOPIK ⭐, 1 ví dụ) + frontmatter (pattern, group, appearances, role_ratio, **level**). Field `level` (vd `TOPIK II (3-4)`) dùng cho cột `Cấp` của §1.
  - **Ví dụ (dùng lại cho §1/§3)**: tách riêng dòng `- **Ví dụ**: {câu Hàn} → {dịch Việt} {đuôi nguồn/marker}` từ block core thành field `example` gồm 3 phần: `hangul`, `dich`, `nguon` (`[TOPIK_xx-Qy]` hoặc `(vd tự tạo) ⚠️ Unverified`). Note thiếu dòng này → `example` rỗng, báo trong Phase 4. Câu quá dài (khi render vào bảng §1/§3) → rút còn 1 mệnh đề chứa mẫu ngữ pháp, giữ `→ dịch` và đuôi nguồn/marker.
  - **Cách chia (형태) — dùng cho §1 (cột Cách chia)**: lấy bảng cách chia thành field `conjugation`. **Ưu tiên** đọc block giữa cặp fence `%% compile:conj-start %%` … `%% compile:conj-end %%` (note mới sinh từ template); **fallback** cho note cũ chưa có fence: lấy bảng dưới heading `## 2. Cách kết hợp (형태)` (từ ngay sau heading tới heading `##` kế tiếp). Không tìm được bảng theo cả hai cách → `conjugation` rỗng, báo Phase 4.
    - **Nén 1 dòng cho cột §1**: nối các giá trị cột **"Dạng"** của các hàng (Động từ / Tính từ / N+이다 / Quá khứ) bằng ` · `; **bỏ** ô rỗng / `(không dùng)` / `—`; thêm **một** dấu `⚠️` ở cuối dòng nếu bảng nguồn có bất kỳ ô `⚠️ Unverified`. `conjugation` rỗng → cột để `—`.
- Pair: members, tested_directions, morph_note, confidence.
- Group: bảng ma trận khác biệt trong body (block giữa `<!-- matrix:start -->` / `<!-- matrix:end -->`) + confusion_pairs.
- Distractor: counts, kill_signal, select_signal.
- Exam: bảng câu × ngữ pháp.

## Phase 3 — Assemble (5 section, thứ tự cố định)

```
§0 Metadata      — ngày compile, số nguồn (X GR / Y GROUP / Z PAIR / W DIS / V EXAM),
                   danh sách note bị bỏ qua kèm lý do. Text §0 chỉ nhắc 5 section hiện có
                   (KHÔNG nhắc Index / Từ điển / Traceability đã bỏ).
§1 Ma trận nhóm  — mỗi GROUP một sub-section: ma trận khác biệt + confusion_pairs (nội dung
                   §3 cũ, đưa lên ngay sau §0). Cấu trúc bảng mỗi nhóm:
                   `Ngữ pháp | Cấp | Cách chia | …diff_axes… | Tín hiệu chọn nhanh | Ví dụ (Hàn → Việt)`.
                   - Cột `Cấp` = field `level` của chính GR hàng đó.
                   - Cột `Cách chia` = chuỗi conjugation nén 1 dòng (luật nén ở Phase 2);
                     conjugation rỗng → `—`.
                   - Cột `Ví dụ` = field example của GR (rút gọn 1 mệnh đề nếu dài).
                   Hai cột `Cấp` + `Cách chia` chèn NGAY SAU cột `Ngữ pháp`, trước các diff_axes.
§2 Quy đổi       — mọi PAIR: cặp | chiều đã thi (TOPIK_37→, ←TOPIK_47) | morph_note | confidence;
                   open lên đầu
§3 Nhiễu         — mọi DIS: pattern | nC/mD | kill_signal | select_signal | Ví dụ (Hàn → Việt);
                   sort distractor_count giảm dần. Cột Ví dụ kéo từ note GR khớp link [[GR_*]] ở
                   cột pattern; pattern không có note GR khớp → để trống + báo ⚠️ ở Phase 4.
§4 Radar         — PAIR open | GR sr-due trong 7 ngày | GROUP/GR còn draft/unverified
```

Đầu file: `> RENDER tự sinh bởi topik-grammar-compile {ngày} — KHÔNG sửa tay.`
Ngay dưới tiêu đề: dòng TOC liệt kê ĐÚNG 5 section với anchor mới (§0…§4). Link "→ Xem [§2]"
(PAIR) trong §4 Radar vẫn đúng vì PAIR = §2.

## Phase 4 — Report

Báo cáo lệch trước khi ghi: note thiếu marker / GROUP thiếu ma trận / GR chưa gán nhóm / PAIR mồ côi / **GR (hoặc pattern §3) thiếu dòng `- **Ví dụ**:` trong block core** (cột Ví dụ §1/§3 để trống) / **GR không lấy được bảng cách chia (thiếu cả fence `compile:conj` lẫn section `## 2. Cách kết hợp (형태)`, hoặc bảng rỗng)** (cột Cách chia §1 để `—`) / **GR thiếu field `level`** (cột Cấp §1 để trống). Chỉ liệt kê ⚠️ — KHÔNG tự sửa note nguồn.

## Phase 5 — Write

Ghi handbook (ghi đè toàn bộ file cũ). Kết thúc: thống kê §0 + nhắc các ⚠️ tồn đọng ảnh hưởng độ đầy đủ của handbook.
