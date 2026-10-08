---
prev_url: 08-dockerizing-ingestion.md
next_url: 10-sql-refresher.md
---
# Điều Phối Đa Container Với Docker Compose (Docker Compose)

`docker compose` cho phép chúng ta định nghĩa và khởi chạy đồng thời nhiều containers chỉ bằng một tệp cấu hình duy nhất, giúp loại bỏ hoàn toàn sự phức tạp khi phải gõ nhiều lệnh `docker run` dài dòng riêng lẻ.

Docker Compose sử dụng định dạng tệp YAML. Dưới đây là nội dung tệp `docker-compose.yaml`:

```yaml
services:
  pgdatabase:
    image: postgres:18
    environment:
      POSTGRES_USER: "root"
      POSTGRES_PASSWORD: "root"
      POSTGRES_DB: "ny_taxi"
    volumes:
      - "ny_taxi_postgres_data:/var/lib/postgresql"
    ports:
      - "5432:5432"

  pgadmin:
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: "admin@admin.com"
      PGADMIN_DEFAULT_PASSWORD: "root"
    volumes:
      - "pgadmin_data:/var/lib/pgadmin"
    ports:
      - "8085:80"

volumes:
  ny_taxi_postgres_data:
  pgadmin_data:
```

### Giải Thích Cấu Trúc:

* **Tự động tạo mạng ảo (Network)**: Bạn không cần phải tạo mạng ảo bằng tay nữa. Docker Compose tự động tạo một mạng mặc định cho toàn bộ dự án. Tất cả các dịch vụ (services) khai báo trong file sẽ tự động nằm chung mạng và nhận diện được nhau theo tên dịch vụ (`pgdatabase` và `pgadmin`).
* Toàn bộ cấu hình biến môi trường (`environment`), ổ đĩa (`volumes`), và cổng mạng (`ports`) đều được khai báo rõ ràng, chuẩn hóa theo cú pháp YAML.

---

## 1. Khởi Chạy Các Dịch Vụ Với Docker Compose

Hãy đảm bảo bạn đã tắt các container chạy thử trước đó, sau đó đứng tại thư mục chứa file `docker-compose.yaml` và chạy lệnh:

```bash
docker compose up
```

### Chế Độ Chạy Ngầm (Detached Mode)

Để giải phóng terminal và chạy toàn bộ dịch vụ dưới nền (background):

```bash
docker compose up -d
```

---

## 2. Dừng Và Xóa Các Dịch Vụ

Nếu chạy ở chế độ thông thường, bạn nhấn tổ hợp phím `Ctrl + C` để dừng. Lệnh chuẩn mực để dừng và dọn sạch tài nguyên:

```bash
docker compose down
```

---

## 3. Các Lệnh Tiện Ích Thường Dùng

```bash
# Xem toàn bộ nhật ký (logs) của các container đang chạy
docker compose logs

# Dừng hệ thống và xóa sạch cả các named volumes (xóa toàn bộ dữ liệu database)
docker compose down -v
```

### Lợi Ích Lớn Của Docker Compose:

- Khởi chạy toàn bộ hệ thống chỉ với một lệnh duy nhất (`docker compose up`).
- Quản lý mạng nội bộ hoàn toàn tự động.
- Cấu hình hạ tầng mang tính khai báo (Declarative Infrastructure), dễ lưu trữ và theo dõi thay đổi qua Git.

---

## 4. Chạy Script Nạp Dữ Liệu Kết Hợp Với Mạng Của Docker Compose

Khi bạn khởi chạy PostgreSQL và pgAdmin bằng Docker Compose, Docker sẽ tự động tạo một mạng ảo có tên theo tiền tố thư mục, ví dụ: `pipeline_default` hoặc `01-docker-terraform_default`.

Kiểm tra tên mạng Docker Compose vừa tạo:

```bash
docker network ls
```

Sau đó, chạy container nạp dữ liệu trỏ vào mạng này:

```bash
docker run -it --rm \
  --network=pipeline_default \
  taxi_ingest:v001 \
    --pg-user=root \
    --pg-pass=root \
    --pg-host=pgdatabase \
    --pg-port=5432 \
    --pg-db=ny_taxi \
    --target-table=yellow_taxi_trips
```
