# Naming Rule

## Pattern theo loại

| Loại | Pattern tên file | Ví dụ |
|---|---|---|
| Grammar | `GR_{pattern}` | `GR_아어야.md`, `GR_더니.md` |
| Pair | `PAIR_{a}_{b}` | `PAIR_탓에_바람에.md` |
| Group | `GROUP_{ten_khong_dau}` | `GROUP_nguyen_nhan.md` |
| Distractor | `DIS_{pattern}` | `DIS_거나.md` |
| Topic | `TOPIC_{category-theme hangul}` | `TOPIC_가전제품.md`, `TOPIC_장소기관.md`, `TOPIC_환경보호.md` |
| Trap | `TRAP_{ten_khong_dau}` | `TRAP_dao_so_sanh.md`, `TRAP_mien_phi_co_phi.md` |
| Exam | `TOPIK_{nn}` | `TOPIK_37.md` (nn = số hiệu kỳ thi thật) |
| Vocab | `VC_{pattern}` | `VC_V고_다니다.md` |
| MOC | `MOC_{ten}` | `MOC_Nhom_Nguyen_nhan.md` |

## Quy tắc chuẩn hóa pattern Hàn trong tên file

1. Giữ Hangul nguyên vẹn; bỏ dấu gạch nối đầu và dấu ngoặc biến thể: `-아/어야` → `아어야`; `-(으)려고` → `으려고`; `-(으)ㄹ 수록` → `을수록`.
2. Khoảng trắng trong pattern → `_`: `-는 바람에` → `는_바람에`; nhưng phần định danh chính có thể rút gọn nếu không gây trùng: `바람에` (ưu tiên ngắn, miễn duy nhất trong vault).
3. Không dấu cách trong tên file; không ký tự `/ \ : * ? " < > |`.
4. PAIR: thứ tự a_b theo **tần suất xuất hiện giảm dần** trong đề; đã đặt rồi thì không đổi (tên file là ID ổn định).
5. GROUP: tiếng Việt không dấu, snake_case: `GROUP_muc_dich`, `GROUP_suy_doan`, `GROUP_nhuong_bo`.
5b. TOPIC: 1 file = 1 **category-theme** (không phải mỗi đáp án một file). Tên file = `TOPIC_{tên category Hangul, bỏ dấu cách}` (`가전제품`, `장소기관`, `환경보호`); field `topic` trong frontmatter trùng tên category. Từ vựng đáp án cùng category liệt kê trong body + field `members`, KHÔNG tách file riêng.
5c. TRAP: 1 file = 1 **kỹ thuật bẫy** (dạng `câu-giống-đoạn-văn` poster câu 9 / `câu-giống-đồ-thị` đồ-thị câu 10, không phải mỗi phương án một file). Tên tiếng Việt không dấu, snake_case: `TRAP_dao_so_sanh`, `TRAP_mien_phi_co_phi`, `TRAP_thay_doi_thu_hang`; field `trap_id` trùng tên file. Chỉ tạo khi bẫy xuất hiện ≥2× (giống DIS).
6. Tên file là ID vĩnh viễn — đổi nghĩa/mở rộng nội dung không đổi tên; cần đổi tên thật sự → cập nhật mọi backlink trong cùng commit.
