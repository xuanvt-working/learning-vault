# Domain BA — placeholder (learn-first)

Khung thư mục đã dựng; **templates / schema / skill CHƯA viết** — chủ đích.
Schema phải lộ ra từ ngữ liệu thật (BABOK, case study, buổi phân tích với Claude),
không thiết kế từ suy đoán.

## Loại note dự kiến (khớp `note_dirs` trong `.claude/domains.yaml`)

| Thư mục | Loại note | Ghi chú |
|---|---|---|
| `10_Knowledge_Areas` | `KA_*` | BABOK knowledge areas |
| `20_Techniques` | `TQ_*` | elicitation, use case, BPMN… — **tham gia SR** |
| `30_Terms` | `TERM_*` | thuật ngữ (giữ tiếng Anh) — **tham gia SR** |
| `40_Cases` | `CASE_*` | case study, bài tập tình huống |

`sr_dirs` của domain BA = `[BA/20_Techniques, BA/30_Terms]` (chỉ TQ_* và TERM_* vào SR queue hợp nhất).

## Kích hoạt

Khi đủ ngữ liệu: tạo `.claude/rules/ba/frontmatter_schema.md` + `BA/00_Templates/*` + skill `ba-note-builder`,
rồi đổi `status: placeholder → active` cho block `ba` trong `.claude/domains.yaml`.
Xem mục **"Domain BA (placeholder)"** trong [`../README.md`](../README.md) gốc.
