---
title: "Hướng dẫn dùng vault trên Obsidian"
tags: [huongdan, moc]
---

# 🧭 Hướng dẫn dùng vault trên Obsidian

> Vault này chạy trên **hai công cụ song song**:
> - **Obsidian** = nơi bạn **đọc, điều hướng, ôn tập** (mắt người).
> - **Claude Code** = nơi **sinh & sửa nội dung** bằng skill (theo ngữ cảnh câu tiếng Việt bạn nói, không phải lệnh gạch chéo).
>
> File này là bản dùng chi tiết cho Obsidian. Phần cài đặt gốc xem thêm [[README]].

---

## A. Cài & mở (một lần)

1. **Mở vault**: Obsidian → `Open folder as vault` → chọn thư mục gốc `xuanvt-learning-vault`.
2. **Bật Dataview** (community plugin — bắt buộc để `98_Views/` hoạt động): `Settings → Community plugins → Browse → Dataview → Install → Enable`. (Đã cài sẵn trong vault này, chỉ cần chắc chắn nó **Enabled**.)
3. **Bật Properties** (core plugin — để xem/sửa frontmatter dạng bảng): `Settings → Core plugins → Properties view`.
4. **Kiểm `python3`** (cho hook bảo vệ vùng cấm khi dùng Claude Code): chạy `python3 --version` trong terminal. Không có → hook không chạy → vùng cấm **không được bảo vệ**.

---

## B. Bản đồ thư mục

| Thư mục | Vai trò | Sửa tay? |
|---|---|---|
| `TOPIK/10_Grammar` | **Canonical** — mỗi ngữ pháp 1 note (nội dung sống ở đây) | ✅ qua Claude/tay |
| `TOPIK/20_Pairs` | Cặp dễ nhầm (quy đổi 2 chiều) | ✅ |
| `TOPIK/25_Groups` | **Nhóm** — hub gom ngữ pháp cùng loại (ma trận khác biệt) | ✅ |
| `TOPIK/30_Distractors` | Hồ sơ "bẫy" nhiễu (kill/select signal) | ✅ |
| `TOPIK/40_Vocab` | Từ vựng / mẫu đi kèm | ✅ |
| `TOPIK/50_Exams` | Đề đã phân tích — **immutable khi `status: verified`** | ⚠️ khóa khi verified |
| `TOPIK/90_MOC` | Map of Content (mục lục điều hướng) | ✅ |
| `TOPIK/00_Templates` | Khuôn note | 🔒 **chỉ người** (hook chặn Claude) |
| `TOPIK/99_Dashboard` | **Render tĩnh** do skill sinh (Pair_Matrix, Distractor_Stats, Handbook) | 🔒 **không sửa tay** (hook chặn) |
| `98_Views` | **Dataview sống** — do người viết tay, Obsidian tự tính lại | ✅ tự do |
| `99_Global_Dashboard` | SR hợp nhất mọi domain (Review_Today) | 🔒 chỉ skill |
| `BA/` | Domain Business Analyst — **placeholder** (chưa kích hoạt) | — |

> **Render vs View** — điểm dễ nhầm:
> - `99_Dashboard/*` = **render**: ảnh chụp tĩnh, chỉ đổi khi chạy lại skill. Muốn đổi nội dung → sửa note nguồn trong `10_Grammar/` rồi chạy lại skill.
> - `98_Views/*` = **Dataview**: truy vấn sống, tự cập nhật mỗi lần mở. Không cần chạy skill.

---

## C. Điều hướng trong Obsidian (thao tác hằng ngày)

- **Quick Switcher** `Ctrl+O`: gõ tên note nhảy nhanh (vd `GR_더니`, `GROUP_nguyen_nhan`).
- **Backlinks / Outgoing links** (panel phải): xem note nào trỏ tới note hiện tại và ngược lại — dò quan hệ ngữ pháp.
- **Graph View** (biểu tượng đồ thị): **nhóm (`GROUP_*`) là hub** — mỗi grammar note link tới `[[GROUP_...]]`, nên đồ thị tụm thành các cụm theo loại nghĩa. Dùng để thấy ngữ pháp "cô đơn" (chưa gắn nhóm) hay cụm dày đặc cần phân biệt kỹ.
- **Local Graph** (trong 1 note): chỉ hiện hàng xóm trực tiếp — tốt để ôn một cụm dễ nhầm.
- **Tìm theo tag**: search `tag:#korean/grammar` hoặc `tag:#topik`.
- **Lọc theo Properties**: bật cột `status`, `group`, `role_ratio` để quét nhanh trạng thái.

---

## D. Đọc dashboard render (`TOPIK/99_Dashboard/`)

Ba file tổng hợp, **chỉ đọc**:

- **`GR_Compiled_Handbook.md`** — tài liệu ôn tổng 7 section (index nhóm, bảng quy đổi 2 chiều, ma trận khác biệt, bảng nhiễu, từ điển rút gọn, traceability, radar ôn). Dùng trước kỳ thi.
- **`Pair_Matrix.md`** — radar mọi cặp dễ nhầm, cặp `open` (mới thi 1 chiều) xếp trước.
- **`Distractor_Stats.md`** — hồ sơ nhiễu, xếp theo tần suất làm bẫy.

Muốn số liệu đổi → sửa note nguồn rồi bảo Claude *"sync vault"* / *"compile handbook"*. **Đừng sửa trực tiếp** — hook chặn và lần sync sau sẽ ghi đè.

---

## E. Dùng Dataview views (`98_Views/Bang_Dieu_Khien.md`)

Mở [[Bang_Dieu_Khien]] — 7 bảng tự cập nhật:

1. **Tiến độ verify** — bao nhiêu note còn `draft` vs `verified`.
2. **Radar nhiễu** ⭐ — grammar bị làm bẫy nhiều nhất (ưu tiên ôn).
3. **SR đến hạn hôm nay** — rỗng cho tới khi khởi tạo SR.
4. **Pair chưa khép (open)** — cặp cần thi thêm chiều.
5. **Nhóm & số thành viên**.
6. **Soát chất lượng** — grammar thiếu nhóm/thiếu appearances.
7. **Distractor tần suất cao**.

Đây là vùng tự do: thêm/sửa query thoải mái (cuối file có ghi chú cú pháp).

---

## F. Vòng lặp làm việc với Claude Code

Skill **kích hoạt theo ngữ cảnh câu bạn nói** (tiếng Việt) — không cần nhớ lệnh:

| Bạn nói / làm | Skill chạy | Kết quả |
|---|---|---|
| Đưa ảnh đề / dán câu hỏi / *"phân tích đề này"* / *"backfill đề cũ"* | `topik-exam-analysis` | EXAM note + diff cho Grammar/Pair/Group/Distractor |
| *"tổng hợp ngữ pháp"* / *"compile handbook"* / *"gom vào 1 file"* | `topik-grammar-compile` | `99_Dashboard/GR_Compiled_Handbook.md` |
| *"sync vault"* / *"cập nhật dashboard"* / *"kiểm tra vault"* | `vault-sync` | Render lại bảng "Lịch sử xuất hiện", Pair_Matrix, Distractor_Stats, Review_Today |
| *"hôm nay ôn gì?"* / báo kết quả *"GR_더니: hard, GR_바람에: good"* | `review-scheduler` | Cập nhật `sr-due/interval/ease`, sinh lịch ôn |

**Quy tắc vàng:**
- Skill luôn đưa **bảng diff** (CREATE/APPEND… kèm nguồn `[Dnn-Qm]`) → **bạn duyệt / sửa từng dòng** → mới ghi.
- Batch đầu ghi `status: draft`; **chỉ con người** nâng lên `verified`.
- Grade SR hợp lệ: `again` / `hard` / `good` / `easy` (hoặc *lại / khó / ổn / dễ*).
- Claim chưa có nguồn → gắn `⚠️ Unverified`, không tự coi là đúng.

---

## G. Khai thác thêm (roadmap)

| # | Việc | Cách làm | Cần chạy skill? |
|---|---|---|---|
| 1 | **Bắt đầu lịch ôn (SR)** | Nói *"khởi tạo lịch SR cho grammar"* hoặc *"hôm nay ôn gì"* rồi báo kết quả | ✅ review-scheduler |
| 2 | **Nâng draft → verified** | Rà claim `⚠️ Unverified`, đối chiếu giáo trình/đề; con người xác nhận rồi hạ marker + gắn nguồn `[XV]`+ngày | ✅ tay (con người nâng status) |
| 3 | **Kích hoạt domain BA** | Làm vài buổi phân tích tài liệu BA thật → tạo `.claude/rules/ba/frontmatter_schema.md` + `BA/00_Templates/*` + skill `ba-note-builder` → đổi `status: placeholder→active` trong `.claude/domains.yaml` | ✅ (learn-first) |
| 4 | **Tự viết Dataview mới** | Copy 1 block trong [[Bang_Dieu_Khien]], đổi `FROM "TOPIK/…"` sang thư mục khác | ❌ tự làm |
| 5 | **Sơ đồ nhóm bằng Canvas** | `Ctrl+P → Create new canvas`, kéo các `GROUP_*`/`GR_*` vào vẽ mối quan hệ trực quan | ❌ tự làm |
| 6 | **Ôn tổng trước thi** | Mở `GR_Compiled_Handbook.md`; nếu cũ, nói *"compile handbook"* để làm mới | ✅ topik-grammar-compile |

---

## H. Vùng cấm (hook tự enforce — nhớ để khỏi thắc mắc khi Claude "không ghi được")

- `*/00_Templates/**` → chỉ người.
- `*/99_Dashboard/**`, `99_Global_Dashboard/**` → chỉ skill (vault-sync/compile).
- Field `sr-*` → chỉ review-scheduler.
- Note trong `50_Exams` khi `status: verified` → immutable.
- `.env` → cấm tuyệt đối.

Nếu Claude báo bị chặn ở các vùng trên → **đúng như thiết kế**, không phải lỗi.

---

## Liên kết nhanh
- Dashboard sống: [[Bang_Dieu_Khien]]
- Tài liệu ôn tổng: `TOPIK/99_Dashboard/GR_Compiled_Handbook.md`
- Radar cặp: `TOPIK/99_Dashboard/Pair_Matrix.md` · Nhiễu: `TOPIK/99_Dashboard/Distractor_Stats.md`
- Cấu hình định tuyến: `.claude/domains.yaml` · Luật: `CLAUDE.md`
