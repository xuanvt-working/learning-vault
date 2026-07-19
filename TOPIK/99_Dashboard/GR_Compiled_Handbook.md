> RENDER tự sinh bởi topik-grammar-compile 2026-07-20 — KHÔNG sửa tay.
> Muốn đổi nội dung → sửa atomic note nguồn (10_Grammar / 20_Pairs / 25_Groups / 30_Distractors / 50_Exams) rồi chạy lại skill.

# 📘 Sổ tay Ngữ pháp TOPIK — Handbook tổng hợp

Tài liệu tra cứu hợp nhất, tái sinh hoàn toàn từ note nguyên tử. 5 section: [§0 Metadata](#0-metadata) · [§1 Ma trận khác biệt theo nhóm](#1-ma-trận-khác-biệt-theo-nhóm) · [§2 Bảng quy đổi hai chiều](#2-bảng-quy-đổi-hai-chiều-pair) · [§3 Bảng nhiễu](#3-bảng-nhiễu-distractor) · [§4 Radar ôn tập](#4-radar-ôn-tập)

---

## §0 Metadata

| Mục | Giá trị |
|---|---|
| Ngày compile | 2026-07-20 |
| Nguồn Grammar | 70 note |
| Nguồn Group | 18 note |
| Nguồn Pair | 9 note |
| Nguồn Distractor | 16 note |
| Nguồn Exam | 6 đề (TOPIK_37–TOPIK_64), mỗi đề 4 câu = 24 câu |

**Kiểm tra toàn vẹn (five-check):** ✅ 70/70 GR đủ marker `%% compile:core %%` · ✅ 18/18 GROUP đủ block `matrix` (⚠️ GROUP_mong_muon=2 & GROUP_tang_tien=1 dưới ngưỡng ≥3 — chủ đích, tách từ GROUP_dieu_kien 2026-07-14) · ✅ mọi `group` của GR khớp GROUP tồn tại (tổng thành viên = 70) · ✅ 9/9 PAIR trỏ GROUP & members hợp lệ · ✅ mọi appearances khớp đề.

**Note bị bỏ qua khi compile:** KHÔNG có. Toàn bộ note được đưa vào handbook.

> [!warning] Cảnh báo độ tin cậy — handbook đang ở mức NHÁP
> **100% note ở `status: draft`** (70 GR, 18 GROUP, 9 PAIR, 16 DIS, 6 EXAM — không note nào `verified`). Theo `source_citation_rule`, gần như mọi claim nghĩa/ràng buộc trong §1 vẫn mang `⚠️ Unverified` và phần lớn ví dụ là `(vd tự tạo)`. **Chưa dùng làm tài liệu authoritative** — cần người duyệt nâng `verified` (xóa marker ⚠️, thêm tag nguồn/`[XV]`).

**5 note "prompt-only"** (chỉ đóng vai câu gạch chân trong đề đồng nghĩa, không phải phương án A–D → `appearances: []`, `role_ratio 0C/0D`): `GR_게` (TOPIK_41-Q3), `GR_고자` (TOPIK_41-Q4, TOPIK_64-Q3), `GR_기만_하면` (TOPIK_60-Q3), `GR_달려_있다` (TOPIK_47-Q4), `GR_아어_봐야` (TOPIK_60-Q4). Đây là chủ đích, không phải lỗi thiếu dữ liệu.

---

## §1 Ma trận khác biệt theo nhóm

Mỗi nhóm: bảng phân biệt nhanh (tín hiệu chọn 3 giây) + cặp dễ nhầm (`confusion_pairs`). Hai cột **Cấp** (level TOPIK) và **Cách chia** (형태 nén 1 dòng) rút từ chính note GR mỗi hàng. Các claim còn ⚠️ Unverified do note nguồn đang draft.

### GROUP_nguyen_nhan — Nguyên nhân — lý do
`diff_axes`: sắc thái kết quả · chủ ngữ · đột ngột vs kéo dài · quy lỗi

| Ngữ pháp | Cấp | Cách chia | Sắc thái kết quả | Đột ngột? | Vế sau cấm | Ràng buộc riêng | Tín hiệu chọn nhanh (3 giây) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|---|---|---|
| [[GR_바람에]] | II (3-4) | V -는 바람에 · QK không chia ⚠️ | thường tiêu cực, ngoài ý muốn | ✅ bột phát | mệnh lệnh/rủ rê | vế trước cố định `-는` | biến cố bất ngờ gây hậu quả [TOPIK_37-Q3] | 서둘러 나오는 바람에 지갑을 놓고 나왔다 → Vì vội ra nên quên ví. [TOPIK_37-Q3] |
| [[GR_탓에]] | II (3-4) | V -는/-은 탓에 · A -은 탓에 · N 탓에/N인 탓에 ⚠️ | tiêu cực, **quy lỗi** | ✖ | mệnh lệnh | có thể là trạng thái/đặc điểm | gán trách nhiệm "tại vì" [TOPIK_47-Q3] | 늦게 일어난 탓에 기차를 놓쳤다 → Vì dậy muộn nên lỡ tàu. [TOPIK_47-Q3] |
| [[GR_느라]] | II (3-4) | V -느라(고) · QK không chia ⚠️ | tiêu cực (không làm được việc khác) | ✖ | mệnh lệnh, thì tương lai | **cùng chủ ngữ + V chủ ý** | bận làm A nên lỡ B [TOPIK_41-Q3] | 게임을 하느라 숙제를 못 했다 → Vì mải chơi game nên không làm bài. (tự tạo)⚠️ |
| [[GR_탓이다]] | II (3-4) | V -은/는 탓이다 · A -은 탓이다 · N N 탓이다 ⚠️ | quy lỗi (kết luận) | ✖ | (là vị ngữ cuối câu) | đứng cuối câu, không nối tiếp | "…là do…" chốt câu [TOPIK_52-Q4] | 일이 이렇게 된 것은 내 탓이다 → Việc thành ra thế này là lỗi của tôi. (tự tạo)⚠️ |

**Dễ nhầm:** `느라 vs 바람에` — 느라 cần V chủ ý + cùng chủ ngữ; 바람에 nhấn biến cố đột ngột, chủ ngữ tự do. · `탓에 vs 탓이다` — 탓에 nối vế "…nên"; 탓이다 là vị ngữ kết luận "…là do".

### GROUP_muc_dich — Mục đích — ý định
`diff_axes`: trang trọng · chủ ngữ vế sau · mục đích vs ý định · định hướng đối tượng

| Ngữ pháp | Cấp | Cách chia | Trang trọng | Chủ ngữ 2 vế | Vế sau cấm | Ràng buộc riêng | Tín hiệu chọn nhanh (3 giây) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|---|---|---|
| [[GR_으려고]] | II (3-4) | V(nguyên âm/ㄹ) -려고 · V(patchim) -으려고 · QK không chia ⚠️ | trung tính | **cùng chủ ngữ** | mệnh lệnh/đề nghị | mục đích của chủ thể có ý chí | "định để…" [TOPIK_52-Q1] | 해가 뜨는 것을 보려고 일찍 일어났다 → Để ngắm mặt trời mọc nên dậy sớm. [TOPIK_52-Q1] |
| [[GR_고자]] | II (3-4) | V -고자 · QK không chia ⚠️ | ✅ văn viết/trang trọng | cùng chủ ngữ | (văn nói ít dùng) | ≈ 기 위해서 | mục đích trang trọng [TOPIK_41-Q4] | 감사의 뜻을 전하고자 이 자리에 섰습니다 → Đứng đây nhằm gửi lời cảm ơn. (tự tạo)⚠️ |
| [[GR_기_위해서]] | II (3-4) | V -기 위해서 · N 을/를 위해서 ⚠️ | trung tính–trang trọng | cùng chủ ngữ (hoặc N을 위해서) | — | dùng được cả với danh từ | "để/vì" phổ quát [TOPIK_41-Q4] | 실력을 늘리기 위해서 신문을 자주 봤다 → Để nâng cao trình độ nên hay đọc báo. [TOPIK_41-Q4] |
| [[GR_기_위해]] | II (3-4) | V -기 위해 · N 을/를 위해 ⚠️ | như trên (rút gọn 서) | như trên | — | biến thể của 기 위해서 | [TOPIK_64-Q3] | 일자리를 늘리기 위해 정책을 수립했다 → Để tăng việc làm nên lập chính sách. [TOPIK_64-Q3] |
| [[GR_도록]] | II (3-4) | V/A -도록 · QK không chia ⚠️ | trung tính | **khác chủ ngữ được** | — | thêm nghĩa "tới mức/sao cho" | tác động tới đối tượng khác [TOPIK_41-Q3] | 깨지 않도록 조용히 들어갔다 → Vào khẽ sao cho (bé) không thức giấc. [TOPIK_41-Q3] |
| [[GR_게]] | II (3-4) | V/A -게 · QK không chia ⚠️ | thân mật hơn | khác chủ ngữ được | — | ≈ 도록 (sao cho) | "sao cho…" [TOPIK_41-Q3] | 잘 보이게 불을 켜 주세요 → Bật đèn sao cho nhìn rõ. (tự tạo)⚠️ |
| [[GR_기로_하다]] | II (3-4) | V -기로 하다 · QK -기로 했다 ⚠️ | trung tính | — | (là vị ngữ) | **quyết định/hẹn**, không phải mục đích thuần | "quyết định sẽ…" [TOPIK_47-Q1] | 내일 놀이공원에 가기로 했다 → Ngày mai đã hẹn đi công viên. [TOPIK_47-Q1] |

**Dễ nhầm:** `으려고 vs 기로_하다` — 으려고 = ý định để làm gì; 기로 하다 = quyết định/hẹn. · `게 vs 도록` — gần như thay được nhau ("sao cho"); 도록 thêm nghĩa "tới mức".

### GROUP_dieu_kien — Điều kiện
`diff_axes`: vế sau bắt buộc · tất yếu vs tùy nghi · điều kiện vs ý định · lặp lại

| Ngữ pháp | Cấp | Cách chia | Loại | Vế sau điển hình | Ràng buộc riêng | Tín hiệu chọn nhanh (3 giây) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|---|---|
| [[GR_아어야]] | II (3) | V(ㅏ/ㅗ) -아야 · V(khác) -어야 · 하다 해야 · A -아/어야 · QK -았/었어야 ⚠️ | điều kiện tất yếu | kết quả khả thi | "chỉ khi/phải… mới" | không có điều kiện thì không có kết quả [TOPIK_37-Q1] | 일찍 일어나야 비행기를 탈 수 있다 → Phải dậy sớm mới kịp máy bay. [TOPIK_37-Q1] |
| [[GR_거든]] | II (3-4) | V/A -거든 · N N이거든 · QK -았/었거든 ⚠️ | điều kiện tùy nghi | **mệnh lệnh/ý chí** | vế sau thường là chỉ dẫn | "nếu… thì hãy" [TOPIK_41-Q2-dis] | 서울에 오거든 꼭 연락해 → Hễ đến Seoul thì nhớ liên lạc. (tự tạo)⚠️ |
| [[GR_으려면]] | I~II (2-3) | V(không patchim) -려면 · V(patchim) -으려면 ⚠️ | điều kiện mục tiêu | điều cần làm | "nếu muốn X thì" | hướng tới mục tiêu [TOPIK_60-Q1-dis] | 합격하려면 열심히 공부해야 한다 → Muốn đỗ thì phải học chăm. (tự tạo)⚠️ |
| [[GR_기만_하면]] | II (3-4) | V/A -기만 하면 · N N이기만 하면 ⚠️ | điều kiện đủ | kết quả lặp lại | "cứ… là (luôn)" | X luôn kéo theo Y [TOPIK_60-Q3] | 술을 마시기만 하면 운다 → Cứ uống rượu là khóc. (tự tạo)⚠️ |

**Dễ nhầm:** `아어야 vs 거든` — 아어야 = điều kiện tất yếu "phải…mới"; 거든 = điều kiện tùy nghi "nếu…thì hãy".

*(Đã tách khỏi nhóm này: cặp mong muốn `-(으)면 하다`/`-(으)면 좋겠다` → GROUP_mong_muon; `-(으)ㄹ수록` → GROUP_tang_tien — 2026-07-14.)*

### GROUP_mong_muon — Mong muốn — nguyện vọng
`diff_axes`: độ trang trọng · độ chủ quan — ⚠️ nhóm **2 thành viên** (dưới ngưỡng ≥3 — placeholder, tách từ điều kiện 2026-07-14)

| Ngữ pháp | Cấp | Cách chia | Loại | Vế sau điển hình | Ràng buộc riêng | Tín hiệu chọn nhanh (3 giây) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|---|---|
| [[GR_으면_하다]] | II (3-4) | V/A -았/었으면 하다 · biến thể -으면 하다 ⚠️ | mong muốn | (là vị ngữ) | -았/었으면 하다 | "mong/giá mà" [TOPIK_37-Q2-dis] | 비가 좀 왔으면 한다 → Mong sao trời mưa chút. (tự tạo)⚠️ |
| [[GR_으면_좋겠다]] | I (2) | V/A -(으)면 좋겠다 · N N이면 좋겠다 · ước trái thực tế -았/었으면 좋겠다 ⚠️ | mong muốn | (là vị ngữ) | chủ quan hơn | "giá mà… thì tốt" [TOPIK_64-Q4-dis] | 내일 날씨가 좋으면 좋겠다 → Giá mai trời đẹp thì tốt. (tự tạo)⚠️ |

**Dễ nhầm:** `으면_하다 vs 으면_좋겠다` — cùng nghĩa mong muốn; 하다 trang trọng/khách sáo hơn, 좋겠다 chủ quan/thân mật hơn.

### GROUP_tang_tien — Tăng tiến — tỉ lệ
`diff_axes`: biến thiên song song — ⚠️ nhóm **1 thành viên** (dưới ngưỡng ≥3 — placeholder, tách từ điều kiện 2026-07-14)

| Ngữ pháp | Cấp | Cách chia | Loại | Vế sau điển hình | Ràng buộc riêng | Tín hiệu chọn nhanh (3 giây) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|---|---|
| [[GR_을수록]] | II (3-4) | V(patchim) -을수록 · V(không patchim/ㄹ) -ㄹ수록 · A -(으)ㄹ수록 · N N일수록 ⚠️ | tăng tiến tỉ lệ | biến đổi mức độ song song | nhấn `-(으)면 -(으)ㄹ수록` | "càng… càng", 2 vế cùng tăng/giảm [TOPIK_47-Q2] | 시간이 지날수록 가족이 그리워진다 → Thời gian càng trôi càng nhớ nhà. [TOPIK_47-Q2] |

**Dễ nhầm:** (chưa có — nhóm 1 thành viên).

### GROUP_tinh_thai — Tình thái
`diff_axes`: nghĩa vụ vs cho phép · chủ thể tác động · khả năng/giá trị

| Ngữ pháp | Cấp | Cách chia | Loại tình thái | Chủ thể chịu tác động | Ràng buộc riêng | Tín hiệu chọn nhanh (3 giây) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|---|---|
| [[GR_아어야_하다]] | I (2) | V -아/어야 하다 · 하다 해야 하다 · A -아/어야 하다 ⚠️ | nghĩa vụ | bản thân/chủ ngữ | "phải" | bắt buộc mới đạt [TOPIK_60-Q2-dis] | 내일까지 보고서를 내야 한다 → Phải nộp báo cáo trước mai. (tự tạo)⚠️ |
| [[GR_아어도_되다]] | I (2) | V -아/어도 되다 · 하다 해도 되다 · A -아/어도 되다 ⚠️ | cho phép | bản thân/chủ ngữ | "được phép" | cho phép/chấp nhận [TOPIK_60-Q2-dis] | 여기 앉아도 돼요 → Ngồi đây cũng được. (tự tạo)⚠️ |
| [[GR_도록_하다]] | II (3-4) | V -도록 하다 · A (hạn chế) ⚠️ | sai khiến/chỉ thị | **người khác** | 시키다 sắc thái | "làm cho/hãy để…" [TOPIK_37-Q2-dis] | 시간을 잘 지키도록 하세요 → Hãy giữ đúng giờ. (tự tạo)⚠️ |
| [[GR_을_만하다]] | II (3-4) | V(patchim) -을 만하다 · V(không patchim/ㄹ) -ㄹ 만하다 · QK -았/었을 만하다 ⚠️ | khả năng/giá trị | đối tượng/việc | "đáng/có thể" | đánh giá đáng làm [TOPIK_60-Q3-dis] | 이 영화는 한 번 볼 만해요 → Phim này đáng xem một lần. (tự tạo)⚠️ |

**Dễ nhầm:** `아어야_하다 vs 아어도_되다` (phải làm vs được phép làm). · `도록_하다 vs 아어야_하다` — 도록 하다 = khiến/chỉ thị người khác; 아어야 하다 = bản thân phải.

### GROUP_nhuong_bo — Nhượng bộ
`diff_axes`: thực tế vs giả định · cường độ nhượng bộ · tính thử nghiệm

| Ngữ pháp | Cấp | Cách chia | Thực tế / giả định | Cường độ | Ràng buộc riêng | Tín hiệu chọn nhanh (3 giây) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|---|---|
| [[GR_아어도]] | I-II (2-3) | V/A -아/어도 · N N(이)라도/여도 · QK -았/었어도 ⚠️ | cả hai (trung tính) | nhẹ | phổ biến nhất | "dù… cũng" [TOPIK_41-Q1] | 형은 차가워 보여도 마음은 따뜻하다 → Trông lạnh lùng nhưng lòng ấm. [TOPIK_41-Q1] |
| [[GR_더라도]] | II (3-4) | V/A -더라도 · N N(이)더라도 · QK -았/었더라도 ⚠️ | thiên **giả định** | mạnh | "dù cho… đi nữa" | nhấn tình huống cực đoan [TOPIK_64-Q3-dis] | 아무리 힘들더라도 포기하지 않겠다 → Dù vất vả đến đâu cũng không bỏ. (tự tạo)⚠️ |
| [[GR_다고_해도]] | II (3-4) | V -ㄴ다고/는다고 해도 · A -다고 해도 · N N(이)라고 해도 · QK -았/었다고 해도 ⚠️ | giả định/dẫn lời | mạnh | "dù cho là/nói rằng…" | nhượng bộ một giả thiết [TOPIK_60-Q4] | 수리한다고 해도 오래 쓰기 어렵다 → Dù có sửa cũng khó dùng lâu. [TOPIK_60-Q4] |
| [[GR_아어_봐야]] | II (4) | V -아/어 봐야 ⚠️ | thử → vô ích | — | vế sau thường phủ định | "có… cũng chẳng ích gì" [TOPIK_60-Q4] | 지금 가 봐야 문을 닫았을 거예요 → Giờ có đến cũng đã đóng cửa. (tự tạo)⚠️ |

**Dễ nhầm:** `아어도 vs 더라도` — 아어도 = dù thực tế/nhẹ; 더라도 = dù cho, giả định mạnh hơn. · `아어_봐야 vs 다고_해도` — 봐야 = dù có thử cũng vô ích; 다고 해도 = dù cho là… cũng.

### GROUP_doi_lap — Đối lập — thay thế
`diff_axes`: tương phản vs thay thế · độ mạnh đối lập · bối cảnh

| Ngữ pháp | Cấp | Cách chia | Loại | Độ đối lập | Ràng buộc riêng | Tín hiệu chọn nhanh (3 giây) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|---|---|
| [[GR_지만]] | I (1-2) | V/A -지만 · N N(이)지만 · QK -았/었지만 ⚠️ | tương phản | rõ | phổ quát | "A nhưng B" [TOPIK_64-Q1-dis] | 이 옷은 예쁘지만 너무 비싸요 → Áo này đẹp nhưng đắt quá. (tự tạo)⚠️ |
| [[GR_반면에]] | II (3-4) | V -는 반면에 · A -(으)ㄴ 반면에 · N N인 반면에 · QK -(으)ㄴ 반면에 ⚠️ | tương phản song song | rõ, đối chiếu | so 2 mặt trái ngược | "trong khi/ngược lại" [TOPIK_41-Q4-dis] | 돈을 많이 버는 반면에 시간이 없다 → Kiếm nhiều tiền nhưng ngược lại không có thời gian. (tự tạo)⚠️ |
| [[GR_는데]] | I (2) | V -는데 · A -(으)ㄴ데 · N N인데 · QK -았/었는데 ⚠️ | bối cảnh/tương phản nhẹ | nhẹ | đa nghĩa (nền, dẫn nhập) | "…thế mà/…và rồi" [TOPIK_52-Q1-dis] | 백화점에 갔는데 사람이 많았다 → Đi trung tâm TM mà đông người. (tự tạo)⚠️ |
| [[GR_대신에]] | II (3) | V -는 대신에 · A -(으)ㄴ 대신에 · N N 대신에 ⚠️ | thay thế/bù lại | (bù trừ) | có tiểu từ 에 | "thay vì/bù lại" [TOPIK_37-Q3-dis] | 외식하는 대신에 집에서 요리했다 → Thay vì ăn ngoài thì nấu ở nhà. (tự tạo)⚠️ |
| [[GR_대신]] | II (3) | V -는 대신 · A -(으)ㄴ 대신 · N N 대신 ⚠️ | thay thế/bù lại | (bù trừ) | biến thể không 에 | [TOPIK_47-Q3-dis] | 도와주는 대신 밥을 사 달라고 했다 → Đổi lại việc giúp thì bảo mua cơm. (tự tạo)⚠️ |

**Dễ nhầm:** `대신에 vs 대신` (cùng nghĩa thay thế/bù lại; chỉ khác tiểu từ 에). · `지만 vs 는데` — 지만 = tương phản rõ; 는데 = bối cảnh/tương phản nhẹ.

### GROUP_suy_doan — Suy đoán
`diff_axes`: căn cứ suy đoán · độ chắc chắn · khẳng định vs phủ định

| Ngữ pháp | Cấp | Cách chia | Căn cứ suy đoán | Độ chắc chắn | Ràng buộc riêng | Tín hiệu chọn nhanh (3 giây) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|---|---|
| [[GR_나_보다]] | II (3) | V -나 보다 · A -(으)ㄴ가 보다 · N N인가 보다 · QK -았/었나 보다 ⚠️ | quan sát trực tiếp | vừa | thiên khẩu ngữ; V-나 보다 / A-(으)ㄴ가 보다 | "xem chừng/hình như" [TOPIK_52-Q3] | 불이 꺼진 걸 보니 자나 봐요 → Thấy đèn tắt, chắc đang ngủ. (tự tạo)⚠️ |
| [[GR_모양이다]] | II (3-4) | V -는/(으)ㄴ 모양이다 · A -(으)ㄴ 모양이다 · N N인 모양이다 ⚠️ | dấu hiệu bên ngoài | vừa | dựa vào bằng chứng gián tiếp | "trông có vẻ/xem ra" [TOPIK_52-Q3] | 웃고 다니는 걸 보니 좋은 일이 있는 모양이다 → Cười suốt, có vẻ có chuyện vui. [TOPIK_52-Q3] |
| [[GR_을_리가_없다]] | II (3-4) | V/A -(으)ㄹ 리가 없다 · N N일 리가 없다 · QK -았/었을 리가 없다 ⚠️ | lý lẽ | **phủ định mạnh** | khẳng định điều bất khả | "không thể nào/lẽ nào" [TOPIK_64-Q4-dis] | 그 사람이 거짓말을 할 리가 없다 → Người đó lẽ nào nói dối. (tự tạo)⚠️ |

**Dễ nhầm:** `나_보다 vs 모양이다` — gần đồng nghĩa; 나 보다 thiên khẩu ngữ, 모양이다 dựa vào dấu hiệu bên ngoài.

### GROUP_trang_thai_tien_trien — Trạng thái — tiến triển
`diff_axes`: trạng thái vs biến đổi · hướng thời gian · tự thân vs tác động

| Ngữ pháp | Cấp | Cách chia | Trạng thái / biến đổi | Hướng thời gian | Ràng buộc riêng | Tín hiệu chọn nhanh (3 giây) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|---|---|
| [[GR_아어_있다]] | I~II (2-3) | V(nội động) -아/어 있다 · QK -아/어 있었다 ⚠️ | trạng thái kết quả | tĩnh (sau khi xong) | V tự động (자동사); ≠ 고 있다 | "đang ở trạng thái…" [TOPIK_37-Q2] | 동생이 여행에서 돌아와 있었다 → Em đã về (đang ở nhà) từ chuyến đi. [TOPIK_37-Q2] |
| [[GR_는_중이다]] | I~II (2-3) | V -는 중이다 · N N 중이다 · QK -는 중이었다 ⚠️ | tiến trình đang diễn ra | đang | N 중이다 / V-는 중이다 | "đang trong lúc…" [TOPIK_47-Q1-dis] | 지금 회의하는 중이다 → Bây giờ đang họp. (tự tạo)⚠️ |
| [[GR_아어_가다]] | II (3-4) | V -아/어 가다 · A (hạn chế) · QK -아/어 갔다 ⚠️ | biến đổi dần | tương lai (xa dần) | hướng ra xa/tiếp diễn | "dần dần (đi tới)…" [TOPIK_64-Q2] | 동생이 점점 아버지를 닮아 간다 → Em ngày càng giống bố. [TOPIK_64-Q2] |
| [[GR_게_되다]] | I~II (2-3) | V -게 되다 · A -아/어지다 · QK -게 되었다/됐다 ⚠️ | kết quả biến đổi | đã trở nên | bị động/ngoài ý muốn | "hoá ra/trở nên…" [TOPIK_60-Q2] | 친구 덕분에 한국 문화를 알게 되었다 → Nhờ bạn mà biết văn hóa Hàn. [TOPIK_60-Q2] |

**Dễ nhầm:** `아어_있다 vs 는_중이다` (trạng thái kết quả duy trì vs đang trong tiến trình). · `아어_가다 vs 게_되다` (biến đổi dần vs trở nên/kết quả biến đổi).

### GROUP_trinh_tu — Trình tự — tức thì
`diff_axes`: gián đoạn vs hoàn tất · độ tức thì · cùng chủ ngữ

| Ngữ pháp | Cấp | Cách chia | Quan hệ hai vế | Độ tức thì | Ràng buộc riêng | Tín hiệu chọn nhanh (3 giây) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|---|---|
| [[GR_다가]] | II (3-4) | V -다(가) · A -다(가) · N N(이)다가 · QK -았/었다가 ⚠️ | đang A → chuyển sang B | — | **cùng chủ ngữ**, A dở dang | "đang… thì" [TOPIK_60-Q1] | 휴대 전화를 보다가 역을 지나쳤다 → Đang xem điện thoại thì lỡ ga. [TOPIK_60-Q1] |
| [[GR_고서]] | II (3-4) | V -고서 · QK không chia ⚠️ | xong A rồi mới B | — | nhấn hoàn tất A trước | "…xong rồi (mới)" [TOPIK_60-Q1-dis] | 손을 씻고서 밥을 먹었다 → Rửa tay xong rồi mới ăn. (tự tạo)⚠️ |
| [[GR_자마자]] | II (3-4) | V -자마자 · QK không chia ⚠️ | A xong là B ngay | ✅ cao | nối tiếp tức thì | "vừa… là" [TOPIK_64-Q3-dis] | 집에 도착하자마자 비가 왔다 → Vừa về đến nhà là mưa. (tự tạo)⚠️ |
| [[GR_기_무섭게]] | II (5-6) | V -기 무섭게 · QK không chia ⚠️ | A xong B đến ngay | ✅ rất cao | khoa trương/nhấn mạnh | "vừa… đã (ngay)" [TOPIK_41-Q4-dis] | 수업이 끝나기 무섭게 뛰어나갔다 → Vừa hết giờ là chạy ra ngay. (tự tạo)⚠️ |
| [[GR_대로]] | II (3-4) | V(ngay khi) -는 대로 · V(y như, QK) -(으)ㄴ 대로 · N N 대로 ⚠️ | ngay khi/theo đúng | ✅ (nghĩa thời gian) | đa nghĩa (theo, y như) | "ngay khi/theo…" [TOPIK_60-Q4-dis] | 도착하는 대로 전화할게요 → Vừa tới nơi là gọi ngay. (tự tạo)⚠️ |

**Dễ nhầm:** `자마자 vs 기_무섭게` (cùng "ngay khi"; 기 무섭게 nhấn mạnh/khoa trương hơn). · `다가 vs 고서` — 다가 = đang A thì chuyển B; 고서 = xong A rồi mới B.

### GROUP_thoi_diem_khoang — Thời điểm — khoảng thời gian
`diff_axes`: thời điểm vs khoảng · lặp lại · tận dụng dịp

| Ngữ pháp | Cấp | Cách chia | Điểm / khoảng | Lặp lại? | Ràng buộc riêng | Tín hiệu chọn nhanh (3 giây) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|---|---|
| [[GR_을_때마다]] | I~II (2-3) | V/A -(으)ㄹ 때마다 · N N일 때마다/N마다 · QK -았/었을 때마다 ⚠️ | thời điểm | ✅ mỗi lần | quy luật lặp | "mỗi khi… là" [TOPIK_60-Q3] | 동생은 차를 탈 때마다 멀미를 한다 → Mỗi khi đi xe em bị say. [TOPIK_60-Q3] |
| [[GR_는_동안]] | I~II (2-3) | V -는 동안 · N N 동안 ⚠️ | khoảng (song hành) | ✖ | 2 việc kéo dài song song | "trong khi/suốt lúc" [TOPIK_60-Q3-dis] | 내가 자는 동안 동생이 청소했다 → Trong lúc tôi ngủ, em dọn dẹp. (tự tạo)⚠️ |
| [[GR_사이에]] | II (3-4) | V -는 사이에 · N N 사이에 ⚠️ | khoảng ngắn/khe | ✖ | thường có biến cố xen vào | "trong lúc (bỗng)…" [TOPIK_37-Q3-dis] | 한눈파는 사이에 아이가 사라졌다 → Trong lúc lơ đễnh, đứa bé biến mất. (tự tạo)⚠️ |
| [[GR_김에]] | II (3-4) | V -는 김에 · V(đã làm) -(으)ㄴ 김에 ⚠️ | dịp/thời cơ | ✖ | tận dụng lúc làm A → làm luôn B | "nhân tiện/nhân dịp" [TOPIK_37-Q3-dis] | 서울에 가는 김에 친구도 만났다 → Nhân tiện lên Seoul, gặp luôn bạn. (tự tạo)⚠️ |

**Dễ nhầm:** `는_동안 vs 사이에` — 는 동안 = suốt khoảng song hành; 사이에 = trong lúc, khe thời gian thường có biến cố xen.
> [!note] `PAIR_기만하면_때마다` nằm trong `pairs_inside` của nhóm này, nhưng thành viên `GR_기만_하면` thuộc GROUP_dieu_kien (quy đổi qua nghĩa "mỗi khi"). Thiết kế có chủ ý, không phải mồ côi.

### GROUP_lua_chon_lietke — Lựa chọn — liệt kê
`diff_axes`: lựa chọn vs liệt kê · bất kể · nghi vấn gián tiếp

| Ngữ pháp | Cấp | Cách chia | Chức năng | Ràng buộc riêng | Bẫy đề | Tín hiệu chọn nhanh (3 giây) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|---|---|
| [[GR_거나]] | I-II (2-3) | V/A -거나 · N (이)거나 · QK -았/었거나 ⚠️ | A **hoặc** B | 2 vế cùng cấp | có thể là "làm A hoặc B" (thay phiên) → đáp án [TOPIK_64-Q1] | "hoặc/hay" [TOPIK_64-Q1] | 주말에는 영화를 보거나 운동을 한다 → Cuối tuần xem phim hoặc tập thể dục. [TOPIK_64-Q1] |
| [[GR_든지]] | II (3-4) | V/A -든지 · N (이)든지 · QK -았/었든지 ⚠️ | **bất kể** A hay B | thường lặp 든지…든지 | ≠ 는지 | "dù… hay… đều" [TOPIK_52-Q2] | 무슨 일을 하든지 열심히 하는 게 중요하다 → Bất kể làm gì, chăm chỉ mới quan trọng. [TOPIK_52-Q2] |
| [[GR_으며]] | II (3-4) | V/A -(으)며 · N (이)며 · QK -았/었으며 ⚠️ | **liệt kê / đồng thời** | trang trọng | vừa A vừa B; và | "vừa… vừa/và" [TOPIK_37-Q1-dis] | 음악을 들으며 공부한다 → Vừa nghe nhạc vừa học. (tự tạo)⚠️ |
| [[GR_는지]] | I-II (2-3) | V -는지 · A -(으)ㄴ지 · N 인지 · QK -았/었는지 ⚠️ | **nghi vấn gián tiếp** | theo sau 알다/모르다/궁금하다… | ≠ 든지 | "…hay không/… gì" [TOPIK_41-Q3-dis] | 오는지 안 오는지 모르겠다 → Không biết có đến hay không. (tự tạo)⚠️ |

**Dễ nhầm:** `든지 vs 는지` — 든지 = bất kể/lựa chọn; 는지 = nghi vấn gián tiếp; dễ nhầm do hình thái gần. · `거나 vs 든지` — 거나 = A hoặc B chọn; 든지 = bất kể A hay B đều được.

### GROUP_khuynh_huong_quy_luat — Khuynh hướng — quy luật
`diff_axes`: tất yếu vs khả năng xấu · khuynh hướng · phụ thuộc

| Ngữ pháp | Cấp | Cách chia | Loại | Sắc thái | Ràng buộc riêng | Tín hiệu chọn nhanh (3 giây) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|---|---|
| [[GR_기_마련이다]] | II (3-4) | V/A -기 마련이다 ⚠️ | quy luật tất yếu | trung tính | "đương nhiên là" | điều hiển nhiên [TOPIK_37-Q4-dis] | 사람은 누구나 늙기 마련이다 → Ai rồi cũng già. (tự tạo)⚠️ |
| [[GR_기_십상이다]] | II (4-5) | V -기 십상이다 ⚠️ | khả năng cao (xấu) | **tiêu cực** | kết cục không mong muốn | "dễ (bị)…" [TOPIK_47-Q4-dis] | 급하게 먹으면 체하기 십상이다 → Ăn vội dễ bị đầy bụng. (tự tạo)⚠️ |
| [[GR_편이다]] | II (3) | V -는 편이다 · A -(으)ㄴ 편이다 · QK -(으)ㄴ 편이다 ⚠️ | khuynh hướng/mức độ | trung tính | "thuộc loại khá…" | đánh giá tương đối [TOPIK_37-Q4-dis] | 매운 음식을 잘 먹는 편이다 → Thuộc loại ăn cay khá tốt. (tự tạo)⚠️ |
| [[GR_기_나름이다]] | II (5-6) | V -기 나름이다 · N N 나름이다 ⚠️ | tùy thuộc | trung tính | gắn V-기 | "tùy vào việc…" [TOPIK_47-Q4] | 이기고 지는 것은 연습하기 나름이다 → Thắng thua tùy ở luyện tập. [TOPIK_47-Q4] |
| [[GR_달려_있다]] | II (5-6) | V -기에 달려 있다 · N N에 달려 있다 ⚠️ | tùy thuộc | trung tính | gắn N에/기에 | "phụ thuộc vào…" [TOPIK_47-Q4] | 성공은 노력에 달려 있다 → Thành công tùy vào nỗ lực. (tự tạo)⚠️ |

**Dễ nhầm:** `기_마련이다 vs 기_십상이다` — 마련이다 = quy luật tất yếu trung tính; 십상이다 = dễ rơi vào kết cục XẤU. · `기_나름이다 vs 달려_있다` — cùng nghĩa "tùy thuộc"; 기 나름이다 gắn V-기, 달려 있다 gắn N/기에.

### GROUP_gioi_han_danh_gia — Giới hạn — đánh giá tương đương
`diff_axes`: giới hạn vs tương đương · mức độ · văn phong

| Ngữ pháp | Cấp | Cách chia | Loại đánh giá | Văn phong | Ràng buộc riêng | Tín hiệu chọn nhanh (3 giây) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|---|---|
| [[GR_뿐이다]] | II (3-4) | V/A -(으)ㄹ 뿐이다 · N N일 뿐이다 · QK -았/었을 뿐이다 ⚠️ | giới hạn | trung tính | "chỉ… mà thôi" | không hơn không kém [TOPIK_52-Q3-dis] | 최선을 다했을 뿐이다 → Chỉ là đã làm hết sức. (tự tạo)⚠️ |
| [[GR_따름이다]] | II (3-4) | V/A -(으)ㄹ 따름이다 · QK -았/었을 따름이다 ⚠️ | giới hạn | ✅ văn viết | ≈ 뿐이다 | "chỉ… (trang trọng)" [TOPIK_47-Q4-dis] | 감사할 따름입니다 → Chỉ biết cảm ơn mà thôi. (tự tạo)⚠️ |
| [[GR_셈이다]] | II (3-4) | V -는/-(으)ㄴ 셈이다 · A -(으)ㄴ 셈이다 · N N인 셈이다 ⚠️ | tương đương/kết toán | trung tính | "tính ra/coi như là" | quy về gần bằng [TOPIK_52-Q4] | 방학도 다 끝난 셈이다 → Kỳ nghỉ coi như đã hết. [TOPIK_52-Q4] |
| [[GR_나_마찬가지이다]] | II (3-4) | V -(으)ㄴ/는 거나 마찬가지이다 · N N(이)나 마찬가지이다 ⚠️ | tương đương | trung tính | "chẳng khác nào" | gần như y hệt [TOPIK_64-Q4] | 서울이 고향이나 마찬가지이다 → Seoul chẳng khác nào quê. [TOPIK_64-Q4] |
| [[GR_지경이다]] | II (3-4) | V/A -(으)ㄹ 지경이다 ⚠️ | mức độ cực | trung tính | "đến nỗi/đến mức" | nhấn mức độ dữ dội [TOPIK_52-Q3-dis] | 배가 고파서 쓰러질 지경이다 → Đói đến mức muốn ngã quỵ. (tự tạo)⚠️ |

**Dễ nhầm:** `뿐이다 vs 따름이다` (cùng "chỉ… mà thôi"; 따름이다 văn viết/trang trọng hơn). · `셈이다 vs 나_마찬가지이다` (cùng "coi như/chẳng khác nào"; đã khép 2 chiều).

### GROUP_ve_ngoai_gia_vo — Vẻ ngoài — giả vờ
`diff_axes`: giả vờ vs giả định · chủ thể cố ý

| Ngữ pháp | Cấp | Cách chia | Cố ý? | Nghĩa | Ràng buộc riêng | Tín hiệu chọn nhanh (3 giây) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|---|---|
| [[GR_척하다]] | II (3-4) | V -는/-(으)ㄴ 척하다 · A -(으)ㄴ 척하다 · N N인 척하다 ⚠️ | ✅ cố ý | giả vờ/làm bộ | chủ thể biết sự thật | "vờ như…" [TOPIK_37-Q4] | 못 들은 척했다 → Vờ như không nghe. (tự tạo)⚠️ |
| [[GR_체하다]] | II (3-4) | V -는/-(으)ㄴ 체하다 · A -(으)ㄴ 체하다 · N N인 체하다 ⚠️ | ✅ cố ý | giả vờ (≈ 척하다) | văn viết hơn | "làm ra vẻ…" [TOPIK_37-Q4] | 미안해할까 봐 모르는 체했다 → Sợ áy náy nên vờ không biết. [TOPIK_37-Q4] |
| [[GR_듯하다]] | II (3-4) | V -는/-(으)ㄴ/-(으)ㄹ 듯하다 · A -(으)ㄴ 듯하다 · N N인 듯하다 ⚠️ | ✖ phỏng đoán | dường như/có vẻ | đánh giá khách quan | "hình như…" [TOPIK_37-Q4-dis] | 밖에 비가 오는 듯하다 → Hình như ngoài trời đang mưa. (tự tạo)⚠️ |

**Dễ nhầm:** `척하다 vs 체하다` (đồng nghĩa hoàn toàn "giả vờ"; 체하다 hơi văn viết; đã thi 1 chiều). · `척하다 vs 듯하다` — 척하다 = cố ý giả vờ; 듯하다 = phỏng đoán khách quan.

### GROUP_kinh_nghiem_tanso — Kinh nghiệm — tần suất
`diff_axes`: có vs không · kinh nghiệm vs tần suất

| Ngữ pháp | Cấp | Cách chia | Nghĩa | Cực | Ràng buộc riêng | Tín hiệu chọn nhanh (3 giây) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|---|---|
| [[GR_은_적이_있다]] | I-II (2-3) | V -(으)ㄴ 적이 있다 ⚠️ | kinh nghiệm | khẳng định | V quá khứ + 은 적이 있다 | "từng/đã có lần" [TOPIK_47-Q1-dis] | 제주도에 가 본 적이 있다 → Tôi từng đến đảo Jeju. (tự tạo)⚠️ |
| [[GR_은_적이_없다]] | I-II (2-3) | V -(으)ㄴ 적이 없다 ⚠️ | kinh nghiệm | phủ định | biến thể phủ định | "chưa từng" [TOPIK_64-Q2-dis] | 그런 말을 들어 본 적이 없다 → Chưa từng nghe câu đó. (tự tạo)⚠️ |
| [[GR_기도_하다]] | II (3-4) | V/A -기도 하다 · N N이기도 하다 · QK -기도 했다 ⚠️ | tần suất/bổ sung | — | "cũng có khi/vừa… cũng" | thi thoảng/thêm cả [TOPIK_64-Q2-dis] | 가끔 혼자 여행을 가기도 한다 → Thỉnh thoảng cũng đi du lịch một mình. (tự tạo)⚠️ |

**Dễ nhầm:** `은_적이_있다 vs 은_적이_없다` (cùng cấu trúc 은 적이, khác cực có/không từng).

### GROUP_hoi_tuong_phat_hien — Hồi tưởng — phát hiện
`diff_axes`: hồi tưởng vs phát hiện · chủ ngữ · nhân quả vs tuần tự

| Ngữ pháp | Cấp | Cách chia | Nghĩa | Chủ ngữ | Ràng buộc riêng | Tín hiệu chọn nhanh (3 giây) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|---|---|
| [[GR_더니]] | II (3-4) | V/A -더니 · N N(이)더니 · QK -았/었더니 ⚠️ | hồi tưởng → hệ quả/biến chuyển | **ngôi 3** (quan sát người/vật khác) | vế trước là điều đã thấy | "…rồi thì (nay)…" [TOPIK_37-Q1-dis] | 하늘이 흐리더니 결국 비가 왔다 → Trời âm u rồi cuối cùng đổ mưa. (tự tạo)⚠️ |
| [[GR_아어_보니까]] | II (3-4) | V -아/어 보니까 ⚠️ | thử → phát hiện | ngôi 1 thường | có bước "thử" trước | "thử… thì thấy" [TOPIK_60-Q4-dis] | 직접 만들어 보니까 쉬웠다 → Tự làm thử thì thấy dễ. (tự tạo)⚠️ |
| [[GR_으니까]] | I-II (2-3) | V/A -(으)니까 · N N(이)니까 · QK -았/었으니까 ⚠️ | lý do / làm-thì-thấy | linh hoạt | 2 nghĩa: lý do & phát hiện | "vì…/… thì (thấy)" [TOPIK_41-Q2] | 집에 도착하니까 비가 내리기 시작했다 → Về đến nhà thì trời bắt đầu mưa. [TOPIK_41-Q2] |

**Dễ nhầm:** `더니 vs 으니까` — 더니 = hồi tưởng điều đã quan sát → hệ quả; 으니까 = lý do/…thì phát hiện. · `아어_보니까 vs 으니까` — 아어 보니까 = thử làm rồi phát hiện; 으니까 = làm/đến thì thấy.

---

## §2 Bảng quy đổi hai chiều (PAIR)

9 cặp đồng nghĩa/hoán đổi đã xuất hiện trong đề. Sắp xếp: `open` (mới thi 1 chiều) lên đầu, `closed` (đã đủ 2 chiều) xuống cuối.

| Cặp | Chiều đã thi | morph_note | confidence | Nhóm |
|---|---|---|---|---|
| GR_게 ↔ GR_도록 | TOPIK_41-Q3: 게→도록 | cùng gắn sau gốc động/tính từ; 도록 thêm được nghĩa "tới mức" | 🔓 open | Mục đích |
| GR_고자 ↔ GR_기_위해서 | TOPIK_41-Q4: 고자→기 위해서 · TOPIK_64-Q3: 고자→기 위해 | 고자 gắn sau gốc V (trang trọng); 기 위해(서) gắn V-기 / N을 위해(서) | 🔓 open | Mục đích |
| GR_기만_하면 ↔ GR_을_때마다 | TOPIK_60-Q3: 기만 하면→을 때마다 | V-기만 하면 (điều kiện đủ); -(으)ㄹ 때마다 (mỗi lần) | 🔓 open | Thời điểm |
| GR_나_보다 ↔ GR_모양이다 | TOPIK_52-Q3: 나 보다→모양이다 | V-나 보다 / A-(으)ㄴ가 보다; -(으)ㄴ/는 모양이다 | 🔓 open | Suy đoán |
| GR_달려_있다 ↔ GR_기_나름이다 | TOPIK_47-Q4: 달려 있다→기 나름이다 | N에/기에 달려 있다 (vị ngữ); V-기 나름이다 (gắn V-기) | 🔓 open | Khuynh hướng |
| GR_아어_봐야 ↔ GR_다고_해도 | TOPIK_60-Q4: 아어 봐야→다고 해도 | V-아/어 봐야 (thử cũng vô ích); V-ㄴ/는다고 해도 (dù cho là) | 🔓 open | Nhượng bộ |
| GR_척하다 ↔ GR_체하다 | TOPIK_37-Q4: 척하다→체하다 | cùng gắn -(으)ㄴ/는 + 척/체 하다; khác biệt ngữ pháp ≈ 0 | 🔓 open | Vẻ ngoài |
| **GR_셈이다 ↔ GR_나_마찬가지이다** | TOPIK_52-Q4: 나 마찬가지이다→셈이다 · TOPIK_64-Q4: 셈이다→나 마찬가지이다 | 셈이다 gắn -(으)ㄴ/는 셈이다; (이)나 마찬가지이다 gắn N / -(으)ㄴ 것이나 | 🔒 **closed** | Giới hạn/đánh giá |
| **GR_탓에 ↔ GR_바람에** | TOPIK_37-Q3: 탓에→바람에 · TOPIK_47-Q3: 바람에→탓에 | 탓에 dùng -(으)ㄴ/는 tùy thì; 바람에 cố định -는, không chia quá khứ | 🔒 **closed** | Nguyên nhân |

---

## §3 Bảng nhiễu (Distractor)

16 pattern từng đóng vai nhiễu. Sắp theo `distractor_count` giảm dần. `kill_signal` = điều kiện loại 3 giây; `select_signal` = môi trường nó ĐÚNG. Cột **Ví dụ** trích câu đề thật `[TOPIK_xx-Qy]` khi pattern từng là đáp án đúng; còn lại là ví dụ tự đặt `(tự tạo)⚠️`.

| # | Pattern | nC/mD | kill_signal (loại khi…) | select_signal (đúng khi…) | Ví dụ (Hàn → Việt) |
|---|---|---|---|---|---|
| 1 | [[GR_더니]] | 0C/4D | chủ ngữ ngôi 1, hoặc không "quan sát người/vật khác rồi phát hiện biến chuyển" | vế trước là điều ĐÃ quan sát ngôi 3, vế sau biến chuyển/hệ quả bất ngờ | 하늘이 흐리더니 결국 비가 왔다 → Trời âm u rồi cuối cùng đổ mưa. (tự tạo)⚠️ |
| 2 | [[GR_거나]] | 1C/3D | câu không liệt kê 2 phương án/hành động cùng cấp để "chọn hoặc thay phiên" | có 2 hành động cùng cấp thay phiên/tùy chọn, thường có 보통·가끔 | 주말에는 보통 영화를 보거나 운동을 한다 → Cuối tuần thường xem phim hoặc tập thể dục. [TOPIK_64-Q1] |
| 3 | [[GR_으려고]] | 1C/3D | vế sau không phải hành động chủ ý nhằm mục đích (hoặc 2 vế khác chủ ngữ) | cùng chủ ngữ, vế trước là mục đích của hành động vế sau | 해가 뜨는 것을 보려고 일찍 일어났다 → Để ngắm mặt trời mọc nên dậy sớm. [TOPIK_52-Q1] |
| 4 | [[GR_다가]] | 1C/2D | 2 vế không phải "đang làm A thì B" cùng chủ ngữ | đang làm A dở dang thì B (thường ngoài ý muốn), cùng chủ ngữ | 휴대 전화를 보다가 역을 지나쳤다 → Đang xem điện thoại thì lỡ ga. [TOPIK_60-Q1] |
| 5 | [[GR_든지]] | 1C/2D | câu không mang ý "bất kể A hay B đều…" (đừng nhầm 는지 nghi vấn) | "dù… hay…/bất kể… đều", thường có từ nghi vấn (무슨/어디/누구) | 무슨 일을 하든지 열심히 하는 게 중요하다 → Bất kể làm việc gì, chăm chỉ mới quan trọng. [TOPIK_52-Q2] |
| 6 | [[GR_도록]] | 1C/2D | câu không diễn "sao cho/để đạt/tới mức" | vế sau hành động nhằm "sao cho" đối tượng đạt trạng thái, hoặc "tới mức" | 깨지 않도록 조용히 들어갔다 → Vào khẽ sao cho (bé) không thức giấc. [TOPIK_41-Q3] |
| 7 | [[GR_아어야]] | 1C/2D | câu không có logic "chỉ khi/phải X thì mới Y" | X là điều kiện tất yếu để Y ("phải… mới…") | 일찍 일어나야 비행기를 탈 수 있다 → Phải dậy sớm mới kịp máy bay. [TOPIK_37-Q1] |
| 8 | [[GR_기_마련이다]] | 0C/2D | câu không khẳng định một QUY LUẬT hiển nhiên | nêu điều tất yếu ai cũng công nhận | 사람은 누구나 늙기 마련이다 → Con người ai rồi cũng già đi. (tự tạo)⚠️ |
| 9 | [[GR_거든]] | 0C/2D | vế sau KHÔNG phải mệnh lệnh/đề nghị/ý chí | "nếu… thì hãy…" — điều kiện tùy nghi, vế sau chỉ dẫn/ý định | 서울에 오거든 꼭 연락해 → Hễ đến Seoul thì nhớ liên lạc. (tự tạo)⚠️ |
| 10 | [[GR_김에]] | 0C/2D | không có ý "tiện thể/nhân dịp làm A thì làm luôn B" | tận dụng dịp đang làm A để làm thêm B | 서울에 가는 김에 친구도 만났다 → Nhân tiện lên Seoul, gặp luôn bạn. (tự tạo)⚠️ |
| 11 | [[GR_대신]] | 0C/2D | không có quan hệ "thay vì/bù lại" | vế sau thay thế/bù trừ vế trước | 도와주는 대신 밥을 사 달라고 했다 → Đổi lại việc giúp thì bảo mua cơm. (tự tạo)⚠️ |
| 12 | [[GR_대신에]] | 0C/2D | 2 vế không có quan hệ "thay vì / bù lại" | vế sau thay thế hoặc bù trừ vế trước | 외식하는 대신에 집에서 요리했어요 → Thay vì ăn ngoài thì nấu ở nhà. (tự tạo)⚠️ |
| 13 | [[GR_도록_하다]] | 0C/2D | không có ai "làm cho/yêu cầu" đối tượng thực hiện (không nghĩa sai khiến) | chủ thể khiến/chỉ thị người khác làm gì | 시간을 잘 지키도록 하세요 → Hãy giữ đúng giờ nhé. (tự tạo)⚠️ |
| 14 | [[GR_뿐이다]] | 0C/2D | câu không giới hạn "chỉ… mà thôi, không gì hơn" | nhấn giới hạn duy nhất ("chỉ… thôi") | 나는 최선을 다했을 뿐이다 → Tôi chỉ làm hết sức mình mà thôi. (tự tạo)⚠️ |
| 15 | [[GR_편이다]] | 0C/2D | câu nói việc CỤ THỂ/kế hoạch, không phải đánh giá "thuộc loại/khá là" | đánh giá khuynh hướng/mức độ tương đối | 매운 음식을 잘 먹는 편이에요 → Thuộc loại ăn cay khá tốt. (tự tạo)⚠️ |
| 16 | [[GR_바람에]] | 1C/1D | vế sau KHÔNG phải kết quả bột phát/ngoài ý muốn | nguyên nhân đột ngột → hậu quả đã rồi, thường tiêu cực | 서둘러 나오는 바람에 지갑을 놓고 나왔다 → Vì vội ra nên quên ví. [TOPIK_37-Q3] |

> [!tip] Ba "vua nhiễu" cần thuộc kill_signal: **더니** (4D — loại ngay nếu ngôi 1), **거나** & **으려고** (3D). Gặp 3 pattern này ở phương án, ưu tiên kiểm điều kiện loại trước.

---

## §4 Radar ôn tập

### 🔓 PAIR còn `open` (mới thi 1 chiều — cần luyện chiều ngược)
7 cặp: `게↔도록` · `고자↔기_위해서` · `기만_하면↔을_때마다` · `나_보다↔모양이다` · `달려_있다↔기_나름이다` · `아어_봐야↔다고_해도` · `척하다↔체하다`. → Xem [§2](#2-bảng-quy-đổi-hai-chiều-pair).

### 📅 GR có `sr-due` trong 7 ngày
Không có dữ liệu SR — **toàn bộ note chưa khởi tạo lịch spaced-repetition** (`sr-due` trống). Chạy skill `review-scheduler` để khởi tạo (nhập kết quả review hoặc hỏi "hôm nay ôn gì").

### ⚠️ Note còn `draft` / chưa `verified`
**Toàn bộ vault**: 70/70 GR · 18/18 GROUP · 9/9 PAIR · 16/16 DIS · 6/6 EXAM đều `status: draft`. Không note nào `verified`, không note nào `needs-review`.

**Việc cần làm để nâng chất lượng handbook:**
1. Người duyệt (Xuân Vũ) rà từng note, xác nhận claim → xóa `⚠️ Unverified`, thêm tag nguồn hoặc `[XV] {ngày}`.
2. Thay ví dụ `(vd tự tạo)` bằng ví dụ trích đề khi có, hoặc giữ nhưng đánh dấu rõ.
3. Khi note sạch marker ⚠️ → nâng `status: verified`; chạy lại skill để handbook phản ánh trạng thái mới.
4. Khởi tạo SR cho các GR tần suất cao (đặc biệt nhóm "vua nhiễu": 더니, 거나, 으려고, 아어야, 다가, 든지, 도록).

---

*Hết handbook — tái sinh bằng skill `topik-grammar-compile`.*
