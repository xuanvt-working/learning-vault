---
title: "BLK: {{Căn cứ}}"
type: blank-note
blank_id: BLK_{{ten_khong_dau}}      # = tên file
blank_name: "{{tên quan hệ suy luận ngắn gọn}}"
category: {{căn-cứ | nhân-quả | đối-lập | khái-quát | mục-đích | điều-kiện | ví-dụ | so-sánh}}
cue_markers: [{{dấu hiệu liên kết quanh blank — 때문이다/따라서/즉/그러나...}}]   # optional
role_in_para: {{mở-đoạn | giữa-đoạn | kết-đoạn | linh-hoạt}}   # optional — vị trí điển hình của blank
members: [{{biểu hiện ngôn ngữ điển hình}}]   # optional
history: []                          # gộp mọi lần; reason mở đầu bằng "{{đáp án đúng/tín hiệu}}"
#  - {exam: TOPIK_35, q: 16, role: correct,    reason: "여성 스트레스 원인=가사·육아 부담 → blank '집에 있을 때'"}
#  - {exam: TOPIK_60, q: 17, role: distractor, reason: "② chọn mệnh đề nhân-quả trong khi mạch bài là đối-lập"}
correct_count: 0                     # vault-sync tự tính — không điền tay
distractor_count: 0                  # vault-sync tự tính — không điền tay
kill_signal: "{{dấu hiệu 3 giây loại option KHÔNG khớp quan hệ này}}"   # bắt buộc
select_signal: "{{khi option ĐÚNG khớp quan hệ này}}"                    # bắt buộc
source: []
status: draft
tags: [korean/topik, reading/blank]
created: {{date}}
---

# Hồ sơ quan hệ chỗ trống: {{blank_name}}

> [!tip] Kill signal — loại option KHÔNG khớp quan hệ trong 3 giây
> {{...}} ⚠️ Unverified

> [!success] Select signal — khi option khớp quan hệ này (chọn chắc)
> {{...}} ⚠️ Unverified

## Biểu hiện điển hình
- {{cụm/dấu hiệu Hàn quanh chỗ trống báo hiệu quan hệ này; ràng buộc nội dung blank}}

## Lịch sử xuất hiện
<!-- sync:appearances:start -->
(vault-sync render từ history — không sửa tay)
<!-- sync:appearances:end -->

## Liên kết
[[TOPIK_{{nn}}]]
