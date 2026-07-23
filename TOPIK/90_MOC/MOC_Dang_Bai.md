---
type: moc-note
status: draft
source: ["user-provided (ảnh phân loại dạng bài TOPIK II)"]
tags: [korean/topik, moc, ref-dang-bai]
created: 2026-07-12
---

# MOC — Dạng bài TOPIK II

Hub taxonomy **dạng bài** domain topik. File này thay cho field `question_count` / `question_types` từng nằm trong frontmatter exam-note — exam-note không còn lưu dạng bài, chỉ ghi dạng ở heading câu.

**Quy ước dùng slug:** heading mỗi câu trong exam-note viết `## Câu {N} — dạng {slug} ({hậu tố 한국어})` cho **mọi dạng** (cột "Slug" + cột "Hậu tố heading" bên dưới). Hậu tố = cột `한국어 (đề bài)` bỏ đuôi động từ `고르기 / 하기 / 고르십시오`. VD: `## Câu 8 — dạng xác-định-chủ-đề (무엇에 대한 글인지)`.

---

## ĐỌC 읽기 (10 dạng)

| Dạng | Slug | 한국어 (đề bài) | Hậu tố heading (한국어) | Nghĩa | Câu điển hình | Trạng thái |
|---|---|---|---|---|---|---|
| 1 | `ngữ-pháp-chỗ-trống` | 빈칸에 들어갈 맞는 문법 고르기 | 빈칸에 들어갈 맞는 문법 | Chọn ngữ pháp thích hợp điền vào chỗ trống ( ) | ~1–2 | đang dùng |
| 2 | `ngữ-pháp-đồng-nghĩa` | 밑줄 친 부분과 비슷한 표현 고르기 | 밑줄 친 부분과 비슷한 표현 | Chọn cách diễn đạt giống phần gạch chân | ~3–4 | đang dùng |
| 3 | `xác-định-chủ-đề` | 무엇에 대한 글인지 고르기 | 무엇에 대한 글인지 | Xác định bài (quảng cáo/thông báo) nói về chủ đề gì | ~5–8 | đang dùng |
| 4a | `câu-giống-đồ-thị` | 도표의 내용과 같은 것 고르기 | 도표의 내용과 같은 것 | Chọn câu có nội dung giống biểu đồ / số liệu (도표/그래프) | 10 | đang dùng |
| 4b | `câu-giống-đoạn-văn` | 글의 내용과 같은 것 고르기 | 글의 내용과 같은 것 | Chọn câu có nội dung giống đoạn văn / poster (안내문/광고) | 9 | đang dùng |
| 4c | `câu-giống-đoạn-văn-dài` | 글의 내용과 같은 것 고르기 | 글의 내용과 같은 것 | Chọn câu có nội dung giống **đoạn văn dài / văn xuôi** (줄글 nhiều câu) | 11–12, 20 | đang dùng |
| 5 | `sắp-xếp-thứ-tự` | 순서대로 맞게 배열한 것 고르기 | 순서대로 맞게 배열한 것 | Sắp xếp 4 mảnh câu (가~라) theo đúng thứ tự | 13–15 | đang dùng |
| 6 | `điền-nội-dung` | 빈칸에 들어갈 알맞은 내용 고르기 | 빈칸에 들어갈 알맞은 내용 | Chọn nội dung thích hợp điền vào chỗ trống ( ) | 16–18 | đang dùng |
| 7 | `từ-vựng+nội-dung-giống` | 빈칸에 알맞은 어휘 + 내용과 같은 것 고르기 | 빈칸에 알맞은 어휘 + 내용과 같은 것 | Chọn từ vựng điền chỗ trống + chọn câu giống nội dung | — | dự phòng |
| 8 | `thành-ngữ-tục-ngữ+nội-dung-giống` | 빈칸에 알맞은 관용 표현이나 속담 + 내용과 같은 것 고르기 | 빈칸에 알맞은 관용 표현이나 속담 + 내용과 같은 것 | Chọn thành ngữ/tục ngữ điền chỗ trống + chọn câu giống nội dung | — | dự phòng |
| 9 | `tâm-trạng+nội-dung-giống` | 심정 + 내용과 같은 것 고르기 | 심정 + 내용과 같은 것 | Chọn tâm trạng + chọn câu giống nội dung | — | dự phòng |
| 10 | `điền-phó-từ` | ( )에 들어갈 알맞은 것 고르기 | 빈칸에 들어갈 알맞은 부사 | Chọn phó từ liên kết/phó từ câu điền vào chỗ trống ( ) | 19 | đang dùng |

> Dạng 4a/4b/4c cùng đề bài "다음 글 또는 도표의 내용과 같은 것을 고르십시오" nhưng **tách theo chất liệu**: 4a `câu-giống-đồ-thị` (도표/그래프, câu 10), 4b `câu-giống-đoạn-văn` (poster/안내문/광고 ngắn, câu 9), 4c `câu-giống-đoạn-văn-dài` (văn xuôi nhiều câu, câu 11–12). 4b và 4c chung hậu tố `글의 내용과 같은 것` — phân biệt bằng độ dài/chất liệu (poster ngắn ↔ đoạn văn dài).

> Dạng 5 `sắp-xếp-thứ-tự` (câu 13–15, đề bài "다음을 순서대로 맞게 배열한 것을 고르십시오"): 4 phương án là **hoán vị** của 4 mảnh câu (가)(나)(다)(라). Sinh **layer cue `sequence-note`** (`TOPIK/47_Sequence/`, tổ chức theo kỹ thuật nối câu, ngưỡng ≥2× như trap-note) — chi tiết ở [[frontmatter_schema]] §sequence-note; KHÔNG sinh GR/PAIR/GROUP/DIS/TOPIC/TRAP.

> Dạng 6 `điền-nội-dung` (câu 16–18, đề bài "다음을 읽고 (   )에 들어갈 내용으로 가장 알맞은 것을 고르십시오"): chất liệu là **đoạn văn có chỗ trống ( )**, 4 phương án là **mệnh đề/cụm nội dung** (không phải ngữ pháp / danh từ chủ đề / câu khẳng định / hoán vị). Sinh **layer `blank-note`** (`TOPIK/48_Blanks/`, tổ chức theo **quan hệ suy luận chỗ trống**, ngưỡng ≥2× như trap/sequence) — chi tiết ở [[frontmatter_schema]] §blank-note; KHÔNG sinh GR/PAIR/GROUP/DIS/TOPIC/TRAP/SEQ (VC vẫn tạo khi có cụm lexical-hóa). Kích hoạt theo Q20.

> Dạng 7–9 là câu **kép** (2 nhiệm vụ / 1 câu). Slug đã đặt sẵn để đề tương lai dùng ngay; tên có thể tinh chỉnh khi phân tích đề thực tế.

> Dạng 10 `điền-phó-từ` (câu 19, đề bài "( )에 들어갈 알맞은 것을 고르십시오"): chất liệu là **đoạn văn có chỗ trống ( ) dùng CHUNG với câu 20** (câu 20 = dạng 4c `câu-giống-đoạn-văn-dài`); 4 phương án là **phó từ liên kết/phó từ câu** (또한/오히려/아마/특히/물론/게다가/만약… — không phải ngữ pháp / nội dung / danh từ chủ đề / hoán vị). Sinh **layer `adverb-note`** (`TOPIK/49_Adverbs/`, tổ chức theo **chức năng phó từ**, ngưỡng ≥2× như trap/sequence/blank) — chi tiết ở [[frontmatter_schema]] §adverb-note; KHÔNG sinh GR/PAIR/GROUP/DIS/TOPIC/TRAP/SEQ/BLK (VC vẫn tạo khi có cụm lexical-hóa). Câu 19 & 20 chung passage: câu 19 giữ Chú giải đầy đủ, câu 20 trỏ "xem Câu 19". Kích hoạt theo Q21.

---

## NGHE 듣기

⏳ Cung cấp sau — sẽ bổ sung taxonomy dạng bài phần Nghe khi có ảnh phân loại.

---

## VIẾT 쓰기

⏳ Cung cấp sau — sẽ bổ sung taxonomy dạng bài phần Viết khi có ảnh phân loại.

---

## Liên kết
- Đáp án theo số câu: [[MOC_Nguon_Tham_Khao]]
- Áp dụng ở: các exam-note trong `TOPIK/50_Exams/`
