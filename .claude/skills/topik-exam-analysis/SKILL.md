---
name: topik-exam-analysis
description: Phân tích đề TOPIK (ảnh hoặc text) thành EXAM note + diff cho các layer Grammar/Pair/Group/Distractor/Topic/Trap/Sequence của learning-vault (domain: topik). Xử lý câu ngữ pháp (ngữ-pháp-chỗ-trống, ngữ-pháp-đồng-nghĩa), câu đọc-hiểu chủ đề (xác-định-chủ-đề — "무엇에 대한 글인지", ĐỌC câu 5~8), câu đọc-hiểu "내용과 같은 것" (câu-giống-đoạn-văn câu 9 poster + câu-giống-đồ-thị câu 10 đồ thị — sinh song song trap-note + topic-note), và câu sắp xếp thứ tự (sắp-xếp-thứ-tự — "순서대로 맞게 배열한 것", ĐỌC câu 13~15, 4 mảnh 가~라 — sinh sequence-note). Dùng skill này BẤT CỨ KHI NÀO người dùng đưa đề TOPIK mới, ảnh câu hỏi trắc nghiệm tiếng Hàn (ngữ pháp, quảng cáo/thông báo, poster, đồ thị, hoặc sắp xếp câu), yêu cầu "phân tích đề", "backfill đề cũ", hoặc nhắc đến việc thêm câu hỏi vào vault — kể cả khi họ chỉ dán một câu hỏi lẻ. Không dùng cho câu hỏi lý thuyết ngữ pháp thuần túy không gắn với đề.
---

# Exam Analysis Skill

Chuyển đề TOPIK thành dữ liệu có cấu trúc của vault theo 5 phase. **Không bao giờ ghi file trước Phase 4 (confirm).**

## Trước khi chạy

1. Đọc `.claude/rules/topik/frontmatter_schema.md`, `.claude/rules/_shared/naming_rule.md`, `.claude/rules/_shared/source_citation_rule.md`.
2. Đọc `CLAUDE.md` phần Quy tắc bắt buộc.
3. Khai danh tính cho hook (env không tới được hook): `mkdir -p .claude/state && echo topik-exam-analysis > .claude/state/active_skill`. Xong việc: `rm -f .claude/state/active_skill`.

## Phase 1 — Parse

- Đọc đề (ảnh/text). Với mỗi câu, trích: số câu, dạng bài, câu gốc nguyên văn Hangul, **bản dịch tiếng Việt toàn câu 문제** (mọi dạng — giữ `( )` và `__gạch chân__`), 4 phương án, đáp án đúng.
- **Chú giải chi tiết (Q17 + Q18 — bắt buộc mọi dạng):** với mỗi câu còn trích để dựng block `### Chú giải chi tiết`: chia chất liệu 문제/đoạn văn thành từng dòng → bản dịch dòng đó + **toàn bộ ngữ pháp** (không bỏ sót) + **toàn bộ từ vựng và cụm từ vựng** (không bỏ sót). **Q18 — mỗi ngữ pháp / mỗi từ vựng viết MỘT dòng** trong danh sách con của hai bullet `- **Ngữ pháp:**` / `- **Từ vựng:**` (không dồn nhiều mục trên một dòng). Link: `[[GR_*]]` cho ngữ pháp khi note tồn tại (KHÔNG appearances / KHÔNG tạo GR mới); `[[VC_*]]` cho cụm lexical-hóa có VC note; **nếu từ thuộc một topic category thì link `[[TOPIC_*]]`**. Ngoài ra trích **phân tích đúng/sai từng đáp án** (2-3 câu, trích dẫn chất liệu Hàn + tên bẫy) để ghi vào cột cuối bảng phương án — cột "Lý do / Phân tích" (dạng ngữ pháp) hoặc nội dung cột "Căn cứ" (dạng chủ đề/câu-giống).
- **Nguồn đáp án (bắt buộc kiểm, Q18):** tra key trong `TOPIK/90_MOC/MOC_Nguon_Tham_Khao.md` (bảng đáp án bộ đề ĐỌC theo số câu) để xác định đáp án đúng mỗi câu. **Trong exam-note KHÔNG cite `[RA:nn-Qm]` inline nữa** — chỉ đặt **một dòng note nguồn đáp án ở đầu page** ngay dưới tiêu đề: `> **Nguồn đáp án:** [[MOC_Nguon_Tham_Khao]] (tra theo số câu).`. Đáp án đúng nhận ra qua cột **Vai ✅** trong bảng phương án. Nếu người dùng đã cung cấp phân tích trong hội thoại thì đối chiếu thêm. Chỉ khi MOC KHÔNG phủ câu đó mới tự giải (nêu rõ trong phân tích cột cuối). Đáp án lấy từ MOC là authoritative.
- **Dạng bài** (slug tra ở `TOPIK/90_MOC/MOC_Dang_Bai.md` — không lưu trong frontmatter, chỉ ghi ở heading `## Câu {N} — dạng {slug} ({hậu tố 한국어})`; hậu tố tra cột "Hậu tố heading" trong `MOC_Dang_Bai`):
  - `ngữ-pháp-chỗ-trống` [~1~2]: điền ngữ pháp vào chỗ trống.
  - `ngữ-pháp-đồng-nghĩa` [~3~4]: chọn ngữ pháp đồng nghĩa cụm gạch chân.
  - `xác-định-chủ-đề` [ĐỌC câu ~5~8]: "무엇에 대한 글인지 고르십시오" — chọn xem quảng cáo/thông báo nói về CHỦ ĐỀ gì. 4 phương án là danh từ chủ đề (신문/병원/…), KHÔNG phải ngữ pháp. Với dạng này trích thêm: **toàn văn** quảng cáo/thông báo (giữ xuống dòng), nghĩa từng phương án, và **từ khóa tín hiệu** dẫn tới đáp án.
  - `câu-giống-đoạn-văn` [ĐỌC câu 9] + `câu-giống-đồ-thị` [ĐỌC câu 10]: "내용과 같은 것을 고르십시오" — 4 phương án là **câu văn khẳng định** (không phải ngữ pháp/danh từ chủ đề). Trích thêm: chất liệu đọc (câu 9 = poster/안내문/광고 giữ xuống dòng; câu 10 = số liệu đồ thị/도표), nghĩa từng phương án, kỹ thuật bẫy của mỗi phương án sai, và **chủ đề chất liệu** (để sinh topic — xem 2c).
  - `sắp-xếp-thứ-tự` [ĐỌC câu 13~15]: "다음을 순서대로 맞게 배열한 것을 고르십시오" — chất liệu là **4 mảnh câu** đánh dấu (가)(나)(다)(라); 4 phương án là **hoán vị thứ tự** (vd `(다)-(나)-(라)-(가)`), KHÔNG phải ngữ pháp/danh từ/câu khẳng định. Trích thêm: **nguyên văn Hangul từng mảnh 가~라** + dịch từng mảnh, 4 phương án hoán vị, đáp án từ MOC. **Suy chuỗi đúng:** map số đáp án (MOC) → phương án hoán vị tương ứng → chuỗi đúng; xác định **cue nối câu** của từng mảnh (mảnh mở đầu không 지시어/접속부사; 지시어/그중 하나 = hồi chiếu → sau tiền ngữ; 그래서/따라서 = kết quả; 하지만/그런데 = đối lập; 또한/그리고 = bổ sung). Ghi dòng `**Trình tự đúng:** (X)→(Y)→(Z)→(W)` mức câu (xem 2e).
- Gán exam_id theo **số hiệu kỳ thi TOPIK thật** dạng `TOPIK_{nn}` (vd `TOPIK_83`); hỏi người dùng nếu đề không ghi số hiệu. Không dùng ID tuần tự Dnn.
- Dựng nội dung `TOPIK_{nn}.md` theo `TOPIK/00_Templates/Exam_Question_Template.md` — trong RAM, chưa ghi.

## Phase 2 — Match

### 2a. Câu dạng `xác-định-chủ-đề` (carve-out — KHÔNG đụng GR/PAIR/GROUP/DIS)

Câu chủ đề không có pattern ngữ pháp để match. Layer `topic-note` tổ chức **theo category** (1 file = 1 category-theme, xem taxonomy trong `frontmatter_schema.md`), KHÔNG mỗi đáp án một file.

- Với **mỗi phương án ĐÚNG**: xác định category-theme của nó (theo bảng taxonomy; theme mới ngoài bảng → đề xuất bổ sung taxonomy). Quét `TOPIK/45_Topics/` theo field `topic`(=category):
  - `EXISTS`: append `history` `{exam, q, role: correct, reason: "{từ} — {tín hiệu}"}` + thêm từ vào `members` (nếu chưa có) + thêm dòng vào bảng "Từ vựng theo category" trong body.
  - `NEW`: tạo file category từ `Topic_Template.md` (điền `members`, `select_signal`, `kill_signal` nếu có, bảng từ vựng, marker sync).
- Phương án **chỉ làm nhiễu**: ghi inline trong exam note (cột Chủ đề `—`, Vai ❌ + căn cứ). **KHÔNG tạo note — kể cả khi tái xuất ≥2×** (khác DIS ngữ pháp).
- Exam note dạng này dùng **block variant chủ đề** (bảng `# | Phương án | Nghĩa | Chủ đề | Vai | Căn cứ`); phương án đúng link file category chứa nó `[[TOPIC_{category}]]` (vd 냉장고 → `[[TOPIC_가전제품]]`), nhiễu để `—`.

### 2b. Câu dạng ngữ pháp (`ngữ-pháp-chỗ-trống` / `ngữ-pháp-đồng-nghĩa`)

Với từng ngữ pháp xuất hiện (đáp án đúng + cả 3 nhiễu của mỗi câu):

- Quét `TOPIK/10_Grammar/` theo field `pattern` → phân loại:
  - `EXISTS`: note đã có → chuẩn bị append vào `appearances`.
  - `NEW`: chưa có → chuẩn bị tạo note mới từ `GR_Analysis_Template.md`, gán `group` (quét `TOPIK/25_Groups/`; nhóm chưa tồn tại → đề xuất tạo GROUP mới).
  - `PAIR-CANDIDATE`: dạng ngữ-pháp-đồng-nghĩa mà cặp (gạch chân ↔ đáp án) chưa có PAIR note, hoặc PAIR `confidence: open` vừa được thi chiều ngược → đề xuất tạo/khép.
- Ngữ pháp làm nhiễu ≥2 lần (tính cả lịch sử) mà chưa có DIS note → đề xuất tạo.

### 2c. Câu dạng câu-giống (`câu-giống-đoạn-văn` câu 9 + `câu-giống-đồ-thị` câu 10 — dual-layer, Q15)

Hai dạng này sinh **song song hai layer**: `trap-note` (theo kỹ thuật bẫy) + `topic-note` (theo category chủ đề). KHÔNG đụng GR/PAIR/GROUP.

**(a) trap-note** (`TOPIK/46_Traps/`, ngưỡng ≥2× giống DIS): với mỗi phương án SAI, xác định kỹ thuật bẫy (taxonomy trong `frontmatter_schema.md` §trap-note). Quét `TOPIK/46_Traps/` theo `trap_id`:
  - `EXISTS`: append `history` `{exam, q, role: distractor, reason: "{①/kỳ} ..."}` + cập nhật `members` nếu có biểu hiện mới.
  - Bẫy mới xuất hiện **≥2×** (tính cả lịch sử, cả 2 vai) mà chưa có note → đề xuất tạo từ `Trap_Template.md` (điền `scope`, `category`, `kill_signal`, `select_signal`, marker sync). Bẫy 1× ghi inline (cột Căn cứ, KHÔNG link) + liệt kê candidate.

**(b) topic-note** (`TOPIK/45_Topics/`, ngưỡng **1×**): xác định **chủ đề của chất liệu đọc** (poster/đồ thị — KHÔNG lấy từ 4 phương án) → map category (câu 9 poster → `광고/안내`; câu 10 đồ thị → `화제`; theme mới ngoài taxonomy → đề xuất bổ sung). Quét `TOPIK/45_Topics/` theo field `topic`(=category-theme):
  - `EXISTS`: append `history` `{exam, q, role: correct, reason: "{chủ đề} — {tín hiệu}"}` + thêm từ khóa chủ đề vào `members` + thêm dòng vào bảng "Từ vựng theo category".
  - `NEW`: tạo file category từ `Topic_Template.md` (append/tạo **ngay 1×**, như dạng chủ đề câu 5-8).

**(c) exam block**: dùng bảng **5 cột** `# | Phương án | Nghĩa | Vai | Căn cứ` (phương án sai có note → `[[TRAP_*]]`; đúng nhận ra qua Vai ✅, KHÔNG cite `[RA:]` trong exam — Q18). Thêm dòng `**Chủ đề:** {theme} → [[TOPIC_{category-theme}]]` **ở mức câu** (dưới khối `**Dịch:**`, trước bảng — KHÔNG thêm cột vào bảng).

### 2d. VC note — cụm từ vựng lexical-hóa (Q18, mọi dạng bài)

Khi chú giải một câu (bất kỳ dạng nào) chứa **cụm động từ + trợ động từ/ngữ pháp đã lexical-hóa** (nghĩa/sắc thái riêng, không suy ra trực tiếp từ nghĩa đen), tạo/append layer `vocab-note` (`TOPIK/40_Vocab/`) và link `[[VC_*]]` ở bullet Từ vựng.

- **Tiêu chí chọn lọc:** chỉ cụm mang nghĩa lexical-hóa/sắc thái riêng (vd `V-고 다니다`, `알고 있다 / 알았다 / 알게 되다`, `-아/어 가다·오다`, `놓고/두고/안 가지고 나오다`, `문을 열다` = khai trương). **KHÔNG** ép trợ động từ ngữ pháp thuần (`V-고 있다`, `-게 되다`, `-아/어 있다`, `-아/어 주다`…) thành VC — chúng để dạng GR (link `[[GR_*]]` nếu có) hoặc gloss inline.
- Quét `TOPIK/40_Vocab/` theo field `pattern`:
  - `EXISTS`: append `source` `[TOPIK_nn-Qm]` + thêm dòng vào bảng "Xuất hiện trong đề" trong body.
  - `NEW`: tạo file từ `Vocab_Pattern_Template.md`, đặt tên theo `naming_rule` (`VC_{pattern}`); điền `pattern`, `related_grammar` (list `GR_*` liên quan, có thể `[]`), `source`.
- Nếu từ/cụm thuộc một **topic category** (đáp án dạng chủ đề, hay từ khóa chủ đề chất liệu đọc) → link `[[TOPIC_*]]` ở bullet Từ vựng (không tạo VC trùng).

### 2e. Câu dạng `sắp-xếp-thứ-tự` (câu 13~15 — single-layer sequence-note, Q19)

Dạng sắp xếp thứ tự sinh **một layer duy nhất `sequence-note`** (`TOPIK/47_Sequence/`, tổ chức **theo kỹ thuật nối câu**, 1 file = 1 kỹ thuật; taxonomy trong `frontmatter_schema.md` §sequence-note). KHÔNG đụng GR/PAIR/GROUP/DIS/TOPIC/TRAP (VC vẫn tạo ở 2d khi có cụm lexical-hóa; link `[[GR_*]]` nền khi note tồn tại).

- Với mỗi câu, xác định **cue quyết định chuỗi đúng** (thường 2-4 cue/câu): mảnh **mở đầu** (nêu chủ đề/định nghĩa, không 지시어/접속부사); mảnh **hồi chiếu** (이것/이런/그것/그중 하나 → phải sau tiền ngữ); mảnh **kết quả** (그래서/따라서/그러므로 → sau nguyên nhân); mảnh **đối lập** (하지만/그런데); mảnh **bổ sung** (또한/그리고). Map mỗi cue → category enum (`mở-đầu|hồi-chiếu|kết-quả|đối-lập|bổ-sung|thời-gian|điều-kiện`).
- Quét `TOPIK/47_Sequence/` theo `cue_id`:
  - `EXISTS`: append `history` `{exam, q, role: correct, reason: "({mảnh}) {biểu hiện} → {ràng buộc vị trí}"}` + cập nhật `members` nếu có biểu hiện mới.
  - Cue mới xuất hiện **≥2×** (tính cả lịch sử) mà chưa có note → đề xuất tạo từ `Sequence_Template.md` (điền `category`, `role_in_order`, `members`, `kill_signal`, `select_signal`, marker sync). Cue 1× ghi inline (cột Căn cứ, KHÔNG link) + liệt kê candidate (theo dõi ở `Seq_Stats.md`).
  - `role: distractor` (tùy chọn): khi một phương án SAI vi phạm cue rõ rệt (vd đặt mảnh chứa 지시어 lên đầu) → có thể log `{..., role: distractor, reason: "③ đặt (나) 이런 lên đầu"}` để cue tích lũy cả 2 vai.
- **exam block** (bảng **4 cột** `# | Thứ tự | Vai | Căn cứ / Phân tích`): cột "Thứ tự" ghi hoán vị mỗi phương án; đáp án đúng Vai ✅ (KHÔNG cite `[RA:]`); cột cuối phân tích chuỗi móc nối (✅) hoặc lý do sai vi phạm cue (❌), cue có note → link `[[SEQ_*]]`. Thêm dòng `**Trình tự đúng:** (X)→(Y)→(Z)→(W)` **mức câu** (dưới khối `**Dịch:**`, trước bảng — KHÔNG thêm cột).

## Phase 3 — Propose

Tổng hợp thành **bảng diff duy nhất**, mỗi dòng một thao tác:

| # | Thao tác | File | Tóm tắt | Nguồn |
|---|---|---|---|---|
| 1 | CREATE | TOPIK/50_Exams/EXAM_D07.md | 4 câu, 2 dạng | [D07] |
| 2 | APPEND appearances | TOPIK/10_Grammar/GR_거나.md | +{D07, q1, distractor} | [D07-Q1-dis] |
| 3 | CREATE | TOPIK/20_Pairs/PAIR_x_y.md | thi chiều x→y, confidence: open | [D07-Q3] |
| ... |

Kèm danh sách `⚠️ Unverified` cần người dùng xác nhận.

## Phase 4 — Confirm ⛔ DỪNG BẮT BUỘC

- Trình bảng diff + unverified. **Batch mode** (backfill nhiều đề): gộp toàn bộ diff của mọi đề vào MỘT bảng, xin duyệt MỘT lần.
- Người dùng có thể: duyệt toàn bộ / loại từng dòng / sửa nội dung dòng. Chỉ tiếp tục khi có xác nhận rõ ràng.

## Phase 5 — Write

- Ghi theo diff đã duyệt. Mọi note mới: `status: draft` (Q2). `role_ratio`, `distractor_count`, `correct_count` để trống — vault-sync tính.
- Ghi xong → báo cáo phần đã ghi: số file tạo/sửa, note draft chờ verify, PAIR chuyển open→closed.
- **⛔ Hỏi xác nhận trước khi sync (DỪNG BẮT BUỘC):** hỏi người dùng có muốn chạy vault-sync ngay không (để tái sinh dashboard + tính counts + five-check). KHÔNG tự chạy.
  - **Đồng ý** → chạy vault-sync → báo cáo kết quả sync.
  - **Không / bỏ qua** → KHÔNG chạy vault-sync; nhắc người dùng dashboard/counts chưa cập nhật và có thể chạy `sync vault` sau.

## Lưu ý chất lượng

- **Q17 + Q18 — EXAM note CHỨA dịch + phân tích chi tiết** (đảo nguyên tắc reference-don't-duplicate cho phần dịch/gloss): mỗi câu gồm câu gốc + khối `**Dịch:**` + bảng phương án (cột cuối "Lý do / Phân tích" chứa phân tích đúng/sai đầy đủ, giữ link `[[GR_*]]`/`[[TOPIC_*]]`/`[[TRAP_*]]` + Vai) + block `### Chú giải chi tiết` (dịch theo dòng + **toàn bộ** ngữ pháp + **toàn bộ** từ vựng/cụm, không bỏ sót). Layer note (`[[GR_*]]`/`[[TOPIC_*]]`/`[[TRAP_*]]`) vẫn giữ tín hiệu select/kill + appearances gộp — KHÔNG trùng vai trò với chú giải trong exam.
- **Q18 — chú giải mỗi mục một dòng:** trong `### Chú giải chi tiết`, bullet `- **Ngữ pháp:**` và `- **Từ vựng:**` mở danh sách con, **mỗi ngữ pháp / mỗi từ vựng một dòng** (không dồn `·`/`;`). Link `[[GR_*]]`/`[[VC_*]]`/`[[TOPIC_*]]` khi note tồn tại.
- **Q18 — cấu trúc file exam:** đầu page chỉ một dòng `> **Nguồn đáp án:** [[MOC_Nguon_Tham_Khao]] (tra theo số câu).` (KHÔNG khối "Nguyên tắc", KHÔNG header "Nguồn đáp án" rải theo nhóm câu). **Bỏ hẳn** hai section cuối `## Ghi chú xoáy ốc` và `## Unverified claims`. Candidate-trap 1× nay chỉ theo dõi ở `Trap_Stats.md` (dashboard, vault-sync sinh) + mô tả inline ở cột Căn cứ; KHÔNG còn liệt kê trong exam-note.
- **Giữ nguyên cấu trúc bảng phương án** (# | Phương án | {Ngữ pháp/Nghĩa/…} | Vai ✅❌ | Lý do / Phân tích): vault-sync five-check đọc bảng này verify appearances. Chỉ nới cột cuối, KHÔNG bỏ cột link/Vai. **KHÔNG cite `[RA:]` trong ô đáp án đúng** (Q18 — nguồn đáp án ở đầu page).
- Mọi dạng bài render `**문제:**` bằng **blockquote nhiều dòng** rồi tới khối `**Dịch:**` blockquote dịch song song từng dòng (giữ `( )` / `__gạch chân__`), trước bảng phương án — theo `frontmatter_schema.md` phần exam-note. Bản dịch + chú giải chi tiết là rendering hỗ trợ → không cần `⚠️ Unverified` từng dòng; exam-note **miễn** section "Unverified claims" (đáp án MOC authoritative), người duyệt [XV] rà khi nâng `status: verified`.
- Topic note (category) mới: điền `topic`(=category), `topic_vi`, `category` (광고/안내/화제), `members`, `select_signal` (bắt buộc), `kill_signal` (khi có), `history` gộp, bảng "Từ vựng theo category", marker sync; `correct_count`/`distractor_count` để trống — vault-sync tính. **Câu 9-10 (Q15):** chủ đề lấy từ chất liệu đọc (không từ phương án), `role: correct`, ngưỡng 1×.
- Trap note (kỹ thuật bẫy) mới (chỉ khi ≥2×): điền `trap_id`(=tên file), `trap_name`, `scope` (poster/đồ-thị/cả-hai), `category`, `members` (khi có), `kill_signal` + `select_signal` (bắt buộc), `history` gộp, marker sync; `correct_count`/`distractor_count` để trống.
- **Câu 9-10 sinh song song cả trap-note LẪN topic-note** — Phase 5 liệt kê đủ cả hai loại file trong diff/summary; exam block có dòng `**Chủ đề:** … → [[TOPIC_*]]`.
- Grammar note mới: điền tối thiểu section 1, 2, 4, 7 của template + marker compile; section khác để khung trống chờ bổ sung.
- Không tự sửa note `status: verified`; cần sửa → đưa vào diff dạng PROPOSE-EDIT chờ duyệt.
