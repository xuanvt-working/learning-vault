---
name: review-scheduler
description: Cập nhật lịch spaced repetition (sr-due, sr-interval, sr-ease) cho grammar notes của learning-vault (SR hợp nhất mọi domain — quét sr_dirs trong .claude/domains.yaml) theo kết quả ôn tập người dùng nhập. Dùng skill này khi người dùng báo kết quả review ("GR_더니: hard", "hôm nay ôn xong, kết quả: ..."), hỏi "hôm nay ôn gì", hoặc muốn khởi tạo lịch SR cho note mới. Đây là skill DUY NHẤT được phép sửa field sr-* (hook enforce).
---

# Review Scheduler Skill

Khai danh tính trước khi ghi: `mkdir -p .claude/state && echo review-scheduler > .claude/state/active_skill`; xóa file khi xong.

## Input

Kết quả review dạng danh sách, mỗi dòng `{note}: {grade}` với grade ∈ `again | hard | good | easy`. Chấp nhận cách viết thoáng (lại/khó/ổn/dễ) nhưng phải xác nhận lại mapping với người dùng nếu không khớp chính xác enum.

## Thuật toán (SM-2 rút gọn)

Khởi tạo note chưa có SR: `sr-ease: 2.5`, `sr-interval: 0`.

| Grade | interval mới | ease mới |
|---|---|---|
| again | 1 ngày | ease − 0.2 (sàn 1.3) |
| hard | max(1, interval × 1.2) | ease − 0.15 (sàn 1.3) |
| good | interval = 1→3; ngược lại interval × ease | giữ nguyên |
| easy | interval × ease × 1.3 | ease + 0.15 |

`sr-due = hôm nay + interval` (làm tròn ngày). Ghi 3 field, không đụng gì khác trong note.

## Truy vấn "hôm nay ôn gì"

Quét mọi thư mục trong `sr_dirs` của các domain active (manifest) lấy note `sr-due <= hôm nay`, sort sr-due tăng dần; bổ sung mục **radar**: PAIR `confidence: open` (chiều ngược dễ ra ở đề kế) và grammar note `status: draft` lâu chưa verify. Xuất danh sách gọn: pattern | nhóm | lần cuối | link.

## Ràng buộc

- Chỉ sửa `sr-due`, `sr-interval`, `sr-ease`. Không sửa status, không sửa nội dung.
- Note người dùng báo mà không tồn tại → liệt kê ⚠️, không tự tạo.
- Kết thúc: bảng tóm tắt thay đổi (note | grade | due cũ → due mới).
