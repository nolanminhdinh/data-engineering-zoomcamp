---
prev_url: 07-pgadmin.md
next_url: 09-docker-compose.md
---
# Đóng Gói Script Nạp Dữ Liệu Vào Docker (Dockerizing the Ingestion Script)

Bây giờ chúng ta sẽ đóng gói toàn bộ script nạp dữ liệu vào bên trong Docker Image để có thể chạy quy trình nạp dữ liệu ở bất kỳ máy chủ nào mà không cần cài đặt Python hay thư viện thủ công.

---

## 1. Cấu Trúc Dockerfile Hoàn Chỉnh

Tệp `pipeline/Dockerfile` định nghĩa việc đóng gói script như sau:

```dockerfile
# Sử dụng base image Python 3.13 slim nhẹ và tối ưu dung lượng
FROM python:3.13.11-slim

# Sao chép file thực thi uv từ image chính thức (kỹ thuật multi-stage build)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Khởi tạo thư mục làm việc bên trong container
WORKDIR /code

# Thêm môi trường ảo vào biến PATH
ENV PATH="/code/.venv/bin:$PATH"

# Sao chép các tệp quản lý phiên bản và khóa phụ thuộc trước (tối ưu Docker caching)
COPY pyproject.toml .python-version uv.lock ./

# Đồng bộ chính xác các phụ thuộc từ file khóa uv.lock (đảm bảo tính tái lập 100%)
RUN uv sync --locked

# Sao chép mã nguồn script nạp dữ liệu vào container
COPY ingest_data.py .

# Thiết lập lệnh mặc định khởi chạy script qua uv
ENTRYPOINT ["uv", "run", "python", "ingest_data.py"]
```

### Giải Thích Quy Trình Tối Ưu Của Dockerfile:

- `FROM python:3.13.11-slim`: Sử dụng image rút gọn giúp kích thước image nhẹ nhất có thể.
- `COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/`: Tận dụng trình quản lý gói siêu tốc `uv`.
- `WORKDIR /code`: Mọi lệnh tiếp theo đều được chạy trong thư mục `/code`.
- `COPY pyproject.toml ...`: Sao chép file cấu hình thư viện trước để Docker lưu vào cache layer. Khi chỉ sửa code Python `ingest_data.py`, Docker không phải tốn thời gian tải lại các thư viện lớn như pandas/sqlalchemy.
- `RUN uv sync --locked`: Khóa chặt các phiên bản thư viện đã kiểm thử.
- `ENTRYPOINT`: Khi container khởi chạy, nó tự động gọi script và sẵn sàng nhận các tham số bổ sung từ dòng lệnh bên ngoài.

---

## 2. Xây Dựng Docker Image (Build Image)

Di chuyển vào thư mục `pipeline` và build image:

```bash
cd pipeline
docker build -t taxi_ingest:v001 .
```

---

## 3. Khởi Chạy Nạp Dữ Liệu Qua Container

Để container nạp dữ liệu kết nối được vào database PostgreSQL, chúng ta **bắt buộc phải gắn container vào cùng mạng `pg-network`**:

```bash
docker run -it \
  --network=pg-network \
  taxi_ingest:v001 \
    --pg-user=root \
    --pg-pass=root \
    --pg-host=pgdatabase \
    --pg-port=5432 \
    --pg-db=ny_taxi \
    --target-table=yellow_taxi_trips
```

### Lưu Ý Quan Trọng:

* Cờ `--network=pg-network` giúp container phân giải được tên miền nội bộ của các container khác.
* Tham số `--pg-host` phải truyền vào tên container của PostgreSQL (`pgdatabase`), **không được** dùng `localhost` vì `localhost` bên trong container `taxi_ingest` sẽ trỏ về chính container đó chứ không phải máy chủ cơ sở dữ liệu.
* Khi chạy xong, bạn có thể mở pgAdmin hoặc `pgcli` để kiểm tra bảng `yellow_taxi_trips` đã chứa đầy đủ dữ liệu chuyến đi!
