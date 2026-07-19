---
title: "TRAP: {{Đảo chiều so sánh}}"
type: trap-note
trap_id: TRAP_{{ten_khong_dau}}      # = tên file
trap_name: "{{tên bẫy ngắn gọn}}"
scope: {{poster | đồ-thị | cả-hai}}   # poster = câu 9 (안내문/광고) | đồ-thị = câu 10 (도표/그래프)
category: {{phạm-vi | thời-hạn | miễn-phí | phương-thức | so-sánh | cực-trị | xu-hướng | bằng-nhau | ngưỡng | thứ-hạng}}
members: [{{biểu hiện ngôn ngữ điển hình}}]   # optional — cụm từ Hàn hay dựng bẫy này
history: []                          # gộp mọi lần, cả 2 vai; reason mở đầu bằng "{{①/kỳ}} ..."
#  - {exam: TOPIK_36, q: 10, role: distractor, reason: "③ 자기 자신 남<여 (thực 남25.1>여18.7)"}
#  - {exam: TOPIK_37, q: 9,  role: correct,    reason: "③ 전화 신청 (đúng — trùng chiêu nhưng khớp poster)"}
distractor_count: 0                  # vault-sync tự tính — không điền tay
correct_count: 0                     # vault-sync tự tính — không điền tay
kill_signal: "{{dấu hiệu 3 giây nhận ra phương án là bẫy}}"   # bắt buộc
select_signal: "{{khi phương án dùng chiêu này lại ĐÚNG — đừng loại nhầm}}"   # bắt buộc
source: []
status: draft
tags: [korean/topik, reading/trap]
created: {{date}}
---

# Hồ sơ bẫy đọc: {{trap_name}}

> [!tip] Kill signal — nhận ra bẫy trong 3 giây
> {{...}} ⚠️ Unverified

> [!success] Select signal — khi chiêu này lại ĐÚNG (đừng loại nhầm)
> {{...}} ⚠️ Unverified

## Biểu hiện điển hình
- {{cụm từ Hàn hay dùng để dựng bẫy này; đối chiếu với dữ kiện poster/đồ thị}}

## Lịch sử xuất hiện
<!-- sync:appearances:start -->
(vault-sync render từ history — không sửa tay)
<!-- sync:appearances:end -->

## Liên kết
[[TOPIK_{{nn}}]]
