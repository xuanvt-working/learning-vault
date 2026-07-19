---
name: template-editor
description: Tạo hoặc sửa file template trong `*/00_Templates/` của learning-vault (mọi domain) — vùng hook chặn với mọi identity khác. Dùng skill này khi người dùng muốn thêm/sửa khuôn note (thêm block dạng bài mới, thêm template loại note mới, dọn placeholder cho khớp naming_rule), hoặc khi một skill khác cần cập nhật template làm bước phụ. KHÔNG dùng để sửa note nội dung (dùng skill sinh note tương ứng) hay dashboard (dùng vault-sync).
---

# Template Editor Skill

Skill DUY NHẤT (ngoài con người) được phép ghi `*/00_Templates/**`. Hook cho qua khi sentinel `active_skill=template-editor`. Vì template là **hợp đồng schema của cả vault**, mọi thay đổi phải minh bạch và người duyệt trước.

## Trước khi chạy

1. Đọc `.claude/rules/{domain}/frontmatter_schema.md` + `.claude/rules/_shared/naming_rule.md` — template PHẢI khớp schema loại note.
2. Đọc template hiện tại (nếu sửa) để giữ đúng phần không đụng tới.

## Quy trình

1. **Propose diff ⛔ DỪNG BẮT BUỘC** — trình đúng nội dung sẽ thêm/đổi (block mới, field mới, placeholder sửa), nêu rõ file. Chờ người duyệt rõ ràng. Không ghi trước bước này.
2. **Khai danh tính**: `mkdir -p .claude/state && echo template-editor > .claude/state/active_skill`.
3. **Ghi** file template theo diff đã duyệt.
4. **Xóa sentinel**: `rm -f .claude/state/active_skill`.
5. **Báo cáo** + nhắc: nếu đổi schema/enum của template, chạy `vault-sync` để five-check không báo lỗi; nếu template dùng cho note đã tồn tại, các note cũ KHÔNG tự đổi theo (chỉ ảnh hưởng note tạo mới).

## Lưu ý

- Chỉ đổi **FORM** (khuôn); không nhét nội dung thật/ví dụ trích đề vào template — placeholder `{{...}}` là chuẩn.
- Template mới cho loại note mới: phải kèm khối schema tương ứng trong `frontmatter_schema.md` (sửa file rule NGOÀI phạm vi skill này — làm ở bước riêng, không bị hook chặn).
- Đổi khuôn là quyết định kiến trúc hiếm — mặc định ưu tiên con người tự sửa; skill này chỉ để tự động hóa có kiểm soát.
