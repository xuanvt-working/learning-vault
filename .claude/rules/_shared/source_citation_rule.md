# Source Citation Rule

Mọi claim ngữ pháp (nghĩa, ràng buộc, ví dụ, quy đổi) phải truy được nguồn. Không có nguồn → không được coi là authoritative.

## Định dạng tag

| Tag | Nguồn | Ví dụ dùng |
|---|---|---|
| `[TOPIK_nn-Qm]` | Đề đã phân tích, kỳ TOPIK nn câu m | `[TOPIK_47-Q3]` — 탓에 ≈ 바람에 |
| `[TOPIK_nn-Qm-dis]` | Bằng chứng từ vai nhiễu | `[TOPIK_60-Q3-dis]` — 탓에 thiếu nghĩa lặp |
| `[KGU-n]` | Giáo trình KGU quyển n | |
| `[TP_GR]` | Tài liệu TP_GR | |
| `[GR_CTT]` | Nguồn GR_CTT | |
| `[SR5:stt]` | Row trong SR_5_GR_Summary (sau import) | `[SR5:117]` |
| `[RA:nn-Qm]` | Đáp án đọc trong `MOC_Nguon_Tham_Khao.md`, kì nn câu m | `[RA:35-Q5]` — câu 5 kì 35 đáp án ① |

## Quy tắc áp dụng

1. Tag đặt cuối claim hoặc cuối hàng bảng. Một claim nhiều nguồn → liệt kê cả: `[TOPIK_37-Q1][TOPIK_52-Q1]`.
2. Nội dung Claude suy luận/mở rộng mà chưa có nguồn (ví dụ tự tạo, ràng buộc nhớ từ training) → gắn `⚠️ Unverified` ngay tại chỗ VÀ liệt kê tập trung trong section "Unverified claims" cuối note.
3. Con người xác nhận → xóa marker, thêm tag nguồn hoặc tag `[XV]` (Xuân Vũ đã duyệt) + ngày.
4. Note chỉ được nâng `status: verified` khi không còn `⚠️ Unverified`.
5. Ví dụ minh họa tự đặt được phép tồn tại ở status draft, nhưng phải đánh dấu `(vd tự tạo)` để phân biệt với ví dụ trích đề.
