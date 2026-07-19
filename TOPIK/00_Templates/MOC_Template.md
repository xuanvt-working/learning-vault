---
title: "MOC: {{Tên}}"
type: moc-note
source: []
status: draft
tags: [korean/moc]
created: {{date}}
---

# MOC: {{Tên}}

{{1-2 câu phạm vi của MOC này}}

## Nhóm thuộc phạm vi
- [[GROUP_...]] — {{n}} thành viên

## Ngữ pháp trong phạm vi (Dataview)
```dataview
TABLE pattern, group, role_ratio, status
FROM "10_Grammar"
WHERE group = "GROUP_{{...}}"
SORT file.name ASC
```

## Cặp quy đổi chưa khép chiều (radar)
```dataview
TABLE members, morph_note, confidence
FROM "20_Pairs"
WHERE group = "GROUP_{{...}}" AND confidence = "open"
```

## Đến hạn ôn
```dataview
TABLE pattern, sr-due
FROM "10_Grammar"
WHERE group = "GROUP_{{...}}" AND sr-due <= date(today)
SORT sr-due ASC
```
