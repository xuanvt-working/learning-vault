---
title: "GROUP: {{Tên nhóm}}"
type: group-note
group_id: GROUP_{{ten_khong_dau}}       # trùng tên file
group_name: "{{Tên nhóm tiếng Việt}}"
members: []                              # ≥3: [GR_아어서, GR_으니까, ...]
pairs_inside: []                         # [PAIR_탓에_바람에]
diff_axes: []                            # [sắc_thái_kết_quả, chủ_ngữ, vế_sau_cấm, ...]
confusion_pairs: []
#  - {a: GR_느라, b: GR_바람에, key: "느라 cần V chủ ý + cùng chủ ngữ"}
source: []
status: draft
tags: [korean/grammar, topik, group]
created: {{date}}
---

# Nhóm: {{Tên nhóm}}

> [!summary] Chức năng chung
> {{1 câu: cả nhóm cùng diễn tả gì; khác nhau ở trục nào}}

## Ma trận khác biệt
<!-- matrix:start -->
| Ngữ pháp | {{trục 1}} | {{trục 2}} | Vế sau cấm | Ràng buộc riêng | Tín hiệu chọn nhanh (3 giây) |
|---|---|---|---|---|---|
| [[GR_...]] | | | | | |
| [[GR_...]] | | | | | |
| [[GR_...]] | | | | | |
<!-- matrix:end -->

Quy tắc điền: mỗi hàng PHẢI trả lời được "khi nào chọn/loại trong 3 giây".
Cột nguồn không cần riêng — tag `[Dnn-Qm]` đặt trong ô nếu claim từ đề.

## Cặp dễ nhầm nhất trong nhóm
| Cặp | Chìa khóa phân biệt | Bằng chứng đề |
|---|---|---|
| {{a}} vs {{b}} | {{key}} | `[Dnn-Qm-dis]` |

## Cặp tương đương bên trong nhóm
{{[[PAIR_...]]}} — xem chi tiết trong pair note (không lặp lại ở đây).

## Câu đối chiếu cùng ngữ cảnh
> Cùng 1 tình huống, đổi lần lượt các pattern — nêu sắc thái mỗi câu:
> {{câu 1}} · {{câu 2}} · {{câu 3}}

## Unverified claims
- {{⚠️ ...}}

## Liên kết
MOC: [[MOC_...]] · Nhóm liên thông: {{[[GROUP_...]]}}
