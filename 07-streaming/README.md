# Module 7: Xử Lý Dữ Liệu Theo Luồng (Streaming)

Trong module này, bạn sẽ làm quen với thế giới **Xử lý dữ liệu theo thời gian thực (Real-time Stream Processing)**. Bạn sẽ sử dụng **Redpanda** (một message broker hiệu năng cao hoàn toàn tương thích với giao thức Apache Kafka), viết mã nguồn Python để phát thông điệp (Produce) và tiêu thụ thông điệp (Consume), lưu trữ sự kiện vào **PostgreSQL**, và áp dụng công cụ xử lý luồng hàng đầu **Apache Flink (PyFlink)** để thực hiện các phép tổng hợp dữ liệu qua cửa sổ thời gian (Window Aggregation), xử lý dữ liệu đến trễ (Late Events) và cập nhật dữ liệu (Upserts).

---

## Danh Sách Bài Học (Units)

1. [Workshop Xử lý luồng với PyFlink (PyFlink: Stream Processing Workshop)](01-introduction.md)
2. [Giới thiệu Redpanda - Message Broker tương thích Kafka (Redpanda)](02-redpanda.md)
3. [Phát thông điệp vào Kafka bằng Python (Produce messages to Kafka)](03-produce-messages-to-kafka.md)
4. [Đọc thông điệp từ Kafka bằng Python (Consume messages with Python)](04-consume-messages-with-python.md)
5. [Lưu trữ các sự kiện luồng vào PostgreSQL (Save events to PostgreSQL)](05-save-events-to-postgresql.md)
6. [Tại sao lại là Apache Flink? (Why Flink?)](06-why-flink.md)
7. [Hình ảnh Docker Flink và các dịch vụ đi kèm (Flink image and services)](07-the-flink-image-and-services.md)
8. [Tác vụ Flink chuyển tiếp dữ liệu cơ bản (Pass-through Flink job)](08-the-pass-through-flink-job.md)
9. [Cơ chế vị trí đọc Offsets: earliest so với latest (Offsets)](09-offsets-earliest-vs-latest.md)
10. [Tính toán tổng hợp với Cửa sổ Tumbling Windows (Aggregation with Tumbling Windows)](10-aggregation-with-tumbling-windows.md)
11. [Xử lý dữ liệu đến trễ và kỹ thuật Upserts (Late events and upserts)](11-late-events-and-upserts.md)
12. [Hiểu rõ các loại cửa sổ thời gian trong Stream Processing (Window types)](12-understanding-window-types.md)
13. [Dọn dẹp môi trường (Cleanup)](13-cleanup.md)
14. [Hỏi đáp các vấn đề thường gặp (Q&A)](14-questions-and-answers.md)

---

## Bài Tập Về Nhà (Homework)

* Kiểm tra đề bài trong thư mục `cohorts/` tương ứng (ví dụ: `cohorts/2026/07-streaming/` hoặc `cohorts/2027/`).

---

## Mã Nguồn Thực Hành (Workshop Code)

* [`code/`](code/) — Toàn bộ dự án workshop PyFlink (gồm Redpanda, Python, Apache Flink, PostgreSQL).

---

## Tài Liệu Bổ Sung Tùy Chọn (Optional Material)

* [Lý thuyết Apache Kafka (theory/)](theory/) — Các bài giảng video giải thích chuyên sâu về kiến trúc Kafka với ví dụ bằng Java.
* [Mã nguồn mở rộng (extras/)](extras/) — Các ví dụ Python và PyFlink từ các khóa trước.

---

## Ghi Chú Của Cộng Đồng (Community Notes)

<details>
<summary>Nhấn để xem ghi chú và tài liệu từ học viên</summary>

* [Ghi chú từ Alvaro Navas](https://github.com/ziritrion/dataeng-zoomcamp/blob/main/notes/6_streaming.md)
* [Bài viết tiếng Tây Ban Nha của Marcos Torregrosa](https://www.n4gash.com/2023/data-engineering-zoomcamp-semana-6-stream-processing/)
* [Ghi chú từ Oscar Garcia](https://github.com/ozkary/Data-Engineering-Bootcamp/tree/main/Step6-Streaming)
* [Ghi chú từ Shayan Shafiee Moghadam](https://github.com/shayansm2/eng-notebook/blob/main/kafka/readme.md)

</details>
