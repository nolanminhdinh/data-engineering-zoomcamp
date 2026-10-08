# Đồ Án Tốt Nghiệp Khóa Học (Course Project)

[🎥 Video hướng dẫn thực hiện đồ án (Bắt buộc xem!)](https://www.youtube.com/watch?v=BL0E8xO8OnE)

---

### Mục Tiêu (Objective)

Mục tiêu của đồ án cuối khóa là vận dụng tổng hợp toàn bộ các kỹ năng và công nghệ đã học trong suốt khóa học để tự tay xây dựng một đường ống dữ liệu toàn diện (end-to-end data pipeline).

### Đề Bài Dự Án (Problem Statement)

Xây dựng một bảng điều khiển phân tích (Dashboard) với ít nhất 2 biểu đồ (tiles) thông qua các bước:

* Lựa chọn một bộ dữ liệu quan tâm (xem [Danh sách gợi ý bộ dữ liệu](#danh-sách-bộ-dữ-liệu-datasets)).
* Xây dựng đường ống dữ liệu để xử lý và nạp tập dữ liệu này vào Hồ dữ liệu (Data Lake).
* Xây dựng đường ống chuyển dữ liệu từ Data Lake vào Kho dữ liệu (Data Warehouse).
* Biến đổi dữ liệu (Transformations) trong Data Warehouse: mô hình hóa và chuẩn bị bảng dữ liệu phục vụ trực quan hóa.
* Xây dựng Dashboard để hiển thị các chỉ số và phân tích hữu ích từ dữ liệu.

### Quy Định Về Dữ Liệu Không Được Phép Sử Dụng (Datasets You Cannot Use)

> [!WARNING]
> Bộ dữ liệu New York Taxi (NYC Taxi dataset) đã được sử dụng xuyên suốt các bài giảng và bài tập về nhà của khóa học. **Bạn KHÔNG ĐƯỢC PHÉP sử dụng bộ dữ liệu NYC Taxi cho đồ án cuối khóa.** Hãy chọn một bộ dữ liệu thực tế khác.

---

## Lựa Chọn Đường Ống Dữ Liệu (Data Pipeline)

Đường ống của bạn có thể xử lý theo dạng **Xử lý luồng (Stream)** hoặc **Xử lý theo lô (Batch)** — đây là quyết định kiến trúc đầu tiên bạn cần đưa ra:

* **Stream**: Phù hợp nếu bạn muốn tiếp nhận và xử lý sự kiện theo thời gian thực (real-time) rồi đưa vào Data Lake.
* **Batch**: Phù hợp nếu bạn muốn chạy xử lý định kỳ theo lịch trình (ví dụ: mỗi giờ một lần hoặc hàng ngày).

## Công Nghệ Sử Dụng (Technologies)

Bạn không bị giới hạn trong các công nghệ đã được dạy trong khóa học. Bạn hoàn toàn có thể lựa chọn các giải pháp thay thế tương đương:

* **Nền tảng Cloud**: Google Cloud Platform (GCP), AWS, Azure,...
* **Hạ tầng dưới dạng mã nguồn (IaC)**: Terraform, Pulumi, CloudFormation,...
* **Điều phối quy trình (Workflow Orchestration)**: Kestra, Apache Airflow, Prefect, Dagster, Mage,...
* **Kho dữ liệu (Data Warehouse)**: Google BigQuery, Snowflake, Amazon Redshift, ClickHouse,...
* **Xử lý theo lô (Batch Processing)**: Apache Spark, DuckDB, dbt, Flink, AWS Batch,...
* **Xử lý luồng (Stream Processing)**: Apache Kafka, Redpanda, Apache Flink, AWS Kinesis, RabbitMQ,...

Nếu bạn sử dụng một công cụ chưa được giới thiệu trong khóa học, hãy nhớ giải thích rõ trong README của dự án công cụ đó đảm nhận vai trò gì.

---

## Bảng Điều Khiển Trực Quan Hóa (Dashboard)

Bạn có thể sử dụng bất kỳ công cụ BI nào (ví dụ: Looker Studio, Streamlit, Metabase, Tableau, Power BI) để dựng Dashboard. Nếu dùng công cụ local, hãy đảm bảo người chấm (peer reviewers) có thể dễ dàng xem được hình ảnh hoặc truy cập báo cáo.

Dashboard của bạn cần có tối thiểu 2 biểu đồ phân tích (tiles), gợi ý:
- 1 biểu đồ thể hiện phân bố của biến phân loại (categorical data).
- 1 biểu đồ thể hiện xu hướng của số liệu theo chuỗi thời gian (temporal/time-series).

Đảm bảo các biểu đồ có chú thích, tiêu đề rõ ràng và trực quan dễ hiểu.

Ví dụ minh họa Dashboard:  
![Ví dụ Dashboard](https://user-images.githubusercontent.com/4315804/159771458-b924d0c1-91d5-4a8a-8c34-f36c25c31a3c.png)

---

## Quy Trình Đánh Giá Chéo (Peer Reviewing)

> [!IMPORTANT]  
> Khóa học áp dụng cơ chế đánh giá chéo giữa các học viên (Peer Reviewing). Đây là cơ hội tuyệt vời để bạn học hỏi từ cách tiếp cận và mã nguồn của bạn bè quốc tế.
> * Để được công nhận điểm đồ án của bản thân, **bạn bắt buộc phải chấm chéo ít nhất 3 dự án** của các học viên khác.
> * Bạn sẽ nhận thêm 3 điểm thưởng cho mỗi lượt chấm bài hoàn thành.

---

## Tiêu Chí Chấm Điểm Chi Tiết (Evaluation Criteria)

* **Mô tả bài toán (Problem description)**
    * 0 điểm: Không mô tả bài toán.
    * 2 điểm: Có mô tả nhưng sơ sài hoặc chưa rõ ràng.
    * 4 điểm: Bài toán được mô tả rõ ràng, nêu bật giá trị giải pháp và mục tiêu đồ án.
* **Điện toán đám mây (Cloud)**
    * 0 điểm: Không dùng Cloud, chỉ chạy hoàn toàn trên máy local cá nhân.
    * 2 điểm: Dự án được triển khai trên nền tảng Cloud.
    * 4 điểm: Dự án triển khai trên Cloud và hạ tầng được quản lý hoàn toàn bằng công cụ IaC (như Terraform).
* **Nạp dữ liệu (Data Ingestion - Chọn Batch hoặc Stream)**
    * *Nếu chọn Batch / Workflow Orchestration:*
        * 0 điểm: Không sử dụng công cụ điều phối (chạy thủ công).
        * 2 điểm: Điều phối một phần: một số bước có điều phối, một số bước vẫn phải chạy tay.
        * 4 điểm: Pipeline tự động hóa hoàn chỉnh (End-to-end): nhiều bước trong DAG liên kết chặt chẽ, tự động tải dữ liệu lên Data Lake.
    * *Nếu chọn Stream:*
        * 0 điểm: Không có hệ thống streaming (như Kafka, Redpanda,...).
        * 2 điểm: Pipeline streaming đơn giản với 1 consumer và 1 producer.
        * 4 điểm: Sử dụng consumer/producers kết hợp các công nghệ xử lý luồng nâng cao (Kafka Streaming, Spark Streaming, Flink,...).
* **Kho dữ liệu (Data Warehouse)**
    * 0 điểm: Không sử dụng DWH.
    * 2 điểm: Có tạo bảng trong DWH nhưng chưa được tối ưu hóa.
    * 4 điểm: Các bảng được Phân vùng (Partitioned) và Gom cụm (Clustered) hợp lý phục vụ các câu truy vấn phân tích thường xuyên (kèm giải thích rõ ràng).
* **Biến đổi dữ liệu (Transformations - dbt, Spark, v.v.)**
    * 0 điểm: Không có bước biến đổi dữ liệu.
    * 2 điểm: Chỉ dùng các câu lệnh SQL đơn giản chạy thủ công (không dùng dbt hay công cụ tương đương).
    * 4 điểm: Các bước biến đổi được xây dựng bài bản bằng dbt, Spark hoặc công nghệ tương đương (có lineage, modular models).
* **Bảng điều khiển (Dashboard)**
    * 0 điểm: Không có dashboard.
    * 2 điểm: Dashboard có 1 biểu đồ.
    * 4 điểm: Dashboard hoàn chỉnh với ít nhất 2 biểu đồ phân tích ý nghĩa.
* **Khả năng tái lập và chạy lại (Reproducibility)**
    * 0 điểm: Không có hướng dẫn cách chạy mã nguồn.
    * 2 điểm: Có hướng dẫn nhưng thiếu sót, người chấm khó chạy lại.
    * 4 điểm: Hướng dẫn chi tiết, rõ ràng từng bước, môi trường dễ khởi tạo và mã nguồn chạy thành công.

> [!NOTE]
> Bạn nên tạo một **repository riêng biệt trên GitHub** cho đồ án (không làm chung bên trong repo này) với tên dự án ấn tượng (ví dụ: `crypto-market-analytics`, `flight-delay-intelligence`), kèm theo file `README.md` được trau chuốt tỉ mỉ. Điều này giúp nâng cao điểm số và là sản phẩm xuất sắc để đưa vào CV ứng tuyển việc làm!

---

## Nâng Cấp Chất Lượng Đồ Án (Tùy Chọn - Không Chấm Điểm)

Những tiêu chí sau không bắt buộc nhưng sẽ giúp dự án của bạn nổi bật vượt trội trong mắt nhà tuyển dụng:
* Thêm bộ kiểm thử tự động (Unit tests, Data tests).
* Sử dụng `Makefile` để chuẩn hóa các thao tác thực thi lệnh.
* Thiết lập luồng tự động hóa CI/CD (GitHub Actions) để kiểm tra code và chạy kiểm thử mỗi lần commit.

---

## Lời Khuyên Từ Các Học Viên Đánh Giá Chéo (Peer Reviewer Tips)

* **Kiểm tra repo từ một bản clone mới tinh**: Nhiều bạn quên không commit các file quan trọng (`requirements.txt`, thư mục cấu hình, thư mục docker volume trỏ sai đường dẫn). Nếu file không có trên GitHub, người chấm sẽ không thể chạy được!
* **Tuyệt đối không hardcode đường dẫn cục bộ hoặc GCP Project ID cá nhân**: Hãy sử dụng biến môi trường (environment variables / `.env`) và hướng dẫn trong README.
* **Xử lý ngoại lệ khi gọi API bên ngoài**: Nếu script lấy dữ liệu từ link bên ngoài, cần bắt lỗi trong trường hợp server trả về lỗi 404 hoặc 500.
* **Chạy thử `docker compose up` trước khi nộp bài**: Đảm bảo không bị lỗi cú pháp YAML hoặc xung đột port.
* **Giữ tài liệu README ăn khớp với mã nguồn thực tế**: Kiểm tra các port, lệnh chạy và đường dẫn trong README xem có khớp với phiên bản code mới nhất không.
* **Dự án dbt cần chạy lệnh cài đặt gói phụ thuộc**: Nếu dùng `dbt_utils`, hãy ghi nhớ chạy `dbt deps`.

---

## Quy Định Về Chống Gian Lận Và Sao Chép (Anti-Plagiarism)

Mọi hành vi sao chép (đạo nhái) đều bị nghiêm cấm. Đồ án sẽ nhận **0 điểm** nếu:
* Sử dụng lại notebook hoặc đồ án của người khác (toàn bộ hoặc một phần).
* Sử dụng lại đồ án của chính bạn từ các khóa học / bootcamp khác.
* Sử dụng lại đồ án giữa kỳ hoặc đồ án từ các khóa ML Zoomcamp trước đây.

---

## Tài Nguyên & Thư Viện Đồ Án Tiêu Biểu (Projects Gallery)

Khám phá hàng trăm đồ án tốt nghiệp xuất sắc từ các cựu học viên để lấy cảm hứng và học hỏi cấu trúc dự án:

[![Thư Viện Đồ Án Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://datatalksclub-projects.streamlit.app/)

* [Đồ án tiêu biểu khóa 2023](../cohorts/2023/project.md)
* [Đồ án tiêu biểu khóa 2022](../cohorts/2022/project.md)
