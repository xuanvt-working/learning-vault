# Learning Vault — Operating Manual (multi-domain)

Vault quản lý nhiều domain học tập. Nguồn định tuyến duy nhất: `.claude/domains.yaml`. Ngôn ngữ làm việc: tiếng Việt; thuật ngữ Hàn giữ Hangul, thuật ngữ BA giữ tiếng Anh.

## Định tuyến domain

| Tín hiệu trong yêu cầu | Domain | Skill vào việc |
|---|---|---|
| Đề TOPIK, ngữ pháp/từ vựng Hàn, ảnh câu trắc nghiệm | `topik` (TOPIK/) | topik-exam-analysis, topik-grammar-compile |
| BABOK, requirement, elicitation, use case, BPMN, case study BA | `ba` (BA/) | (placeholder — chưa kích hoạt, xem dưới) |
| "sync vault", "hôm nay ôn gì", kết quả review | mọi domain active | vault-sync, review-scheduler (đọc manifest) |

Không chắc domain nào → hỏi, không đoán (no silent assumption).

## Nguyên tắc chung (mọi domain)

1. **Reference-don't-duplicate**: nội dung sống trong note canonical; nơi khác chỉ link.
2. **No silent assumptions**: claim không truy được nguồn → `⚠️ Unverified`, chờ người duyệt.
3. **Source citation**: theo `.claude/rules/_shared/source_citation_rule.md`.
4. **Naming**: theo `.claude/rules/_shared/naming_rule.md`; schema frontmatter theo rule riêng từng domain (`.claude/rules/{domain}/`).
5. **Single-source render**: `{domain}/99_Dashboard/` và `99_Global_Dashboard/` là output tự sinh — không sửa tay.
6. **Hybrid human-confirm**: skill đề xuất diff, ghi sau khi duyệt; batch đầu ghi `status: draft`.
7. Hook `PreToolUse` enforce vùng cấm — đọc manifest, áp cho mọi domain.

## Skills dùng chung

| Skill | Phạm vi |
|---|---|
| `vault-sync` | Quét mọi domain `status: active` trong manifest; render body sections, tính counts, tái sinh dashboard domain + `99_Global_Dashboard/Review_Today.md` (SR hợp nhất) |
| `review-scheduler` | SR queue hợp nhất mọi domain — quét `sr_dirs` trong manifest |

## Domain: topik (active)

Luồng: `50_Exams` (immutable khi verified) → Grammar/Pairs/Groups/Distractors/Vocab → Dashboard. Chi tiết + decision log Q1–Q5: xem `TOPIK/00_Templates/` và `.claude/rules/topik/frontmatter_schema.md`. Backfill lần đầu: `TOPIK/BACKFILL_SEED.md`.

## Domain: ba (placeholder — learn-first)

Cấu trúc thư mục đã dựng, nhưng **templates và skill chưa viết** — chủ đích: schema BA phải lộ ra từ vài buổi phân tích tài liệu thật (BABOK, case study) trước khi đóng khuôn, như cách 6 đề TOPIK sinh ra template GR/PAIR/GROUP. Khi đủ ngữ liệu: tạo `.claude/rules/ba/frontmatter_schema.md` + `BA/00_Templates/*` + skill `ba-note-builder`, đổi `status: placeholder → active` trong manifest.

## Vùng cấm (hook enforce, mọi domain)

- `*/00_Templates/**`: chỉ con người hoặc skill `template-editor` (sentinel `.claude/state/active_skill`); skill phải propose diff trước khi ghi.
- `*/99_Dashboard/**` và `99_Global_Dashboard/**`: chỉ vault-sync / *-compile (sentinel `.claude/state/active_skill`).
- Field `sr-*`: chỉ review-scheduler.
- Thư mục trong `immutable_when_verified` của manifest: note `status: verified` là bất biến.
- `.env`: cấm tuyệt đối.

## Quyết định kiến trúc (decision log)

| # | Quyết định |
|---|---|
| Q1–Q5 | Giữ nguyên (xem `.claude/rules/topik/frontmatter_schema.md` phần đầu) |
| Q6 | Multi-domain phương án A: một vault, namespace theo domain, manifest định tuyến, SR queue hợp nhất |
| Q7 | BA theo learn-first: dựng khung trước, schema/template/skill viết sau khi có ngữ liệu thật |
| Q8 | Claude Project trên claude.ai tách riêng theo domain (memory không trộn), độc lập với vault |
| Q9 | Nới hook `00_Templates/`: mở cho skill chuyên trách `template-editor` (gate bằng sentinel như dashboard), vẫn giữ nguyên tắc propose-diff-first + con người duyệt |
| Q10 | Domain topik thêm dạng đọc-hiểu `xác-định-chủ-đề` (TOPIK ĐỌC 5~8) + layer `topic-note` (`TOPIK/45_Topics/`, tín hiệu select/kill như distractor) |
| Q11 | Layer `topic-note` tổ chức **theo category** (1 file = 1 category-theme, gộp từ vựng đáp án cùng chủ đề vào `members` + bảng body + `history` gộp), KHÔNG mỗi đáp án một file. Dạng `xác-định-chủ-đề` chỉ tạo note cho phương án ĐÚNG; nhiễu inline-only (bỏ khoản nhiễu ≥2×). Taxonomy chuẩn trong `frontmatter_schema.md` |
| Q12 | Đáp án dạng bài ĐỌC lấy từ `TOPIK/90_MOC/MOC_Nguon_Tham_Khao.md` (bảng key theo số câu), cite `[RA:nn-Qm]` (authoritative, không Unverified); MOC thiếu câu nào mới tự giải + `⚠️ Unverified` |
| Q13 | Domain topik thêm dạng đọc-hiểu "내용과 같은 것" (TOPIK ĐỌC 9~12) tách **hai slug theo chất liệu**: câu 9 poster/안내문/광고 = `câu-giống-đoạn-văn` (글의 내용과 같은 것), câu 10 đồ thị/도표 = `câu-giống-đồ-thị` (도표의 내용과 같은 것). Layer `trap-note` (`TOPIK/46_Traps/`) phục vụ **cả hai slug**, tổ chức **theo kỹ thuật bẫy** (ngưỡng ≥2× như DIS, tái dùng history + sync marker + counts), field `scope` (poster/đồ-thị) phân biệt chất liệu; KHÔNG sinh GR/PAIR/GROUP (topic → xem Q15). Block exam 5 cột `# | Phương án | Nghĩa | Vai | Căn cứ`; câu 9 poster = blockquote, câu 10 đồ thị = bảng số liệu. Taxonomy bẫy chuẩn trong `frontmatter_schema.md` |
| Q14 | Heading mỗi câu trong exam-note mang **hậu tố 한국어 rút gọn** cho MỌI dạng: `## Câu {N} — dạng {slug} ({hậu tố 한국어})` (bỏ đuôi động từ `고르기/고르십시오`, vd `xác-định-chủ-đề (무엇에 대한 글인지)`). Nguồn hậu tố = cột "Hậu tố heading" trong `TOPIK/90_MOC/MOC_Dang_Bai.md` |
| Q15 | Hai slug câu-giống (`câu-giống-đoạn-văn` câu 9 + `câu-giống-đồ-thị` câu 10) sinh **dual-layer song song**: `trap-note` (như Q13) **và** `topic-note` mới. Từ vựng chủ đề lấy từ **chất liệu đọc** (poster/đồ thị), KHÔNG từ 4 phương án; ngưỡng **1×** (append/tạo ngay, như topic câu 5-8, KHÁC ngưỡng ≥2× của trap); category tái dùng enum `광고\|안내\|화제` (câu 9 → `광고/안내`, câu 10 → `화제`, KHÔNG mở rộng enum); `role: correct` = "chủ đề bài xuất hiện" (five-check nới: không đòi khớp phương án đáp án). Exam-note thêm dòng `**Chủ đề:** {theme} → [[TOPIC_{category-theme}]]` ở **mức câu** (dưới khối Dịch, trước bảng 5 cột — không thêm cột). Chi tiết trong `frontmatter_schema.md` §topic-note |
| Q16 | Domain topik thêm dạng đọc-hiểu "내용과 같은 것" trên **đoạn văn dài** (TOPIK ĐỌC câu 11~12) = slug `câu-giống-đoạn-văn-dài` (hậu tố `글의 내용과 같은 것`, dạng 4c trong `MOC_Dang_Bai`). Render y hệt câu 9 (blockquote văn xuôi + Dịch + `**Chủ đề:**` mức câu + bảng 5 cột) và sinh **dual-layer song song** như Q15: `trap-note` (ngưỡng ≥2×; thêm `scope: văn-xuôi` + 5 category bẫy prose `đảo-thông-tin\|đảo-thời-điểm\|nói-quá\|không-có-thông-tin\|sai-mục-đích`) **và** `topic-note` (category `화제`, ngưỡng 1×, chủ đề lấy từ đoạn văn). **Chuẩn hóa toàn vault:** MỌI câu (mọi dạng) kết thúc bằng hai dòng thống nhất `**Ngữ pháp:**` (thay "Ngữ pháp nền"; liệt kê pattern trong 문제 + link `[[GR_*]]` nếu note tồn tại, KHÔNG appearances/KHÔNG tạo GR mới) rồi `**Từ vựng:**` (thay "Từ vựng mới/khóa"; inline-only). Backfill toàn bộ 8 đề hiện có. Chi tiết trong `frontmatter_schema.md` |
| Q17 | Exam-note **đảo nguyên tắc reference-don't-duplicate cho phần dịch/gloss**: mỗi câu (mọi dạng) CHỨA dịch + phân tích chi tiết ngay trong exam-note. **Bỏ** hai dòng tóm tắt `**Ngữ pháp:**`/`**Từ vựng:**` (Q16), **thay bằng** block `### Chú giải chi tiết`: chia chất liệu 문제/đoạn văn theo **từng dòng** → bản dịch dòng + **toàn bộ** ngữ pháp (không bỏ sót; `[[GR_*]]` chỉ khi note tồn tại, KHÔNG appearances/KHÔNG tạo GR mới) + **toàn bộ** từ vựng/cụm (không bỏ sót). **Phân tích đúng/sai từng đáp án** gộp vào **cột cuối bảng phương án** (đổi tên "Lý do 1 dòng" → "Lý do / Phân tích", hoặc mở rộng cột "Căn cứ") — GIỮ nguyên cấu trúc bảng + cột link `[[GR_*]]`/`[[TOPIC_*]]`/`[[TRAP_*]]` + Vai ✅❌ (vault-sync five-check đọc bảng verify appearances). Nội dung dịch/gloss/phân tích là rendering hỗ trợ (miễn `⚠️ Unverified` từng dòng, nêu tập trung ở "Unverified claims"). Backfill toàn bộ 8 đề. Chi tiết trong `frontmatter_schema.md` §exam-note |
| Q18 | **Chuẩn hóa lại trình bày exam-note (thay một phần Q16/Q17).** (1) Bỏ khối "Nguyên tắc" đầu file. (2) Nguồn đáp án gộp thành **một dòng note đầu page** `> **Nguồn đáp án:** [[MOC_Nguon_Tham_Khao]] (tra theo số câu).` — bỏ header "Nguồn đáp án (câu X~Y)" rải theo nhóm câu VÀ **bỏ `[RA:nn-Qm]` inline** trong bảng phương án (đáp án đúng nhận ra qua Vai ✅). (3) Trong `### Chú giải chi tiết`, **mỗi ngữ pháp / mỗi từ vựng một dòng** (danh sách con, không dồn `·`/`;`), link `[[GR_*]]`/`[[VC_*]]`/`[[TOPIC_*]]` khi note tồn tại (từ thuộc topic → link `[[TOPIC_*]]`). (4) **Bỏ hẳn** hai section cuối `## Ghi chú xoáy ốc` và `## Unverified claims`; candidate-trap 1× theo dõi ở `Trap_Stats.md` + mô tả inline cột Căn cứ; exam-note **miễn** section "Unverified claims" (đáp án MOC authoritative — ngoại lệ có chủ đích so `source_citation_rule` §2). (5) Thêm bước tạo **VC note chọn lọc** cho cụm động từ+trợ động từ **lexical-hóa** (vd `V-고 다니다`, `알고 있다/알았다/알게 되다`, `-아/어 가다·오다`); trợ động từ ngữ pháp thuần vẫn để GR/inline. Áp cho template, skill `topik-exam-analysis`, `frontmatter_schema.md` §exam-note/§vocab-note; backfill toàn bộ 8 đề hiện có. |
| Q19 | Domain topik kích hoạt dạng đọc-hiểu **`sắp-xếp-thứ-tự`** (TOPIK ĐỌC **câu 13~15**, đề bài "다음을 순서대로 맞게 배열한 것을 고르십시오", hậu tố heading `순서대로 맞게 배열한 것`, dạng 5 trong `MOC_Dang_Bai`): chất liệu là **4 mảnh câu** (가)(나)(다)(라), 4 phương án là **hoán vị thứ tự**. Sinh **một layer mới `sequence-note`** (`TOPIK/47_Sequence/`, prefix `SEQ_`) tổ chức **theo kỹ thuật nối câu** (`mở-đầu\|hồi-chiếu\|kết-quả\|đối-lập\|bổ-sung\|thời-gian\|điều-kiện`), ngưỡng **≥2×** như trap-note (cue 1× → inline + candidate ở `Seq_Stats.md`), `role: correct` = "cue định vị mảnh trong chuỗi đúng" (five-check nới như topic-note); **KHÔNG** sinh GR/PAIR/GROUP/DIS/TOPIC/TRAP (VC vẫn tạo khi có cụm lexical-hóa). Exam block **4 cột** `# \| Thứ tự \| Vai \| Căn cứ / Phân tích` + dòng `**Trình tự đúng:** (X)→(Y)→(Z)→(W)` mức câu; render 문제/Dịch blockquote mỗi mảnh một dòng + `### Chú giải chi tiết` như mọi dạng (Q17). vault-sync đếm count + render marker + sinh dashboard `Seq_Stats.md`. Chi tiết `frontmatter_schema.md` §sequence-note. Backfill 8 đề (35/36/37/41/47/52/60/64) câu 13-15. |
