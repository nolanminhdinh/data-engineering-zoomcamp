---
video_url: https://www.youtube.com/watch?v=-JLnp-iLins
prev_url: ../01-docker-terraform/13-gcp-overview.md
next_url: 02-what-is-kestra.md
---
# Điều Phối Quy Trình Công Việc Là Gì? (What is Workflow Orchestration?)

Hãy liên tưởng đến một dàn nhạc giao hưởng (orchestra). Trong dàn nhạc có rất nhiều nhạc cụ khác nhau, mỗi nhạc cụ đóng một vai trò và biểu diễn những đoạn nhạc riêng biệt. Để đảm bảo tất cả các nhạc cụ cùng hòa tấu nhịp nhàng và chính xác tại từng thời điểm, họ cần một **nhạc trưởng (conductor)** đứng ra chỉ huy toàn bộ dàn nhạc.

Bây giờ, hãy thay thế các nhạc cụ bằng các **công cụ / nền tảng công nghệ (tools & platforms)** và thay thế nhạc trưởng bằng một **công cụ điều phối quy trình (Workflow Orchestrator)**. Trong kiến trúc dữ liệu, chúng ta thường có rất nhiều công cụ và hệ thống cần phối hợp chặt chẽ với nhau: một số chạy theo lịch trình cố định (schedules), một số chạy dựa trên các sự kiện phát sinh (event-driven). Đó chính là lúc công cụ điều phối phát huy vai trò làm nhạc trưởng điều hành toàn bộ hệ sinh thái dữ liệu.

---

## Các Nhiệm Vụ Cốt Lõi Của Một Workflow Orchestrator:

- **Thực thi các quy trình (Workflows)** bao gồm chuỗi các bước được định nghĩa trước (DAG - Directed Acyclic Graph).
- **Giám sát và ghi nhận nhật ký (Monitoring & Logging)**: theo dõi trạng thái, cảnh báo lỗi và tự động thực hiện các hành động xử lý ngoại lệ (thử lại - retry, gửi email/slack thông báo).
- **Tự động kích hoạt (Triggers)**: khởi chạy quy trình dựa trên lịch biểu thời gian (cron schedules) hoặc sự kiện kích hoạt (webhook, file mới xuất hiện trong bucket,...).

---

## Tầm Quan Trọng Trong Data Engineering

Trong ngành Kỹ thuật Dữ liệu, bạn liên tục phải luân chuyển dữ liệu từ nơi này sang nơi khác, đi kèm với các bước biến đổi, làm sạch và nạp dữ liệu ở giữa. Công cụ điều phối quy trình sẽ quản lý chặt chẽ sự phụ thuộc giữa các bước, đảm bảo bước trước thành công thì bước sau mới chạy, đồng thời cung cấp giao diện trực quan theo dõi toàn diện dòng chảy dữ liệu (data observability).

Trong Module 2 này, chúng ta sẽ xây dựng đường ống dữ liệu hoàn chỉnh theo mô hình ETL (Trích xuất, Chuyển đổi, Nạp) với **Kestra** làm trung tâm điều phối.
