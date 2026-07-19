# Frontmatter Schema Rule

Mọi note phải có frontmatter hợp lệ theo loại. Skill validate TRƯỚC khi ghi (Phase 1 của vault-sync/grammar-compile chạy five-check: schema hợp lệ / enum hợp lệ / link tồn tại / appearances khớp EXAM / marker compile đầy đủ). Vi phạm → báo ⚠️, KHÔNG tự sửa.

## Chung (mọi loại)

| Field | Bắt buộc | Giá trị |
|---|---|---|
| `type` | ✅ | `grammar-note` / `pair-note` / `group-note` / `distractor-note` / `exam-note` / `vocab-note` / `topic-note` / `trap-note` / `moc-note` |
| `status` | ✅ | `draft` → `verified` (chỉ con người nâng) / `imported` (từ sr5-import) / `needs-review` |
| `created` | ✅ (trừ exam-note) | YYYY-MM-DD |
| `source` | ✅ (trừ exam-note) | list tag nguồn, xem source_citation_rule |
| `tags` | ✅ | tối thiểu `korean/grammar` hoặc `korean/vocab` |

> **Ngoại lệ exam-note:** không dùng `title`, `source`, `created`, `question_count`, `question_types`. Định danh bằng `exam_id` (= tên file, thay `title`) + `date_analyzed`. Dạng bài không lưu trong frontmatter — tra ở [[MOC_Dang_Bai]], ghi ở heading mỗi câu.

## grammar-note (TOPIK/10_Grammar)

```yaml
type: grammar-note
pattern: "-더니"              # bắt buộc, Hangul
level: "TOPIK II (3-4)"
group: GROUP_hoi_tuong        # bắt buộc, phải tồn tại trong TOPIK/25_Groups
stage: ""                     # GĐ 1-5, optional
stt_goc: ""                   # optional (Q5), điền khi sr5-import
pair_with: [GR_았더니]        # optional, list link
appearances:                  # bắt buộc, có thể rỗng []
  - {exam: TOPIK_37, q: 1, role: distractor}   # role: correct | distractor
role_ratio: ""                # vault-sync tự tính "1C/1D" — không điền tay
sr-due:
sr-interval:
sr-ease:
```

## pair-note (TOPIK/20_Pairs)

```yaml
type: pair-note
members: [GR_탓에, GR_바람에]          # đúng 2 phần tử, thứ tự theo tần suất
equivalence: two-way                    # two-way | one-way | conditional
tested_directions:
  - {exam: TOPIK_37, q: 3, prompt: 탓에, answer: 바람에}
morph_note: "탓에 dùng -(으)ㄴ | 바람에 cố định -는"
confidence: closed                      # open (thi 1 chiều) | closed (đủ 2 chiều)
group: GROUP_nguyen_nhan                # nhóm chứa cặp
```

## group-note (TOPIK/25_Groups)

```yaml
type: group-note
group_id: GROUP_nguyen_nhan             # trùng tên file
group_name: "Nguyên nhân — lý do"
members: [GR_아어서, GR_으니까, ...]    # ≥3
pairs_inside: [PAIR_탓에_바람에]
diff_axes: [sắc_thái_kết_quả, chủ_ngữ, vế_sau_cấm, ...]
confusion_pairs:
  - {a: GR_느라, b: GR_바람에, key: "느라 cần V chủ ý + cùng chủ ngữ"}
```

## distractor-note (TOPIK/30_Distractors)

```yaml
type: distractor-note
pattern: "-거나"
history:                                # mọi lần xuất hiện, cả 2 vai
  - {exam: TOPIK_41, q: 1, role: distractor, reason: "không có vế lựa chọn"}
  - {exam: TOPIK_64, q: 1, role: correct, reason: "보통 + 2 hành động cùng cấp"}
distractor_count: 0                     # vault-sync tự tính
correct_count: 0                        # vault-sync tự tính
kill_signal: "..."                      # bắt buộc — điều kiện loại 3 giây
select_signal: "..."                    # bắt buộc — môi trường nó ĐÚNG
```

## exam-note (TOPIK/50_Exams)

```yaml
type: exam-note
exam_id: TOPIK_XX             # số hiệu kỳ thi thật, vd TOPIK_83 (= tên file, thay title)
date_analyzed: YYYY-MM-DD
status: draft                           # verified → immutable (hook chặn)
tags: [korean/topik, exam]
```

Exam-note KHÔNG lưu `question_count` / `question_types` / `source` / `created` / `title`. Dạng bài mỗi câu ghi ở heading `## Câu {N} — dạng {slug} ({hậu tố 한국어})` cho **mọi dạng** (slug + hậu tố tra ở [[MOC_Dang_Bai]] — cột "Slug" và "Hậu tố heading"; dạng ngữ pháp đồng nghĩa dùng slug `ngữ-pháp-đồng-nghĩa`). VD: `## Câu 8 — dạng xác-định-chủ-đề (무엇에 대한 글인지)`.

**Cấu trúc file (Q18):** frontmatter → `# Đề TOPIK_nn` → **một dòng note nguồn đáp án** `> **Nguồn đáp án:** [[MOC_Nguon_Tham_Khao]] (tra theo số câu).` → các block câu → **hết**. KHÔNG còn khối "Nguyên tắc" đầu file, KHÔNG header "Nguồn đáp án (câu X~Y)" rải theo nhóm câu, và **KHÔNG** hai section cuối `## Ghi chú xoáy ốc` / `## Unverified claims`. `[RA:nn-Qm]` **không xuất hiện trong exam-note** (đáp án tra ở MOC; đáp án đúng nhận ra qua cột **Vai ✅** trong bảng phương án). Exam-note **miễn** section "Unverified claims" (ngoại lệ có chủ đích so với `source_citation_rule` §2): đáp án MOC authoritative, còn dịch/gloss/phân tích là rendering hỗ trợ — người duyệt [XV] rà khi nâng `status: verified`. Candidate-trap 1× theo dõi ở `Trap_Stats.md` (dashboard) + mô tả inline ở cột Căn cứ, KHÔNG liệt kê trong exam-note.

Trình bày `**문제:**` (bắt buộc, mọi dạng bài): câu gốc đặt trong **blockquote nhiều dòng** (`> …`), ngay dưới là **khối `**Dịch:**` blockquote** dịch tiếng Việt song song từng dòng, rồi mới tới bảng phương án. Giữ `( )` cho câu ngữ-pháp-chỗ-trống và `__gạch chân__` cho câu ngữ-pháp-đồng-nghĩa trong cả câu gốc lẫn bản dịch. Bản dịch là rendering câu nguồn (không phải claim ngữ pháp) → KHÔNG cần gắn `⚠️ Unverified`; người duyệt chỉnh lại khi nâng `status: verified`.

```markdown
**문제:**
> {câu gốc Hangul, có thể nhiều dòng}

**Dịch:**
> {bản dịch tiếng Việt, mỗi dòng tương ứng một dòng Hàn}
```

**Block bắt buộc cuối MỖI câu (mọi dạng bài) — `### Chú giải chi tiết` (chuẩn hóa Q17 + Q18):** sau bảng phương án, mỗi câu kết thúc bằng **một block `### Chú giải chi tiết`** thay cho hai dòng tóm tắt cũ (`**Ngữ pháp:**` / `**Từ vựng:**` đã bỏ). Block chia chất liệu 문제/đoạn văn thành **từng dòng (hoặc từng câu)**, mỗi dòng gồm: dòng Hàn (blockquote `>`), mũi tên `→` bản dịch dòng đó, rồi hai bullet `- **Ngữ pháp:**` / `- **Từ vựng:**` mở **danh sách con — Q18: mỗi ngữ pháp / mỗi từ vựng một dòng** (không dồn `·`/`;` trên một dòng), liệt kê **toàn bộ** — **không bỏ sót**:

```markdown
### Chú giải chi tiết

> {dòng Hàn 1}
→ {dịch dòng 1}
- **Ngữ pháp:**
  - {pattern — giải thích ngắn} · [[GR_*]]   ← link NẾU note tồn tại, chưa có thì nêu inline (KHÔNG tạo link gãy / KHÔNG tạo GR mới / KHÔNG appearances)
  - {pattern 2 — giải thích} · …
- **Từ vựng:**
  - {từ — nghĩa}
  - {cụm lexical-hóa — nghĩa} · [[VC_*]]   ← link nếu VC note tồn tại
  - {từ thuộc topic category — nghĩa} · [[TOPIC_*]]   ← nếu từ thuộc một topic thì link tới TOPIC

> {dòng Hàn 2}
→ {dịch dòng 2}
- **Ngữ pháp:**
  - …
- **Từ vựng:**
  - …
```

- **Phân tích đúng/sai từng đáp án** KHÔNG tách block riêng: viết đầy đủ (2-3 câu, trích dẫn chất liệu Hàn + tên bẫy) **vào cột cuối của bảng phương án** — cột này đổi tên "Lý do 1 dòng" → **"Lý do / Phân tích"** (dạng ngữ pháp) hoặc mở rộng nội dung cột **"Căn cứ"** (dạng chủ đề / câu-giống). Bảng phương án + cột `[[GR_*]]`/`[[TOPIC_*]]`/`[[TRAP_*]]` + cột Vai ✅❌ **giữ nguyên cấu trúc** (vault-sync five-check đọc bảng này để verify appearances).
- **Ngữ pháp trong block với câu đọc-hiểu (5~12) là ngữ pháp NỀN:** chỉ link `[[GR_*]]` khi note đã có, **KHÔNG append `appearances`, KHÔNG tạo GR note mới** (enum `role` chỉ `correct|distractor`, ngữ pháp nền không thuộc hai vai này).
- Nội dung dịch theo dòng + gloss từ vựng + phân tích ngữ pháp/đáp án là **rendering hỗ trợ** (như bản Dịch) → KHÔNG cần `⚠️ Unverified` từng dòng. Exam-note KHÔNG còn section "Unverified claims" (Q18) — người duyệt [XV] rà toàn bộ khi nâng `status: verified`.

Ghi chú dạng bài `xác-định-chủ-đề` (đọc-hiểu, TOPIK ĐỌC câu 5~8 "무엇에 대한 글인지 고르십시오"): câu KHÔNG có phương án ngữ pháp → block trong exam note dùng bảng `# | Phương án | Nghĩa | Chủ đề | Vai | Căn cứ`. **Chỉ phương án ĐÚNG** link tới file category chứa nó `[[TOPIC_{category}]]` (vd 냉장고 → `[[TOPIC_가전제품]]`); phương án nhiễu để `—` (KHÔNG link, KHÔNG sinh note — dù tái xuất ≥2×). Các câu này sinh/append layer `topic-note` **theo category**, KHÔNG sinh GR/PAIR/GROUP/DIS.

Ghi chú dạng bài đọc-hiểu "내용과 같은 것" (TOPIK ĐỌC "다음 글 또는 도표의 내용과 같은 것을 고르십시오") — **hai slug tách theo chất liệu**: **câu 9 poster/안내문/광고 → slug `câu-giống-đoạn-văn` (글의 내용과 같은 것)**; **câu 10 đồ thị/도표/그래프 → slug `câu-giống-đồ-thị` (도표의 내용과 같은 것)**. Cả hai: 4 phương án là **câu văn khẳng định** (không phải ngữ pháp, không phải danh từ chủ đề) → block dùng bảng **5 cột** `# | Phương án | Nghĩa | Vai | Căn cứ`. Render 문제: **poster/안내문 (câu 9)** đặt trong blockquote nhiều dòng như thường; **đồ thị/그래프 (câu 10)** thay khối blockquote bằng dòng `**문제 (도표):** {tiêu đề}` + **bảng số liệu thường** (biểu đồ không đặt vừa blockquote) rồi tới `**Dịch:**`. Cột Căn cứ: phương án ĐÚNG nhận ra qua Vai ✅ (Q18 — KHÔNG cite `[RA:]` trong exam, nguồn đáp án ở dòng note đầu page); phương án bẫy có note thì link `[[TRAP_{ten}]]` (vd đảo so sánh → `[[TRAP_dao_so_sanh]]`), bẫy 1× chưa có note thì mô tả inline (KHÔNG link). Cả hai slug sinh/append **hai layer song song** (Q15): (1) `trap-note` **theo kỹ thuật bẫy** (ngưỡng ≥2×, giống DIS) và (2) `topic-note` **theo category chủ đề** (ngưỡng 1×, lấy từ chất liệu đọc — xem §topic-note); KHÔNG sinh GR/PAIR/GROUP. Chủ đề ghi ở **mức câu**: ngay dưới khối `**Dịch:**` (trước bảng phương án) thêm dòng `**Chủ đề:** {theme} → [[TOPIC_{category-theme}]]` (KHÔNG thêm cột vào bảng 5 cột — bảng giữ nguyên `# | Phương án | Nghĩa | Vai | Căn cứ`).

Ghi chú dạng bài `câu-giống-đoạn-văn-dài` (đọc-hiểu "내용과 같은 것", TOPIK ĐỌC **câu 11~12** — chất liệu là **đoạn văn dài / văn xuôi 줄글** nhiều câu, khác poster câu 9 và đồ thị câu 10) — **Q16**: render y hệt `câu-giống-đoạn-văn` (câu 9): 4 phương án là **câu văn khẳng định** → bảng **5 cột** `# | Phương án | Nghĩa | Vai | Căn cứ`; 문제 đặt trong **blockquote nhiều dòng** (văn xuôi), rồi khối `**Dịch:**`, rồi dòng `**Chủ đề:** {theme} → [[TOPIC_{category-theme}]]` ở mức câu. Cột Căn cứ: đúng nhận ra qua Vai ✅ (KHÔNG cite `[RA:]` trong exam — Q18), bẫy có note link `[[TRAP_*]]`, bẫy 1× mô tả inline. Sinh **hai layer song song** như câu 9-10: (1) `trap-note` (ngưỡng ≥2×) và (2) `topic-note` **category `화제`** (ngưỡng 1×, chủ đề lấy từ **đoạn văn**, KHÔNG từ 4 phương án); KHÔNG sinh GR/PAIR/GROUP. Kết câu bằng block `### Chú giải chi tiết` như mọi dạng (Q17).

## topic-note (TOPIK/45_Topics) — MODEL THEO CATEGORY

Layer tín hiệu đọc chủ đề cho **bốn dạng**: `xác-định-chủ-đề` (câu 5~8), `câu-giống-đoạn-văn` (câu 9, Q15) + `câu-giống-đồ-thị` (câu 10, Q15), và `câu-giống-đoạn-văn-dài` (câu 11~12, Q16). **1 file = 1 category** (chủ đề gộp), KHÔNG phải mỗi đáp án một file. Từ vựng cùng chủ đề gom vào một file category; `history` **gộp** mọi thành viên (cả 2 vai) → tái dùng nguyên cơ chế vault-sync (1 block appearances, đếm count như DIS).

**Luật tạo note:**
- **Dạng `xác-định-chủ-đề` (câu 5~8):** chỉ phương án ĐÚNG mới sinh/append category note (chủ đề = chính từ vựng đáp án). Phương án nhiễu chỉ ghi inline trong exam note (`—`), KHÔNG bao giờ tạo note — kể cả khi tái xuất ≥2×.
- **Dạng `câu-giống-đoạn-văn` / `câu-giống-đồ-thị` (câu 9-10, Q15) + `câu-giống-đoạn-văn-dài` (câu 11-12, Q16):** chủ đề lấy từ **chất liệu đọc** (poster / đồ thị / đoạn văn dài), KHÔNG từ 4 phương án (phương án là câu văn). Mỗi câu 9/10/11/12 xuất hiện là sinh/append category note **ngay (ngưỡng 1×)**, `role: correct` = "chủ đề bài này xuất hiện", `reason` mở đầu bằng chủ đề `"{chủ đề} — {tín hiệu nhận diện}"`. Category theo mapping: **câu 9 poster/안내문/광고 → `광고` hoặc `안내`; câu 10 đồ thị/도표 → `화제`; câu 11-12 đoạn văn → `화제`** (tái dùng enum cũ, KHÔNG mở rộng). Từ khóa chủ đề gom vào `members`. Đây SONG SONG với trap-note cùng câu — không loại trừ nhau.
- **Lưu ý five-check:** entry `history` nguồn câu 9-12 KHÔNG đòi `role` khớp một phương án đáp án cụ thể trong EXAM (chủ đề trích từ chất liệu, không phải phương án) — vault-sync chỉ verify exam+q tồn tại và dạng bài là dạng-sinh-topic.

```yaml
type: topic-note
topic: "가전제품"              # bắt buộc — tên category-theme (Hangul, = tên file bỏ dấu cách)
topic_vi: "đồ điện gia dụng"   # bắt buộc, gloss tiếng Việt
category: 광고                 # bắt buộc: 광고 | 안내 | 화제 (enum thô)
members: [냉장고, 선풍기, 에어컨]  # bắt buộc — list từ vựng đáp án trong category
history:                       # bắt buộc — gộp mọi thành viên; reason mở đầu bằng "{từ/chủ đề} — ..."
  - {exam: TOPIK_36, q: 5, role: correct, reason: "냉장고 — 신선도·온도 조절"}     # câu 5~8: từ = đáp án
  - {exam: TOPIK_41, q: 5, role: correct, reason: "선풍기 — 시원한 바람"}
  - {exam: TOPIK_52, q: 10, role: correct, reason: "인구변화 — 연령별 비율 도표"}   # câu 9-10 (Q15): chủ đề = chất liệu đọc
correct_count: 0              # vault-sync tự tính — không điền tay
distractor_count: 0           # vault-sync tự tính — không điền tay
select_signal: "..."          # bắt buộc — dấu hiệu bài THUỘC category này (mức category)
kill_signal: "..."            # optional — dấu hiệu loại category này
```

**Taxonomy category tham chiếu** (mở rộng khi có đề mới; `topic` = tên file):

| category (광고/안내/화제) | file `topic` | topic_vi | từ vựng ví dụ |
|---|---|---|---|
| 광고 | 가전제품 | đồ điện gia dụng | 냉장고, 선풍기, 에어컨 |
| 광고 | 식음료 | thực phẩm & đồ uống | 주스, 우유 |
| 광고 | 생활용품 | đồ dùng sinh hoạt | 휴지, 침대, 신문 |
| 광고 | 장소기관 | cơ sở / nơi chốn dịch vụ | 은행, 우체국, 식당, 마트, 빨래방, 안경점, 병원 |
| 광고 | 행사전시 | sự kiện / triển lãm | 꽃박람회, 축제, 대회, 전시회 |
| 화제 | 안전 | an toàn (giao thông/cháy) | 교통안전, 화재예방 |
| 화제 | 환경보호 | bảo vệ môi trường/thiên nhiên | 자연보호, 환경보호 |
| 화제 | 생활예절 | nếp sống / cộng đồng | 전화예절, 봉사활동 |
| 화제 | 애완동물 | thú cưng / vật nuôi | 애완동물, 반려동물 |
| 안내 | 이용안내 | hướng dẫn sử dụng / dịch vụ | 이용방법, 배달안내, 이용안내 |
| 안내 | 신청접수 | đăng ký / tiếp nhận / liên hệ | 사원모집, 접수방법, 문의방법 |
| 안내 | 주의사항 | điều cần lưu ý | 주의사항 |

Body bắt buộc: callout select/kill + **bảng "Từ vựng theo category"** (`Từ | Nghĩa | Select signal | Nguồn`, thủ công) + cặp marker `<!-- sync:appearances:start --> … <!-- sync:appearances:end -->` (vault-sync render bảng history gộp) + `## Liên kết`.

## vocab-note (TOPIK/40_Vocab)

```yaml
type: vocab-note
pattern: "V-고 다니다"
related_grammar: [GR_고_있다]
```

**Luật tạo VC (Q18 — chọn lọc):** tạo/append VC khi chú giải gặp **cụm động từ + trợ động từ/ngữ pháp đã lexical-hóa** — nghĩa/sắc thái riêng, không suy trực tiếp từ nghĩa đen (vd `V-고 다니다`, `알고 있다 / 알았다 / 알게 되다`, `-아/어 가다·오다`, `놓고/두고/안 가지고 나오다`, `문을 열다` = khai trương). **KHÔNG** ép trợ động từ ngữ pháp thuần (`V-고 있다`, `-게 되다`, `-아/어 있다`, `-아/어 주다`…) thành VC — để dạng GR (link `[[GR_*]]` nếu có) hoặc gloss inline. Đặt tên theo `naming_rule` (`VC_{pattern}`); `EXISTS` → append `source` + bảng "Xuất hiện trong đề"; `NEW` → tạo từ `Vocab_Pattern_Template.md`. Từ/cụm thuộc một **topic category** → link `[[TOPIC_*]]` (không tạo VC trùng). VC là layer tham chiếu (không có `appearances`/dashboard — vault-sync chỉ five-check schema).

## trap-note (TOPIK/46_Traps) — MODEL THEO KỸ THUẬT BẪY

Layer tín hiệu "bẫy đọc" cho ba dạng "내용과 같은 것": `câu-giống-đoạn-văn` (poster câu 9), `câu-giống-đồ-thị` (đồ-thị câu 10) và `câu-giống-đoạn-văn-dài` (đoạn văn dài câu 11-12, Q16). **1 file = 1 kỹ thuật bẫy** (không phải mỗi phương án một file). `history` **gộp** mọi lần kỹ thuật xuất hiện (cả 2 vai) → tái dùng nguyên cơ chế vault-sync (1 block appearances, đếm count như DIS/topic).

**Luật tạo note:** giống DIS — chỉ tạo file khi kỹ thuật bẫy xuất hiện **≥2×** (tính cả lịch sử, cả 2 vai). Bẫy 1× ghi inline trong exam note (mô tả ở cột Căn cứ, KHÔNG link) + theo dõi "candidate" ở `Trap_Stats.md` (dashboard — Q18 đã bỏ section `## Ghi chú xoáy ốc` trong exam-note); graduate thành note khi tái xuất.

```yaml
type: trap-note
trap_id: TRAP_dao_so_sanh        # bắt buộc, = tên file
trap_name: "Đảo chiều so sánh (A>B ↔ A<B)"   # bắt buộc
scope: đồ-thị                    # bắt buộc: poster (câu 9, 안내문/광고) | đồ-thị (câu 10, 도표) | văn-xuôi (câu 11-12, đoạn văn dài) | cả-hai (nhiều chất liệu)
category: so-sánh                # bắt buộc, enum thô. Poster/đồ-thị: phạm-vi | thời-hạn | miễn-phí | phương-thức | so-sánh | cực-trị | xu-hướng | bằng-nhau | ngưỡng | thứ-hạng. Văn-xuôi (Q16): đảo-thông-tin | đảo-thời-điểm | nói-quá | không-có-thông-tin | sai-mục-đích
members: []                      # optional — biểu hiện ngôn ngữ điển hình (cụm Hàn hay dựng bẫy)
history:                         # bắt buộc — gộp mọi lần, cả 2 vai; reason mở đầu bằng "{①/kỳ} ..."
  - {exam: TOPIK_36, q: 10, role: distractor, reason: "③ 자기 자신 남<여 (thực 남25.1>여18.7)"}
correct_count: 0                 # vault-sync tự tính — không điền tay
distractor_count: 0              # vault-sync tự tính — không điền tay
kill_signal: "..."               # bắt buộc — dấu hiệu 3 giây nhận ra phương án là bẫy
select_signal: "..."             # bắt buộc — khi phương án dùng chiêu này lại ĐÚNG
```

**Taxonomy bẫy tham chiếu** (mở rộng khi có đề mới; `trap_id` = tên file):

| category | file `trap_id` | scope | biểu hiện |
|---|---|---|---|
| thời-hạn | TRAP_lan_dau_vs_thu_N | poster | 처음/이번에 처음 ↔ 제N회 (đã tổ chức nhiều lần) |
| thời-hạn | TRAP_thoi_han_qua_rong | poster | 일 년/한 달/내내 khi poster ghi kỳ hạn cụ thể ngắn hơn |
| miễn-phí | TRAP_mien_phi_co_phi | cả-hai | 무료 ↔ 유료/돈 내야/사 먹다 (poster + văn xuôi) |
| phạm-vi | TRAP_chi_gioi_han | poster | "N만/오직" thu hẹp sai đối tượng thực |
| phương-thức | TRAP_phuong_thuc_dang_ky | poster | sai kênh (전화/홈피/이메일) hoặc thời điểm (예약·당일 불가) đăng ký |
| so-sánh | TRAP_dao_so_sanh | đồ-thị | A>B ↔ A<B đảo chiều so sánh |
| cực-trị | TRAP_doc_sai_cuc_tri | đồ-thị | 가장 많이/적다 đọc sai max/min |
| xu-hướng | TRAP_dao_xu_huong | đồ-thị | 늘었다 ↔ 줄었다 đảo xu hướng (so 2 mốc) |
| bằng-nhau | TRAP_khang_dinh_bang_nhau | đồ-thị | khẳng định A=B khi số liệu lệch |
| ngưỡng | TRAP_nguong_mot_nua | đồ-thị | 절반/반을 넘는다 so với mốc 50% |
| thứ-hạng | TRAP_thay_doi_thu_hang | đồ-thị | 순위 바뀜/변화 없음/떨어짐 (up/down/no-change) |
| đảo-thông-tin | *(candidate)* | văn-xuôi | đảo hành động/sự kiện: 전시(trưng bày)↔판매(bán), A했다↔B했다 |
| đảo-thời-điểm | *(candidate)* | văn-xuôi | 그때/옛날 (quá khứ) ↔ 최근/요즘 (gần đây); đảo mốc thời gian |
| nói-quá | *(candidate)* | văn-xuôi | tuyệt-đối-hóa: 잠시/일부 ↔ 항상/완전히/성격을 바꾸다 |
| không-có-thông-tin | *(candidate)* | văn-xuôi | phương án bịa / trái nội dung (đoạn văn không nói / nói ngược) |
| sai-mục-đích | *(candidate)* | văn-xuôi | đảo mục đích/lý do: 위해서 X (thực mục đích là Y) |

> Nhóm bẫy `văn-xuôi` (câu 11-12) mới xuất hiện 1× tại TOPIK_35 → còn **candidate** (chưa tạo file, chờ ≥2×); cột `trap_id` điền khi graduate.

Body bắt buộc: callout `[!tip] Kill signal` / `[!success] Select signal` (⚠️ Unverified) + `## Biểu hiện điển hình` + cặp marker `<!-- sync:appearances:start --> … <!-- sync:appearances:end -->` (vault-sync render bảng history gộp) + `## Liên kết`.
