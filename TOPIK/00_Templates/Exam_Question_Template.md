---
type: exam-note
exam_id: TOPIK_{{nn}}         # = tên file, thay title
date_analyzed: {{date}}
status: draft                # verified → immutable (hook chặn ghi)
tags: [korean/topik, exam]
---

<!-- exam-note KHÔNG lưu title/question_count/question_types/source/created.
     Dạng bài ghi ở heading mỗi câu; danh sách slug đầy đủ tra [[MOC_Dang_Bai]]. -->


# Đề TOPIK_{{nn}}

> **Nguồn đáp án:** [[MOC_Nguon_Tham_Khao]] (tra theo số câu).

## Câu {{m}} — dạng {{ngữ-pháp-chỗ-trống (빈칸에 들어갈 맞는 문법) | ngữ-pháp-đồng-nghĩa (밑줄 친 부분과 비슷한 표현)}}

**문제:**
> {{câu gốc nguyên văn Hangul, giữ ( ) hoặc __gạch chân__}}

**Dịch:**
> {{bản dịch tiếng Việt toàn câu, giữ ( ) hoặc __gạch chân__}}

| # | Phương án | Ngữ pháp | Vai | Lý do / Phân tích |
|---|---|---|---|---|
| ① | {{...}} | [[GR_...]] | ❌ | {{phân tích đúng/sai đầy đủ 2-3 câu; trích dẫn Hàn nếu cần}} |
| ② | {{...}} | [[GR_...]] | ✅ | {{...}} |
| ③ | {{...}} | [[GR_...]] | ❌ | {{...}} |
| ④ | {{...}} | [[GR_...]] | ❌ | {{...}} |

### Chú giải chi tiết

> {{dòng Hàn 1 của 문제}}
→ {{dịch dòng 1}}
- **Ngữ pháp:**
  - {{pattern — giải thích ngắn}} · [[GR_...]]   <!-- link chỉ khi note tồn tại; KHÔNG tạo GR mới / KHÔNG appearances -->
  - {{pattern 2 — giải thích}} · …
  <!-- mỗi ngữ pháp MỘT dòng, liệt kê HẾT, không bỏ sót -->
- **Từ vựng:**
  - {{từ — nghĩa}}
  - {{cụm lexical-hóa — nghĩa}} · [[VC_...]]   <!-- link khi VC note tồn tại -->
  - {{từ thuộc topic category — nghĩa}} · [[TOPIC_...]]   <!-- nếu từ thuộc topic thì link tới TOPIC -->
  <!-- mỗi từ/cụm MỘT dòng, HẾT các từ trong dòng -->

> {{dòng Hàn 2 nếu có}}
→ {{dịch dòng 2}}
- **Ngữ pháp:**
  - {{...}}
- **Từ vựng:**
  - {{...}}

---
(lặp block trên cho từng câu ngữ pháp)

## Câu {{m}} — dạng xác-định-chủ-đề (무엇에 대한 글인지)

**문제:**
> {{toàn văn quảng cáo/thông báo — giữ nguyên xuống dòng}}

**Dịch:**
> {{dịch tiếng Việt song song từng dòng}}

| # | Phương án | Nghĩa | Chủ đề | Vai | Căn cứ / Phân tích |
|---|---|---|---|---|---|
| ① | {{신문}} | {{báo}} | [[TOPIC_{{...}}]] | ✅ | {{từ khóa + phân tích vì sao đúng}} |
| ② | {{...}} | {{...}} | — | ❌ | {{vì sao loại}} |
| ③ | {{...}} | {{...}} | — | ❌ | {{...}} |
| ④ | {{...}} | {{...}} | — | ❌ | {{...}} |

### Chú giải chi tiết

> {{dòng Hàn 1 của quảng cáo/thông báo}}
→ {{dịch dòng 1}}
- **Ngữ pháp:**
  - {{pattern nền — giải thích}} · [[GR_...]]   <!-- link chỉ khi note tồn tại; KHÔNG appearances / KHÔNG tạo GR mới -->
  - …
- **Từ vựng:**
  - {{từ — nghĩa}}
  - {{cụm lexical-hóa — nghĩa}} · [[VC_...]]
  - {{từ thuộc topic category — nghĩa}} · [[TOPIC_...]]

> {{dòng Hàn 2 nếu có}}
→ {{dịch dòng 2}}
- **Ngữ pháp:**
  - {{...}}
- **Từ vựng:**
  - {{...}}

---
(lặp block trên cho từng câu chủ đề)

## Câu {{m}} — dạng {{câu-giống-đoạn-văn (글의 내용과 같은 것) [poster câu 9] | câu-giống-đồ-thị (도표의 내용과 같은 것) [đồ-thị câu 10] | câu-giống-đoạn-văn-dài (글의 내용과 같은 것) [đoạn văn dài câu 11-12]}}

<!-- "다음 글 또는 도표의 내용과 같은 것을 고르십시오" (ĐỌC câu 9~12) — tách 3 slug theo chất liệu:
     poster/안내문 (câu 9) → slug câu-giống-đoạn-văn (글의 내용과 같은 것): 문제 dạng blockquote như dưới.
     đồ thị/그래프 (câu 10) → slug câu-giống-đồ-thị (도표의 내용과 같은 것): thay khối 문제 bằng
     "**문제 (도표):** {{tiêu đề}}" + BẢNG SỐ LIỆU thường (biểu đồ không đặt vừa blockquote), rồi tới **Dịch:**.
     đoạn văn dài/줄글 (câu 11-12, Q16) → slug câu-giống-đoạn-văn-dài (글의 내용과 같은 것): 문제 dạng blockquote nhiều dòng như câu 9.
     Cả ba sinh/append SONG SONG trap-note VÀ topic-note (topic lấy chủ đề từ chất liệu đọc, ngưỡng 1×; câu 11-12 → category 화제, xem Q15/Q16). Cột Căn cứ / Phân tích: phương án ĐÚNG nhận ra qua Vai ✅ (KHÔNG cite [RA:] trong exam — nguồn đáp án ở đầu page); phương án bẫy có note thì link [[TRAP_*]]. -->

**문제:**
> {{toàn văn poster/thông báo — giữ nguyên xuống dòng}}

**Dịch:**
> {{dịch tiếng Việt song song từng dòng}}

**Chủ đề:** {{theme}} → [[TOPIC_{{category-theme}}]]   <!-- mức câu, KHÔNG thêm cột vào bảng; câu 9 → 광고/안내, câu 10 → 화제 -->

| # | Phương án | Nghĩa | Vai | Căn cứ / Phân tích |
|---|---|---|---|---|
| ① | {{câu Hàn}} | {{dịch}} | ❌ | {{đối chiếu poster/đồ thị — phân tích đầy đủ}} — [[TRAP_...]] |
| ② | {{...}} | {{...}} | ✅ | {{khớp dữ kiện}} |
| ③ | {{...}} | {{...}} | ❌ | {{...}} — [[TRAP_...]] |
| ④ | {{...}} | {{...}} | ❌ | {{...}} — [[TRAP_...]] |

### Chú giải chi tiết

> {{dòng Hàn 1 của đoạn văn / nhãn+số liệu đồ thị}}
→ {{dịch dòng 1}}
- **Ngữ pháp:**
  - {{pattern nền — giải thích}} · [[GR_...]]   <!-- link chỉ khi note tồn tại; KHÔNG appearances / KHÔNG tạo GR mới -->
  - …
- **Từ vựng:**
  - {{từ — nghĩa}}
  - {{cụm lexical-hóa — nghĩa}} · [[VC_...]]
  - {{từ thuộc topic category — nghĩa}} · [[TOPIC_...]]

> {{dòng Hàn 2 nếu có}}
→ {{dịch dòng 2}}
- **Ngữ pháp:**
  - {{...}}
- **Từ vựng:**
  - {{...}}

---
(lặp block trên cho câu 9 poster, câu 10 đồ thị & câu 11-12 đoạn văn dài)

## Câu {{m}} — dạng sắp-xếp-thứ-tự (순서대로 맞게 배열한 것)

<!-- "다음을 순서대로 맞게 배열한 것을 고르십시오" (ĐỌC câu 13~15) — 4 mảnh câu (가)(나)(다)(라),
     4 phương án là HOÁN VỊ thứ tự. Sinh MỘT layer sequence-note (theo kỹ thuật nối câu, ngưỡng ≥2×);
     KHÔNG sinh GR/PAIR/GROUP/DIS/TOPIC/TRAP (VC vẫn tạo khi có cụm lexical-hóa).
     Đáp án đúng nhận ra qua Vai ✅ (KHÔNG cite [RA:] trong exam). Cue có note → link [[SEQ_*]] cột Căn cứ; cue 1× mô tả inline. -->

**문제:**
> (가) {{mảnh 가 nguyên văn Hangul}}
> (나) {{mảnh 나}}
> (다) {{mảnh 다}}
> (라) {{mảnh 라}}

**Dịch:**
> (가) {{dịch mảnh 가}}
> (나) {{dịch mảnh 나}}
> (다) {{dịch mảnh 다}}
> (라) {{dịch mảnh 라}}

**Trình tự đúng:** ({{X}})→({{Y}})→({{Z}})→({{W}})

| # | Thứ tự | Vai | Căn cứ / Phân tích |
|---|---|---|---|
| ① | ({{다}})-({{나}})-({{라}})-({{가}}) | ✅ | {{chuỗi móc nối: mảnh mở đầu + cue nối từng bước}} — [[SEQ_...]] |
| ② | {{...}} | ❌ | {{vi phạm cue nào — vd đặt mảnh chứa 지시어 lên đầu}} — [[SEQ_...]] |
| ③ | {{...}} | ❌ | {{...}} |
| ④ | {{...}} | ❌ | {{...}} |

### Chú giải chi tiết

> (가) {{mảnh 가 Hangul}}
→ {{dịch mảnh 가}}
- **Ngữ pháp:**
  - {{pattern nền — giải thích}} · [[GR_...]]   <!-- link chỉ khi note tồn tại; KHÔNG appearances / KHÔNG tạo GR mới -->
- **Từ vựng:**
  - {{từ — nghĩa}}
  - {{cụm lexical-hóa — nghĩa}} · [[VC_...]]

<!-- lặp > (나)/(다)/(라) như trên, mỗi mảnh: dòng Hàn → dịch → Ngữ pháp / Từ vựng -->

---
(lặp block trên cho từng câu sắp-xếp-thứ-tự, câu 13~15)
