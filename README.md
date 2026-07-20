# Learning Vault — Tổng quan (multi-domain)

Một vault Obsidian quản lý nhiều domain học tập. Nguồn định tuyến duy nhất: [`.claude/domains.yaml`](.claude/domains.yaml). Nội dung do skill của Claude Code sinh/sửa (kích hoạt **theo ngữ cảnh câu tiếng Việt** bạn nói, không phải lệnh gạch chéo), con người đọc & ôn trên Obsidian.

- **`TOPIK/`** — domain `topik`, **active**: đã phân tích 8 đề TOPIK II với đầy đủ layer ngữ pháp + đọc-hiểu.
- **`BA/`** — domain `ba`, **placeholder** (learn-first): khung thư mục dựng sẵn, schema/template/skill viết sau khi có ngữ liệu thật. Xem [`BA/README_BA.md`](BA/README_BA.md).

Ngôn ngữ làm việc: tiếng Việt; thuật ngữ Hàn giữ Hangul, thuật ngữ BA giữ tiếng Anh.

---

## 1. Kiến trúc

### Mô hình đa domain (Q6)
Một vault, **namespace theo domain** (mỗi domain một thư mục gốc), một **manifest** ([`.claude/domains.yaml`](.claude/domains.yaml)) định tuyến mọi skill/hook, và một **SR queue hợp nhất** cho mọi domain active. Thêm domain mới = thêm một block trong manifest + bộ template + (tùy chọn) skill riêng — không sửa skill dùng chung.

### Bản đồ layer domain `topik`

| Thư mục | Vai trò | Sửa tay? |
|---|---|---|
| `TOPIK/10_Grammar` | **Canonical** — mỗi ngữ pháp 1 note (`GR_*`), nội dung sống ở đây | ✅ qua Claude/tay |
| `TOPIK/20_Pairs` | Cặp ngữ pháp dễ nhầm (`PAIR_*`), quy đổi 2 chiều | ✅ |
| `TOPIK/25_Groups` | Nhóm ngữ pháp cùng loại (`GROUP_*`) — hub ma trận khác biệt | ✅ |
| `TOPIK/30_Distractors` | Hồ sơ "bẫy" nhiễu ngữ pháp (`DIS_*`) — kill/select signal | ✅ |
| `TOPIK/40_Vocab` | Cụm từ vựng lexical-hóa (`VC_*`) | ✅ |
| `TOPIK/45_Topics` | Chủ đề đọc-hiểu theo category (`TOPIC_*`) — câu ĐỌC 5~12 | ✅ |
| `TOPIK/46_Traps` | Kỹ thuật bẫy đọc-hiểu (`TRAP_*`) — câu "내용과 같은 것" | ✅ |
| `TOPIK/50_Exams` | Đề đã phân tích (`TOPIK_nn`) — **immutable khi `status: verified`** | ⚠️ khóa khi verified |
| `TOPIK/90_MOC` | Map of Content: taxonomy dạng bài + đáp án tham chiếu | ✅ |
| `TOPIK/00_Templates` | Khuôn note | 🔒 chỉ người / skill `template-editor` (hook chặn) |
| `TOPIK/99_Dashboard` | **Render tĩnh** do skill sinh | 🔒 không sửa tay (hook chặn) |
| `98_Views` | **Dataview sống** — người viết tay, Obsidian tự tính lại | ✅ tự do |
| `99_Global_Dashboard` | SR hợp nhất mọi domain (`Review_Today`) — *chưa sinh, tạo khi khởi tạo SR* | 🔒 chỉ skill |

> **Render vs View:** `99_Dashboard/*` = ảnh chụp tĩnh (chỉ đổi khi chạy lại skill → muốn đổi nội dung thì sửa note nguồn rồi chạy lại). `98_Views/*` = truy vấn Dataview sống (tự cập nhật mỗi lần mở).

**Quy mô hiện tại** (tính đến 2026-07): 8 đề (`TOPIK_35/36/37/41/47/52/60/64`), ~90 note ngữ pháp + 12 cặp + 18 nhóm + 23 nhiễu, cùng các layer đọc-hiểu Topic (~29) / Trap (~16) / Vocab (~15).

### Luồng dữ liệu
```
50_Exams (đề)  ──►  skill phân tích  ──►  câu ngữ pháp  ──►  10_Grammar · 20_Pairs · 25_Groups · 30_Distractors
                                     └─►  câu đọc-hiểu  ──►  45_Topics · 46_Traps · 40_Vocab
                                                                        │
                                                          99_Dashboard (render) + 98_Views (Dataview sống)
```

### Nguyên tắc chung (chi tiết trong [`CLAUDE.md`](CLAUDE.md))
1. **Reference-don't-duplicate** — nội dung sống ở note canonical; nơi khác chỉ link.
2. **No silent assumptions** — claim không truy được nguồn → `⚠️ Unverified`, chờ người duyệt.
3. **Source citation** — theo [`.claude/rules/_shared/source_citation_rule.md`](.claude/rules/_shared/source_citation_rule.md).
4. **Single-source render** — `99_Dashboard/` và `99_Global_Dashboard/` là output tự sinh, không sửa tay.
5. **Hybrid human-confirm** — skill đề xuất diff, ghi sau khi duyệt; batch đầu ghi `status: draft`, chỉ con người nâng `verified`.

---

## 2. Dạng bài đang phân tích

Domain `topik` xử lý phần **ĐỌC 읽기**; taxonomy đầy đủ ở [`TOPIK/90_MOC/MOC_Dang_Bai.md`](TOPIK/90_MOC/MOC_Dang_Bai.md), đáp án tham chiếu ở [`TOPIK/90_MOC/MOC_Nguon_Tham_Khao.md`](TOPIK/90_MOC/MOC_Nguon_Tham_Khao.md) (tag `[RA:nn-Qm]`).

| Dạng | Câu | Layer sinh ra |
|---|---|---|
| `ngữ-pháp-chỗ-trống` | ~1~2 | Grammar / Pair / Group / Distractor |
| `ngữ-pháp-đồng-nghĩa` | ~3~4 | Grammar / Pair / Group / Distractor |
| `xác-định-chủ-đề` (무엇에 대한 글인지) | ~5~8 | Topic |
| `câu-giống-đoạn-văn` (poster/안내문/광고) | 9 | Trap + Topic (song song) |
| `câu-giống-đồ-thị` (도표/그래프) | 10 | Trap + Topic (song song) |
| `câu-giống-đoạn-văn-dài` (văn xuôi) | 11~12 | Trap + Topic (song song) |

> Phần **NGHE 듣기** và **VIẾT 쓰기** còn `⏳` (bổ sung taxonomy khi có ngữ liệu).

---

## 3. Cài đặt & mở vault

1. **Obsidian** → `Open folder as vault` → chọn thư mục gốc `xuanvt-learning-vault`.
2. Bật **Dataview** (community plugin, bắt buộc để `98_Views/` hoạt động) + **Properties** (core plugin, xem/sửa frontmatter).
3. **Claude Code**: mở project tại thư mục gốc; Claude tự đọc `CLAUDE.md` + `.claude/domains.yaml`.
4. Cần **`python3`** trên PATH để hook `PreToolUse` chạy (bảo vệ vùng cấm). Kiểm tra: `python3 --version`. Không có → hook không chạy → vùng cấm **không được bảo vệ**.

> Hướng dẫn dùng Obsidian chi tiết (điều hướng, graph, Dataview): [`HUONG_DAN_OBSIDIAN.md`](HUONG_DAN_OBSIDIAN.md).

---

## 4. Vòng lặp làm việc với skill

Skill kích hoạt theo ngữ cảnh — cứ mô tả việc bằng tiếng Việt.

| Bạn nói / làm | Skill | Kết quả |
|---|---|---|
| Đưa ảnh/dán câu hỏi (ngữ pháp, poster/thông báo, đồ thị) · *"phân tích đề này"* · *"backfill đề cũ"* | `topik-exam-analysis` | EXAM note + **diff** cho Grammar/Pair/Group/Distractor/Topic/Trap/Vocab |
| *"tổng hợp ngữ pháp"* · *"compile handbook"* · *"gom vào 1 file"* | `topik-grammar-compile` | `TOPIK/99_Dashboard/GR_Compiled_Handbook.md` |
| *"sync vault"* · *"cập nhật dashboard"* · *"kiểm tra vault"* | `vault-sync` | Render appearances + `Pair_Matrix`, `Distractor_Stats`, `Topic_Stats`, `Trap_Stats`; sinh `99_Global_Dashboard/Review_Today.md` (khi đã có SR) |
| *"hôm nay ôn gì?"* · báo kết quả *"GR_더니: hard, GR_바람에: good"* | `review-scheduler` | Cập nhật `sr-due/interval/ease`, sinh lịch ôn (skill DUY NHẤT sửa field `sr-*`) |
| Thêm/sửa khuôn note trong `00_Templates/` | `template-editor` | Sửa template (skill duy nhất được vào vùng này, gate bằng sentinel + propose-diff) |

**Quy tắc vàng:**
- Skill luôn đưa **bảng diff** (CREATE/APPEND… kèm nguồn `[TOPIK_nn-Qm]` / `[RA:nn-Qm]`) → bạn duyệt / sửa từng dòng → mới ghi. Batch nhiều đề gộp một bảng, duyệt một lần.
- Note mới ghi `status: draft`; **chỉ con người** nâng lên `verified`.
- Grade SR hợp lệ: `again` / `hard` / `good` / `easy` (hoặc *lại / khó / ổn / dễ*).
- Claim chưa có nguồn → `⚠️ Unverified`, không tự coi là đúng.

> **Lưu ý:** hiện **chưa khởi tạo SR** nên `99_Global_Dashboard/Review_Today.md` còn rỗng. Nói *"khởi tạo lịch SR cho grammar"* để bắt đầu.

---

## 5. Vùng cấm (hook `PreToolUse` enforce, mọi domain)

- `*/00_Templates/**` → chỉ con người hoặc skill `template-editor`.
- `*/99_Dashboard/**` và `99_Global_Dashboard/**` → chỉ skill `vault-sync` / `*-compile`.
- Field `sr-*` → chỉ `review-scheduler`.
- Note `status: verified` trong thư mục `immutable_when_verified` (topik: `50_Exams`) → bất biến.
- `.env` → cấm tuyệt đối.

Claude báo bị chặn ở các vùng trên = **đúng thiết kế**, không phải lỗi.

---

## 6. Domain BA (placeholder — kích hoạt khi sẵn sàng)

BA theo **learn-first**: schema phải lộ ra từ ngữ liệu thật (như 6+ đề TOPIK đầu tiên sinh ra template GR/PAIR/GROUP), không thiết kế từ suy đoán.

1. Làm vài buổi phân tích tài liệu BA thật (BABOK, case study) với Claude.
2. Từ ngữ liệu đó: tạo `.claude/rules/ba/frontmatter_schema.md` + `BA/00_Templates/*` + skill `ba-note-builder`.
3. Đổi `status: placeholder → active` cho block `ba` trong [`.claude/domains.yaml`](.claude/domains.yaml). Hook / vault-sync / review-scheduler tự nhận.

Chi tiết loại note dự kiến: [`BA/README_BA.md`](BA/README_BA.md).

---

## 7. Thứ tự đọc để hiểu hệ thống

[`CLAUDE.md`](CLAUDE.md) (nguyên tắc + decision log Q1–Q18) → [`.claude/domains.yaml`](.claude/domains.yaml) → [`.claude/rules/`](.claude/rules/) → [`TOPIK/90_MOC/`](TOPIK/90_MOC/) (taxonomy dạng bài + đáp án) → [`TOPIK/00_Templates/`](TOPIK/00_Templates/) → [`.claude/skills/`](.claude/skills/).

**Link nhanh:** dashboard sống [`98_Views/Bang_Dieu_Khien.md`](98_Views/Bang_Dieu_Khien.md) · hướng dẫn Obsidian [`HUONG_DAN_OBSIDIAN.md`](HUONG_DAN_OBSIDIAN.md) · handbook ôn tổng `TOPIK/99_Dashboard/GR_Compiled_Handbook.md`.
