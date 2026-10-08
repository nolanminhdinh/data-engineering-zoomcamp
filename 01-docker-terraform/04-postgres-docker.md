---
prev_url: 03-dockerizing-pipeline.md
next_url: 05-data-ingestion.md
---
# Khởi Chạy PostgreSQL Với Docker (Running PostgreSQL with Docker)

Bây giờ chúng ta sẽ bước vào các tác vụ Kỹ thuật Dữ liệu thực chiến. Chúng ta sẽ sử dụng hệ quản trị cơ sở dữ liệu quan hệ **PostgreSQL**.

Với Docker, bạn không cần phải cài đặt PostgreSQL trực tiếp lên hệ điều hành của mình. Bạn chỉ cần truyền các **biến môi trường (environment variables)** để cấu hình tài khoản, đồng thời gắn một **volume** để lưu trữ dữ liệu bền vững (persistent data).

---

## Khởi Chạy PostgreSQL Trong Container

Chạy lệnh Docker sau để khởi động một cơ sở dữ liệu PostgreSQL độc lập:

```bash
docker run -it --rm \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql \
  -p 5432:5432 \
  postgres:18
```

### Giải Thích Các Tham Số Cấu Hình:

* `-e`: Thiết lập các biến môi trường cho container:
  * `POSTGRES_USER="root"`: Tên người dùng quản trị.
  * `POSTGRES_PASSWORD="root"`: Mật khẩu truy cập.
  * `POSTGRES_DB="ny_taxi"`: Tên cơ sở dữ liệu khởi tạo mặc định.
* `-v ny_taxi_postgres_data:/var/lib/postgresql`: Tạo một **Named Volume** (ổ đĩa có tên):
  * Docker tự động quản lý volume này trên ổ đĩa hệ thống.
  * Dữ liệu trong database sẽ **không bị mất** ngay cả khi container bị tắt hoặc xóa.
* `-p 5432:5432`: Ánh xạ cổng (port forwarding) `5432` từ container ra cổng `5432` của máy thật (host). Nhờ đó các công cụ bên ngoài máy thật có thể kết nối vào qua `localhost:5432`.
* `postgres:18`: Phiên bản PostgreSQL 18 chuẩn.

---

### Phương Pháp Thay Thế: Sử Dụng Thư Mục Máy Thật (Bind Mount)

Nếu bạn muốn trực tiếp nhìn thấy và quản lý thư mục dữ liệu trên máy thật:

```bash
mkdir ny_taxi_postgres_data

docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql \
  -p 5432:5432 \
  postgres:18
```

### So Sánh Named Volume và Bind Mount:

* **Named volume** (`tên_volume:/path`): Do Docker tự động quản lý tối ưu hiệu năng trên ổ cứng. Khuyên dùng trong đa số trường hợp cơ sở dữ liệu.
* **Bind mount** (`/đường_dẫn_máy_thật:/container/path`): Ánh xạ trực tiếp tới một thư mục cụ thể trên máy tính của bạn, giúp bạn dễ dàng xem hoặc backup file trực tiếp.

---

## Kết Nối Tới PostgreSQL Bằng CLI (`pgcli`)

Khi container đang chạy, chúng ta có thể tương tác với cơ sở dữ liệu bằng công cụ dòng lệnh thông minh [pgcli](https://www.pgcli.com/) (có tính năng gợi ý cú pháp tự động và tô màu trực quan).

Cài đặt `pgcli` qua `uv`:

```bash
uv add --dev pgcli
```

* Cờ `--dev` đánh dấu đây là công cụ phục vụ môi trường phát triển (development dependency), sẽ được ghi vào mục `[dependency-groups]` của `pyproject.toml` thay vì phụ thuộc production.

Kết nối vào cơ sở dữ liệu:

```bash
uv run pgcli -h localhost -p 5432 -u root -d ny_taxi
```

* `uv run`: Chạy lệnh trong bối cảnh môi trường ảo của dự án.
* `-h localhost`: Địa chỉ máy chủ (đang chạy local).
* `-p 5432`: Cổng kết nối.
* `-u root`: Tên đăng nhập.
* `-d ny_taxi`: Tên cơ sở dữ liệu cần kết nối.
* Khi terminal hỏi mật khẩu, nhập `root`.

---

## Các Câu Lệnh SQL Cơ Bản (Basic SQL Commands)

Sau khi vào giao diện tương tác của `pgcli`, hãy thử thực thi một số câu lệnh:

```sql
-- Liệt kê danh sách các bảng trong database
\dt

-- Tạo một bảng thử nghiệm
CREATE TABLE test (id INTEGER, name VARCHAR(50));

-- Chèn dữ liệu mẫu
INSERT INTO test VALUES (1, 'Hello Docker');

-- Truy vấn dữ liệu
SELECT * FROM test;

-- Thoát khỏi pgcli
\q
```
