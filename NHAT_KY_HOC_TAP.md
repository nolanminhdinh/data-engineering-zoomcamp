# 📓 Nhật Ký Học Tập Data Engineering Zoomcamp

> **Học viên:** Nolan Minh Dinh  
> **Ngày bắt đầu:** 08/10/2026  
> **Nhánh học tập:** `vietnamese`  
> **Mục tiêu:** Nắm vững nền tảng Data Engineering hiện đại, hoàn thành 7 modules thực hành và xây dựng đồ án tốt nghiệp (End-to-End Data Pipeline) hoàn chỉnh đưa vào Portfolio.

---

## 🗺️ Tổng Quan Lộ Trình Khóa Học (Curriculum Progress)

| Module | Tên Học Phần | Trạng Thái | Ngày Bắt Đầu | Ngày Hoàn Thành | Ghi Chú |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **01** | [Containerization & Infrastructure as Code](01-docker-terraform/README.md) | 🔄 **Đang học** | 08/10/2026 | ... | Docker, Postgres, Terraform, GCP |
| **02** | [Workflow Orchestration](02-workflow-orchestration/README.md) | ⏳ Chưa bắt đầu | ... | ... | Kestra, GCS, BigQuery, AI Copilot |
| **W1** | [Workshop: Data Ingestion](cohorts/2026/workshops/dlt.md) | ⏳ Chưa bắt đầu | ... | ... | dlt Hub, API Ingestion |
| **03** | [Data Warehousing](03-data-warehouse/README.md) | ⏳ Chưa bắt đầu | ... | ... | BigQuery, Partitioning, Clustering, ML |
| **04** | [Analytics Engineering](04-analytics-engineering/README.md) | ⏳ Chưa bắt đầu | ... | ... | dbt, DuckDB, Modeling, Star Schema |
| **05** | [Data Platforms](05-data-platforms/README.md) | ⏳ Chưa bắt đầu | ... | ... | Bruin CLI, Data Quality, MCP |
| **06** | [Batch Processing](06-batch/README.md) | ⏳ Chưa bắt đầu | ... | ... | Apache Spark, PySpark, Dataproc |
| **07** | [Streaming](07-streaming/README.md) | ⏳ Chưa bắt đầu | ... | ... | Kafka, Redpanda, PyFlink, Windowing |
| **Project** | [Đồ Án Tốt Nghiệp Cuối Khóa](projects/README.md) | ⏳ Chưa bắt đầu | ... | ... | End-to-End Pipeline & Dashboard |

---

## 🚀 Chi Tiết Tiến Độ Module 1: Docker & Terraform

### Danh sách các bài học (Checklist)
- [ ] **Bài 01**: [Giới thiệu về Docker](01-docker-terraform/01-introduction.md) *(Docker vs VM, Images, Containers, Volumes)*
- [ ] **Bài 02**: [Môi trường ảo và Data Pipeline](01-docker-terraform/02-virtual-environment.md) *(uv, pyproject.toml, Pandas, Parquet)*
- [ ] **Bài 03**: [Đóng gói Pipeline vào Docker](01-docker-terraform/03-dockerizing-pipeline.md) *(Dockerfile, Multi-stage build với uv)*
- [ ] **Bài 04**: [Khởi chạy PostgreSQL với Docker](01-docker-terraform/04-postgres-docker.md) *(Named Volume, Port 5432, pgcli)*
- [ ] **Bài 05**: [Bộ dữ liệu NY Taxi và Nạp dữ liệu](01-docker-terraform/05-data-ingestion.md) *(Jupyter, Dtype, Chunking nạp theo khối)*
- [ ] **Bài 06**: [Viết Script nạp dữ liệu độc lập](01-docker-terraform/06-ingestion-script.md) *(Click CLI, argparse, refactor code)*
- [ ] **Bài 07**: [Quản trị cơ sở dữ liệu với pgAdmin](01-docker-terraform/07-pgadmin.md) *(Docker Network, Web GUI localhost:8085)*
- [ ] **Bài 08**: [Đóng gói Script nạp dữ liệu](01-docker-terraform/08-dockerizing-ingestion.md) *(Kết nối container qua pg-network)*
- [ ] **Bài 09**: [Điều phối với Docker Compose](01-docker-terraform/09-docker-compose.md) *(docker-compose.yaml, lệnh up/down)*
- [ ] **Bài 10**: [Ôn tập kiến thức SQL thực chiến](01-docker-terraform/10-sql-refresher.md) *(Inner/Left Join, Group By, Data Quality)*
- [ ] **Bài 11**: [Dọn dẹp môi trường](01-docker-terraform/11-cleanup.md) *(Dọn dẹp container, image, volume)*
- [ ] **Bài 12**: [Tổng quan về Terraform](01-docker-terraform/12-terraform-overview.md) *(IaC, Plan, Apply, Destroy, tfstate)*
- [ ] **Bài 13**: [Tổng quan Google Cloud Platform](01-docker-terraform/13-gcp-overview.md) *(GCP Service Account, IAM, GCS, BigQuery)*
- [ ] **Bài tập về nhà (Homework 1)**: Hoàn thành và nộp đáp án.

---

## 📝 Nhật Ký Học Hàng Ngày (Daily Log)

### Ngày 1: 08/10/2026
* **Mục tiêu hôm nay:** Bắt đầu Module 1 - Học từ Bài 01 đến Bài 04 (Làm quen với Docker, Môi trường ảo `uv`, và khởi chạy PostgreSQL).
* **Nội dung đã học:**
  - Thiết lập môi trường học tập tiếng Việt, đồng bộ repository mới nhất từ DataTalksClub.
  - Hiểu bản chất Containerization và ưu điểm của Docker so với máy ảo thông thường (nhẹ, cô lập, nhất quán môi trường).
  - Khái niệm tính phi trạng thái (Stateless) của Container và cách dùng Volume để lưu trữ dữ liệu bền vững.
* **Lệnh quan trọng đã thực hành:**
  ```bash
  # Kiểm tra Docker
  docker --version
  
  # Khởi tạo project Python siêu tốc với uv
  uv init --python=3.13
  uv add pandas pyarrow sqlalchemy "psycopg[binary,pool]"
  
  # Khởi chạy PostgreSQL trên Docker với named volume
  docker run -it --rm -e POSTGRES_USER=root -e POSTGRES_PASSWORD=root -e POSTGRES_DB=ny_taxi -v ny_taxi_postgres_data:/var/lib/postgresql -p 5432:5432 postgres:18
  ```
* **Khó khăn / Thắc mắc gặp phải:**
  - ... *(Ghi lại các lỗi gặp phải trong lúc làm và cách đã khắc phục tại đây)*
* **Kế hoạch ngày tiếp theo:**
  - Hoàn thành bài 05, 06, 07: Viết script nạp dữ liệu NY Taxi theo khối (chunking) và kết nối pgAdmin.

---

### Mẫu Ghi Chép Cho Các Ngày Tiếp Theo:
```markdown
### Ngày ... : .../.../2026
* **Mục tiêu hôm nay:** ...
* **Nội dung đã học:** ...
* **Lệnh / Mã nguồn đã thực hành:** ...
* **Lỗi gặp phải & Cách giải quyết:** ...
* **Kế hoạch tiếp theo:** ...
```

---

## 💡 Bảng Thuật Ngữ Cần Nhớ Nhanh Trong Module 1
* **Image vs Container:** Image là bản thiết kế tĩnh (bất biến), Container là phiên bản đang chạy trong bộ nhớ.
* **Volume:** Cơ chế lưu trữ dữ liệu độc lập ngoài vòng đời của container (xóa container không bị mất dữ liệu database).
* **Docker Network:** Mạng ảo giúp các container nói chuyện với nhau thông qua tên container (`pgdatabase`, `pgadmin`).
* **Chunking:** Đọc dữ liệu theo từng khối nhỏ (ví dụ 100,000 dòng/lần) để tránh lỗi tràn RAM (Out-of-Memory).
* **IaC (Infrastructure as Code):** Quản lý hạ tầng đám mây hoàn toàn bằng file code mã nguồn với Terraform.
