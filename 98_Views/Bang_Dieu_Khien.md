---
title: "Bảng điều khiển (Dataview sống)"
tags: [dashboard, view]
---

# Bảng điều khiển — Dataview sống 🔴

> [!info] View này khác dashboard render
> Đây là **view do người viết tay** bằng Dataview — Obsidian **tự tính lại mỗi lần mở note**, không cần chạy skill.
> Thư mục `98_Views/` **không** nằm trong `note_dirs` của `.claude/domains.yaml` ⇒ vault-sync/hook bỏ qua ⇒ bạn (và Claude) sửa tự do.
> Ngược lại, `TOPIK/99_Dashboard/*` là **render tĩnh** do skill sinh — không sửa tay.
>
> Cần bật community plugin **Dataview** thì các bảng dưới mới hiện. Nếu một bảng báo lỗi field, xem ghi chú cú pháp ở cuối.

---

## 1. Tiến độ verify (draft → verified)
Đếm grammar note theo `status`. Mục tiêu: kéo dần từ `draft` sang `verified`.

```dataview
TABLE length(rows) AS "Số note"
FROM "TOPIK/10_Grammar"
GROUP BY status
```

## 2. Radar nhiễu — grammar bị làm bẫy nhiều nhất ⭐
Sắp theo số lần xuất hiện với vai **distractor** (nhiễu). Đây là các mẫu "bẫy" tần suất cao — ưu tiên ôn.

```dataview
TABLE role_ratio AS "C/D",
      length(filter(appearances, (a) => a.role = "distractor")) AS "Số lần nhiễu",
      group AS "Nhóm"
FROM "TOPIK/10_Grammar"
WHERE length(appearances) > 0
SORT length(filter(appearances, (a) => a.role = "distractor")) DESC
LIMIT 15
```

## 3. SR đến hạn hôm nay 📅
Rỗng cho tới khi bạn chạy **review-scheduler** để khởi tạo lịch (field `sr-*` hiện đang trống).

```dataview
TABLE row["sr-due"] AS "Đến hạn", row["sr-interval"] AS "Khoảng (ngày)", row["sr-ease"] AS "Ease"
FROM "TOPIK/10_Grammar"
WHERE row["sr-due"] AND row["sr-due"] <= date(today)
SORT row["sr-due"] ASC
```

## 4. Pair chưa khép (open) — cần thi thêm chiều 🔓
Cặp `open` = mới thi 1 chiều; cần bằng chứng chiều ngược lại để nâng `closed`.

```dataview
TABLE members AS "Thành viên", confidence AS "Độ chắc", morph_note AS "Ghi chú hình thái"
FROM "TOPIK/20_Pairs"
WHERE confidence = "open"
```

## 5. Nhóm & số thành viên 🗂️
Nhóm là **hub** trong Graph View. Nhóm ít thành viên có thể còn thiếu ngữ pháp cùng loại.

```dataview
TABLE group_name AS "Tên nhóm", length(members) AS "Số thành viên"
FROM "TOPIK/25_Groups"
SORT length(members) DESC
```

## 6. Soát chất lượng nhanh — grammar thiếu nhóm / thiếu appearances ⚠️
Note lọt vào đây là ứng viên cần bổ sung (chưa gắn `group` hoặc chưa có lần xuất hiện nào trong đề).

```dataview
LIST
FROM "TOPIK/10_Grammar"
WHERE !group OR length(appearances) = 0
```

## 7. Distractor có tỉ lệ nhiễu cao (từ note DIS) 🎯
Xếp theo `distractor_count` — bẫy càng lặp càng đáng thuộc `kill_signal`.

```dataview
TABLE distractor_count AS "Số lần nhiễu", correct_count AS "Số lần đúng", kill_signal AS "Loại ngay khi…"
FROM "TOPIK/30_Distractors"
SORT distractor_count DESC
LIMIT 15
```

---

> [!note] Ghi chú cú pháp Dataview (để tự sửa/thêm query)
> - **Field có gạch nối** (`sr-due`, `sr-interval`, `sr-ease`) phải viết `row["sr-due"]`. Viết `sr-due` trần, Dataview hiểu là phép trừ `sr - due` → sai.
> - **`appearances` là danh sách object** `{exam, q, role}` → đếm theo vai bằng `length(filter(appearances, (a) => a.role = "distractor"))`.
> - Đổi `"distractor"` thành `"correct"` để đếm số lần làm đáp án đúng.
> - Thêm bảng mới: copy một block, đổi `FROM "TOPIK/…"` sang thư mục khác (`40_Vocab`, `50_Exams`…).
