# Module 2: Điều Phối Quy Trình Công Việc (Workflow Orchestration)

Module này hướng dẫn cách tổ chức, tự động hóa, lập lịch và quản lý các luồng dữ liệu (data pipelines) từ cơ bản đến nâng cao sử dụng công cụ điều phối hiện đại **Kestra**, kết hợp với **PostgreSQL**, **Google Cloud Storage (GCS)**, **BigQuery**, và ứng dụng **Trí tuệ nhân tạo (AI Copilot & Context Engineering)** để tăng tốc xây dựng pipeline.

---

## Danh Sách Bài Học (Units)

1. [Điều phối quy trình công việc là gì? (What is Workflow Orchestration?)](01-what-is-workflow-orchestration.md)
2. [Kestra là gì? (What is Kestra?)](02-what-is-kestra.md)
3. [Cài đặt Kestra (Installing Kestra)](03-installing-kestra.md)
4. [Các khái niệm cốt lõi trong Kestra (Kestra Concepts)](04-kestra-concepts.md)
5. [Điều phối mã nguồn Python (Orchestrate Python Code)](05-orchestrate-python-code.md)
6. [Xây dựng quy trình đầu tiên (Getting Started Pipeline)](06-getting-started-pipeline.md)
7. [Database cục bộ: Nạp dữ liệu Taxi vào Postgres (Load Taxi Data to Postgres)](07-load-taxi-data-to-postgres.md)
8. [Database cục bộ: Lập lịch và Chạy bù dữ liệu (Scheduling and Backfills)](08-scheduling-and-backfills.md)
9. [So sánh kiến trúc ETL và ELT (ETL vs ELT)](09-etl-vs-elt.md)
10. [Thiết lập nền tảng Google Cloud (Setup GCP)](10-setup-google-cloud-platform.md)
11. [Quy trình GCP: Nạp dữ liệu Taxi vào BigQuery (Load Taxi Data to BigQuery)](11-load-taxi-data-to-bigquery.md)
12. [Quy trình GCP: Lập lịch và chạy bù toàn bộ tập dữ liệu (Schedule and Backfill Full Dataset)](12-schedule-and-backfill-full-dataset.md)
13. [Giới thiệu: Tại sao nên ứng dụng AI vào điều phối quy trình? (Why AI for Workflows?)](13-why-ai-for-workflows.md)
14. [Kỹ nghệ ngữ cảnh với ChatGPT (Context Engineering with ChatGPT)](14-context-engineering-with-chatgpt.md)
15. [Trợ lý AI Copilot trong Kestra (AI Copilot in Kestra)](15-ai-copilot-in-kestra.md)
16. [Nâng cao: Ứng dụng RAG vào đường ống dữ liệu (Retrieval Augmented Generation)](16-retrieval-augmented-generation.md)
17. [Nâng cao: Triển khai lên đám mây - Tùy chọn (Deploy to the Cloud)](17-deploy-to-the-cloud.md)
18. [Tài nguyên tham khảo bổ sung (Additional Resources)](18-additional-resources.md)

---

## Bài Tập Về Nhà (Homework)

* Kiểm tra thư mục `cohorts/` tương ứng (ví dụ: `cohorts/2026/02-workflow-orchestration/` hoặc `cohorts/2027/`).

---

## Chi Tiết Các Phần Học (Sections)

### 2.1 Giới thiệu về Điều phối quy trình công việc (Introduction to Workflow Orchestration)
Trong phần này, bạn sẽ tìm hiểu nền tảng của điều phối quy trình công việc, tầm quan trọng của nó trong kiến trúc dữ liệu hiện đại, và vị trí của Kestra trong bức tranh toàn cảnh công nghệ điều phối.

### 2.2 Bắt đầu với Kestra (Getting Started with Kestra)
Học cách cài đặt Kestra cục bộ bằng Docker Compose, nắm vững các khái niệm then chốt (Flows, Tasks, Triggers, Execution) và mở rộng luồng bằng cách thực thi script Python trực tiếp bên trong workflow.

Các bước thực hành:
1. Cài đặt Kestra sử dụng Docker Compose.
2. Nắm vững cấu trúc Kestra YAML để xây dựng workflow đầu tiên.
3. Thực thi một mã nguồn Python bên trong Kestra Flow.

### 2.3 Dự án thực hành: Xây dựng Data Pipeline với Kestra
Xây dựng pipeline ETL hoàn chỉnh cho dữ liệu NYC Yellow và Green Taxi từ Ủy ban Taxi & Limousine thành phố New York (TLC):
1. Trích xuất dữ liệu từ các [tệp CSV phát hành](https://github.com/DataTalksClub/nyc-tlc-data/releases).
2. Nạp dữ liệu vào PostgreSQL cục bộ hoặc lưu trữ trên Google Cloud (GCS + BigQuery).
3. Thiết lập lập lịch tự động (scheduling) và chạy bù dữ liệu lịch sử (backfilling).

### 2.4 Đường ống ELT trong Kestra: Nền tảng Google Cloud (GCP)
Chuyển đổi từ môi trường cục bộ lên môi trường Cloud chuẩn doanh nghiệp:
1. Sử dụng Google Cloud Storage (GCS) làm Hồ dữ liệu (Data Lake).
2. Sử dụng BigQuery làm Kho dữ liệu (Data Warehouse).

### 2.5 Ứng dụng AI vào Kỹ thuật Dữ liệu trong Kestra
Tận dụng sức mạnh của Large Language Models (LLMs) để tăng tốc xây dựng workflow:
- Hiểu lý do tại sao kỹ nghệ ngữ cảnh (Context Engineering) lại quan trọng khi làm việc với LLMs.
- Sử dụng Kestra AI Copilot để viết luồng YAML nhanh chóng và chính xác.
- Tích hợp kiến trúc Retrieval Augmented Generation (RAG) trực tiếp vào đường ống dữ liệu.

**Điều kiện cần:**
- Đã hoàn thành các bài học trước trong Module 2.
- Kestra đang chạy ổn định ở máy local.
- Tài khoản Google Cloud có quyền truy cập Gemini API (có gói sử dụng miễn phí rất rộng rãi).

---

### 2.6 Nâng cao: Triển khai lên Cloud (Tùy chọn)
Hướng dẫn đưa hệ thống Kestra lên Google Cloud để vận hành liên tục và tự động đồng bộ workflows trực tiếp từ Git repository.

> [!NOTE]
> Khi commit workflows vào Git, tuyệt đối không đưa thông tin nhạy cảm (API keys, credentials) vào code. Hãy sử dụng [Secrets](https://go.kestra.io/de-zoomcamp/secret) và [KV Store](https://go.kestra.io/de-zoomcamp/kv-store) của Kestra.

**Tài liệu tham khảo:**
- [Cài đặt Kestra trên Google Cloud](https://go.kestra.io/de-zoomcamp/gcp-install)
- [Quy trình chuyển từ Môi trường Dev sang Môi trường Production](https://go.kestra.io/de-zoomcamp/dev-to-prod)
- [Tích hợp Git trong Kestra](https://go.kestra.io/de-zoomcamp/git)
- [Triển khai Flows tự động bằng GitHub Actions](https://go.kestra.io/de-zoomcamp/deploy-github-actions)

---

### 2.7 Tài nguyên & Mẹo xử lý sự cố (Troubleshooting)

- [Tài liệu chính thức Kestra Docs](https://go.kestra.io/de-zoomcamp/docs)
- [Thư viện mẫu Blueprints](https://go.kestra.io/de-zoomcamp/blueprints)
- Hơn 600 [Plugins mở rộng trong Kestra](https://go.kestra.io/de-zoomcamp/plugins)
- [GitHub Kestra](https://go.kestra.io/de-zoomcamp/github)
- [Cộng đồng Slack Kestra](https://go.kestra.io/de-zoomcamp/slack)
- [Danh sách video YouTube Module 2](https://go.kestra.io/de-zoomcamp/yt-playlist)

#### Các mẹo xử lý sự cố thường gặp:
Khi gặp vấn đề với Kestra trong Module 2, hãy chú ý cấu hình Docker image và port như sau:
- Sử dụng `image: kestra/kestra:v1.1` - cố định phiên bản để đảm bảo tính tái lập; **KHÔNG NÊN** dùng `kestra/kestra:develop` vì đây là bản phát triển có thể chứa lỗi chưa kiểm thử.
- Cố định PostgreSQL image ở phiên bản `postgres:18`.
- Nếu cổng `8080` bị chiếm bởi pgAdmin hoặc ứng dụng khác, hãy đổi cổng ánh xạ trong file `docker-compose.yml` sang `18080:8080` và truy cập Kestra Web UI tại `http://localhost:18080/`.
- Nếu cần khởi động lại sạch sẽ: chạy `docker-compose down -v` rồi khởi chạy lại bằng `docker-compose up -d`.

Nếu gặp lỗi đọc dữ liệu từ BigQuery dạng:
```
BigQueryError{reason=invalid, location=null, 
message=Error while reading table: kestra-sandbox.zooomcamp.yellow_tripdata_2020_01, 
error message: CSV table references column position 17, but line contains only 14 columns.; 
```
-> Nguyên nhân thường do file CSV bị thiếu cột ở các tháng khác nhau trong bộ dữ liệu gốc, cần kiểm tra lại định nghĩa schema hoặc xử lý chuẩn hóa ở bước nạp.
