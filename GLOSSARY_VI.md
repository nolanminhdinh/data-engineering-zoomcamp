# Bảng Tra Cứu Thuật Ngữ Chuyên Ngành Data Engineering (English - Vietnamese Glossary)

Tài liệu này chuẩn hóa các thuật ngữ kỹ thuật được sử dụng xuyên suốt khóa học **Data Engineering Zoomcamp**. Trong ngành Data Engineering, nhiều thuật ngữ nên được giữ nguyên tiếng Anh kèm giải thích tiếng Việt để thuận tiện khi tra cứu tài liệu quốc tế và phỏng vấn việc làm.

---

## 1. Kiến Trúc & Lưu Trữ Dữ Liệu (Architecture & Storage)

| Thuật ngữ tiếng Anh | Thuật ngữ tiếng Việt / Giải thích | Ý nghĩa chuyên ngành |
| :--- | :--- | :--- |
| **Data Lake** | Hồ dữ liệu | Nơi lưu trữ tập trung dữ liệu thô (raw data) ở mọi định dạng (structured, semi-structured, unstructured) với chi phí thấp (ví dụ: Google Cloud Storage, AWS S3). |
| **Data Warehouse (DWH)** | Kho dữ liệu | Hệ thống lưu trữ dữ liệu đã được làm sạch, mô hình hóa và tối ưu cho việc truy vấn phân tích (OLAP) và báo cáo BI (ví dụ: Google BigQuery, Snowflake). |
| **Data Lakehouse** | Kiến trúc Lakehouse | Kiến trúc kết hợp sự linh hoạt, chi phí rẻ của Data Lake với khả năng quản lý giao dịch ACID và hiệu năng truy vấn của Data Warehouse. |
| **OLTP (Online Transaction Processing)** | Xử lý giao dịch trực tuyến | Cơ sở dữ liệu tối ưu hóa cho các thao tác đọc/ghi nhanh từng bản ghi đơn lẻ (CRUD), tính toàn vẹn cao (ví dụ: PostgreSQL, MySQL). |
| **OLAP (Online Analytical Processing)** | Xử lý phân tích trực tuyến | Hệ thống tối ưu hóa cho truy vấn tổng hợp phức tạp trên tập dữ liệu lớn, thường lưu trữ theo cột (Columnar Storage). |
| **Columnar Storage** | Lưu trữ dạng cột | Định dạng lưu trữ theo từng cột thay vì theo từng hàng, giúp nén tốt hơn và chỉ đọc các cột cần thiết khi truy vấn (ví dụ: Parquet, ORC). |
| **Partitioning** | Phân vùng dữ liệu | Chia nhỏ bảng dữ liệu thành các phần riêng biệt dựa trên một giá trị (thường là ngày tháng), giúp giảm khối lượng quét dữ liệu (Data scanned). |
| **Clustering** | Gom cụm dữ liệu | Sắp xếp và lưu trữ các hàng dữ liệu có giá trị tương đồng nằm liền kề nhau trong các khối lưu trữ (storage blocks). |

---

## 2. Đường Ống Dữ Liệu & Quy Trình (Data Pipelines & Processing)

| Thuật ngữ tiếng Anh | Thuật ngữ tiếng Việt / Giải thích | Ý nghĩa chuyên ngành |
| :--- | :--- | :--- |
| **Data Pipeline** | Đường ống dữ liệu | Tập hợp các bước xử lý tự động di chuyển dữ liệu từ nguồn (source) đến đích (destination). |
| **Data Ingestion** | Nạp dữ liệu / Thu nạp dữ liệu | Quá trình tiếp nhận và đưa dữ liệu thô từ các nguồn bên ngoài vào hệ thống lưu trữ. |
| **Batch Processing** | Xử lý theo lô / theo đợt | Xử lý các khối lượng dữ liệu lớn tại các thời điểm định kỳ (hàng giờ, hàng ngày, hàng tuần). |
| **Stream Processing** | Xử lý theo luồng / thời gian thực | Xử lý liên tục từng bản ghi (record/event) ngay khi chúng vừa được tạo ra. |
| **ETL (Extract - Transform - Load)** | Trích xuất - Chuyển đổi - Nạp | Dữ liệu được trích xuất từ nguồn, biến đổi trên máy chủ xử lý trung gian, sau đó nạp vào kho dữ liệu. |
| **ELT (Extract - Load - Transform)** | Trích xuất - Nạp - Chuyển đổi | Dữ liệu được nạp thẳng vào kho dữ liệu ở dạng thô, sau đó tận dụng sức mạnh tính toán của DWH (như BigQuery) để biến đổi bằng SQL. |
| **Workflow Orchestration** | Điều phối quy trình công việc | Lập lịch, theo dõi sự phụ thuộc, giám sát và quản lý việc thực thi các tác vụ trong đường ống dữ liệu (ví dụ: Kestra, Airflow). |
| **DAG (Directed Acyclic Graph)** | Đồ thị có hướng không chu trình | Mô hình biểu diễn thứ tự thực thi của các tác vụ trong pipeline mà không bị lặp vô tận. |
| **Idempotency** | Tính lũy đẳng / Tính bất biến kết quả | Đặc tính đảm bảo nếu chạy lại cùng một pipeline/tác vụ nhiều lần với cùng input thì kết quả vẫn nhất quán và không sinh dữ liệu trùng lặp. |
| **Backfill** | Chạy bù dữ liệu lịch sử | Chạy lại pipeline cho các mốc thời gian trong quá khứ khi có thay đổi logic hoặc khi vừa nạp dữ liệu mới. |

---

## 3. Kỹ Thuật Phân Tích & Mô Hình Hóa (Analytics Engineering & Data Modeling)

| Thuật ngữ tiếng Anh | Thuật ngữ tiếng Việt / Giải thích | Ý nghĩa chuyên ngành |
| :--- | :--- | :--- |
| **Analytics Engineering** | Kỹ thuật phân tích dữ liệu | Cầu nối giữa Data Engineering và Data Analytics, áp dụng các tiêu chuẩn kỹ thuật phần mềm (CI/CD, testing, version control) vào việc mô hình hóa dữ liệu bằng SQL. |
| **dbt (data build tool)** | Công cụ dbt | Framework biến đổi dữ liệu (Transform) chuẩn công nghiệp, sử dụng SQL kết hợp Jinja templating. |
| **Fact Table** | Bảng sự kiện / Bảng dữ kiện | Bảng chứa các số đo định lượng, số liệu kinh doanh (metrics, facts) gắn liền với các mốc thời gian (ví dụ: bảng đơn hàng, bảng chuyến đi taxi). |
| **Dimension Table** | Bảng chiều không gian / Bảng thuộc tính | Bảng chứa các thuộc tính mô tả ngữ cảnh cho bảng Fact (ví dụ: bảng thông tin khách hàng, bảng danh mục địa điểm). |
| **Star Schema** | Lược đồ hình sao | Mô hình dữ liệu trong đó bảng Fact nằm ở trung tâm và kết nối trực tiếp với các bảng Dimension xung quanh. |
| **Snowflake Schema** | Lược đồ hình bông tuyết | Biến thể của Star Schema trong đó các bảng Dimension được chuẩn hóa tiếp thành nhiều bảng nhỏ hơn. |
| **Data Lineage** | Nguồn gốc dòng dữ liệu | Sơ đồ truy vết chuỗi vòng đời của dữ liệu: dữ liệu bắt nguồn từ đâu, đi qua những biến đổi nào và phục vụ báo cáo nào. |

---

## 4. Công Nghệ Đóng Gói & Hạ Tầng (Containerization & Infrastructure)

| Thuật ngữ tiếng Anh | Thuật ngữ tiếng Việt / Giải thích | Ý nghĩa chuyên ngành |
| :--- | :--- | :--- |
| **Containerization** | Đóng gói ứng dụng / Đóng gói container | Đóng gói ứng dụng cùng mọi thư viện và môi trường phụ thuộc vào một container độc lập. |
| **Docker Image** | Bản dựng Docker / Ảnh Docker | Bản mẫu bất biến (read-only blueprint) chứa mã nguồn và các thiết lập cần thiết để khởi chạy container. |
| **Docker Container** | Phiên bản chạy của Docker Image | Thực thể đang chạy của một Docker image trong môi trường cô lập. |
| **Docker Compose** | Công cụ điều phối đa container | Công cụ định nghĩa và chạy đồng thời nhiều container bằng một file YAML. |
| **IaC (Infrastructure as Code)** | Hạ tầng dưới dạng mã nguồn | Quản lý và cung cấp hạ tầng máy chủ, mạng, cơ sở dữ liệu thông qua các tệp mã nguồn thay vì cấu hình thủ công trên giao diện web (ví dụ: Terraform). |
| **Terraform State** | Trạng thái Terraform | File lưu giữ bức tranh thực tế về hạ tầng đã được tạo ra để so sánh và cập nhật khi có thay đổi code. |

---

## 5. Xử Lý Phân Tán & Luồng Dữ Liệu (Distributed Processing & Streaming)

| Thuật ngữ tiếng Anh | Thuật ngữ tiếng Việt / Giải thích | Ý nghĩa chuyên ngành |
| :--- | :--- | :--- |
| **Apache Spark** | Công cụ tính toán phân tán Spark | Framework tính toán phân tán trong bộ nhớ (in-memory) cho các tác vụ xử lý dữ liệu quy mô cực lớn. |
| **PySpark** | Giao diện Python cho Spark | Thư viện Python cho phép lập trình viên tương tác với Spark Engine. |
| **RDD (Resilient Distributed Dataset)** | Tập dữ liệu phân tán có khả năng phục hồi | Cấu trúc dữ liệu nền tảng cốt lõi của Spark, có khả năng chịu lỗi và tính toán song song. |
| **Dataframe** | Khung dữ liệu phân tán | Cấu trúc dữ liệu dạng bảng 2 chiều (hàng và cột) được Spark tối ưu hóa bằng Catalyst Optimizer. |
| **Shuffle** | Quá trình xáo trộn / phân phối lại dữ liệu | Thao tác Spark truyền tải dữ liệu qua mạng giữa các node khi thực hiện các phép gom nhóm (GroupBy) hoặc kết nối (Join). |
| **Message Broker** | Bộ định tuyến trung gian thông điệp | Hệ thống tiếp nhận, lưu trữ tạm và chuyển tiếp các thông điệp giữa các dịch vụ (ví dụ: Apache Kafka, Redpanda). |
| **Topic** | Chủ đề dữ liệu | Kênh phân loại dữ liệu trong Kafka/Redpanda nơi các message được ghi vào. |
| **Partition** | Phân vùng trong Topic | Đơn vị mở rộng quy mô song song trong Kafka, đảm bảo thứ tự message theo từng partition. |
| **Offset** | Chỉ số vị trí bản ghi | Số nguyên định danh tuần tự cho từng message trong một partition. |
| **Producer** | Bên phát dữ liệu | Ứng dụng/tiến trình gửi message vào Topic. |
| **Consumer** | Bên tiêu thụ dữ liệu | Ứng dụng/tiến trình đọc message từ Topic. |
| **Consumer Group** | Nhóm tiêu thụ | Nhóm các consumer cùng chia sẻ việc đọc dữ liệu từ các partition của một topic. |
| **Tumbling Window** | Cửa sổ thời gian không gối lặp | Cửa sổ phân chia luồng dữ liệu thành các khoảng thời gian cố định, liên tiếp và không chồng lấn lên nhau (ví dụ: mỗi 5 phút một lần). |
| **Sliding Window** | Cửa sổ thời gian trượt | Cửa sổ thời gian di chuyển với bước nhảy nhỏ hơn độ dài cửa sổ, cho phép các khoảng thời gian gối lên nhau. |
| **Late Data / Out-of-Order Events** | Dữ liệu đến trễ | Các sự kiện có timestamp xảy ra sớm nhưng do độ trễ mạng nên được hệ thống tiếp nhận muộn hơn thời gian xử lý. |
