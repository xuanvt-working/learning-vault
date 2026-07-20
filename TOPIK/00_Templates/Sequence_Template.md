---
title: "SEQ: {{Hồi chiếu}}"
type: sequence-note
cue_id: SEQ_{{ten_khong_dau}}       # = tên file
cue_name: "{{tên kỹ thuật nối câu ngắn gọn}}"
category: {{mở-đầu | hồi-chiếu | kết-quả | đối-lập | bổ-sung | thời-gian | điều-kiện}}
role_in_order: {{mở-đầu | giữa | kết | linh-hoạt}}   # vị trí điển hình
members: [{{biểu hiện ngôn ngữ điển hình}}]   # optional — cụm Hàn báo hiệu cue này
history: []                          # gộp mọi lần; reason mở đầu bằng "({{mảnh}}) ..."
#  - {exam: TOPIK_35, q: 13, role: correct,    reason: "(나) 그중 하나 → phải sau (다) 여러 가지"}
#  - {exam: TOPIK_60, q: 13, role: distractor, reason: "③ đặt (나) 이런 lên đầu — vi phạm hồi chiếu"}
correct_count: 0                     # vault-sync tự tính — không điền tay
distractor_count: 0                  # vault-sync tự tính — không điền tay
kill_signal: "{{câu chứa cue này KHÔNG thể đứng đầu — nhận ra 3 giây}}"   # bắt buộc
select_signal: "{{khi cue này định vị chắc chắn (mở đầu / móc nối)}}"     # bắt buộc
source: []
status: draft
tags: [korean/topik, reading/sequence]
created: {{date}}
---

# Hồ sơ cue sắp xếp: {{cue_name}}

> [!tip] Kill signal — loại vị trí sai trong 3 giây
> {{...}} ⚠️ Unverified

> [!success] Select signal — khi cue này định vị chắc chắn
> {{...}} ⚠️ Unverified

## Biểu hiện điển hình
- {{cụm từ Hàn báo hiệu cue này; ràng buộc vị trí trong chuỗi}}

## Lịch sử xuất hiện
<!-- sync:appearances:start -->
(vault-sync render từ history — không sửa tay)
<!-- sync:appearances:end -->

## Liên kết
[[TOPIK_{{nn}}]]
