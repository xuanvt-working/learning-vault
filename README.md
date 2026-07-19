# Learning Vault — Khởi động (multi-domain)

Một vault, nhiều domain học tập. Định tuyến: `.claude/domains.yaml`.
- `TOPIK/` — active, sẵn sàng backfill
- `BA/` — placeholder (learn-first: kích hoạt sau khi có ngữ liệu thật)

> Các skill kích hoạt theo ngữ cảnh câu bạn nói (không phải lệnh gạch chéo). Cứ mô tả việc bằng tiếng Việt; các ví dụ dưới nêu rõ tên skill để bạn biết cái gì đang chạy.

## Bước 1: Mở vault
Mở folder này bằng Obsidian và Claude Code (cùng thư mục gốc).

**Setting Obsidian:**
- Core plugin **Properties** (xem frontmatter) — đã bật sẵn.
- Cài + bật community plugin **Dataview**: `Settings → Community plugins → Browse → Dataview`. (Đây là community plugin, không có sẵn — phải cài.)

**Setting Claude Code:**
- Mở project tại thư mục gốc; Claude tự đọc `CLAUDE.md` + `.claude/domains.yaml`.
- Cần **`python3`** trên PATH để hook `PreToolUse` chạy được. Kiểm tra: `python3 --version`. Không có python3 → hook không chạy → vùng cấm không được bảo vệ.

## Bước 2: Kiểm tra hook
Thử yêu cầu Claude Code sửa 1 file trong `TOPIK/00_Templates/` → phải bị chặn.

**Ví dụ:**
> "Sửa file `TOPIK/00_Templates/GR_Analysis_Template.md`, thêm một dòng bất kỳ."

Kết quả đúng: hook chặn Write/Edit, Claude báo không ghi được. Nếu **không** bị chặn → kiểm lại `python3` và `.claude/settings.json` (hook `PreToolUse` khớp `Write|Edit|MultiEdit`).

## Bước 3: Backfill / phân tích đề (skill `topik-exam-analysis`)
**Ví dụ backfill hàng loạt:**
> "Chạy `topik-exam-analysis` backfill từ `TOPIK/BACKFILL_SEED.md`, batch-confirm một lần."

**Ví dụ một đề / câu lẻ:**
> "Phân tích đề này giúp tôi." (kèm ảnh hoặc dán text câu hỏi)

Skill đưa **bảng diff** liệt kê mọi thao tác (CREATE/APPEND…) kèm nguồn `[Dnn-Qm]` trước → bạn duyệt (sửa được từng dòng) → skill mới ghi, batch đầu `status: draft` → Phase cuối tự chạy `vault-sync`.

## Bước 4: Compile + SR
**Compile handbook (skill `topik-grammar-compile`):**
> "Chạy `topik-grammar-compile`."

→ Output duy nhất `TOPIK/99_Dashboard/GR_Compiled_Handbook.md`. Là render — muốn đổi nội dung thì sửa note nguồn trong `10_Grammar/` rồi chạy lại.

**Sync tay khi số liệu bảng lệch (skill `vault-sync`):**
> "Sync vault." / "Cập nhật dashboard."

**Ôn tập (skill `review-scheduler`):**
> "Hôm nay ôn gì?" → đọc `99_Global_Dashboard/Review_Today.md` (SR hợp nhất, sinh sau khi sync).

Báo kết quả ôn để cập nhật lịch (đây là skill DUY NHẤT sửa được field `sr-*`):
> "GR_더니: hard, GR_바람에: good, GR_탓에: easy"

Grade hợp lệ: `again` / `hard` / `good` / `easy` (hoặc lại / khó / ổn / dễ).

## Kích hoạt domain BA (khi sẵn sàng)
1. Làm vài buổi phân tích tài liệu BA thật với Claude (như đã làm 6 đề TOPIK).
2. Từ ngữ liệu đó: tạo `.claude/rules/ba/frontmatter_schema.md` + `BA/00_Templates/*` + skill `ba-note-builder`.
3. Đổi `status: placeholder → active` trong `.claude/domains.yaml`. Hook/sync/scheduler tự nhận.

## Thứ tự đọc để hiểu hệ thống
CLAUDE.md → .claude/domains.yaml → .claude/rules/ → TOPIK/00_Templates/ → .claude/skills/
