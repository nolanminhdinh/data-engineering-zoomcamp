---
prev_url: 02-virtual-environment.md
next_url: 04-postgres-docker.md
---
# Đóng Gói Đường Ống Vào Docker (Dockerizing the Pipeline)

Bây giờ chúng ta sẽ đóng gói (containerize) script Python vừa viết vào bên trong một Docker Image để có thể triển khai ở bất kỳ môi trường nào. Hãy tạo tệp `Dockerfile` với nội dung dưới đây:

---

## 1. Viết Dockerfile Đơn Giản Với `pip`

```dockerfile
# Base image nền tảng chứa Python
FROM python:3.13.11-slim

# Cài đặt các thư viện phụ thuộc: pandas và pyarrow
RUN pip install pandas pyarrow

# Thiết lập thư mục làm việc bên trong container
WORKDIR /app

# Sao chép script từ máy thật vào thư mục /app trong container
COPY pipeline.py pipeline.py

# Khai báo lệnh mặc định sẽ chạy ngay khi container khởi động
ENTRYPOINT ["python", "pipeline.py"]
```

### Giải Thích Các Chỉ Lệnh Cốt Lõi:

- `FROM`: Image nền tảng ban đầu (ở đây dùng Python 3.13 bản rút gọn `-slim` để giảm dung lượng image).
- `RUN`: Thực thi các lệnh cài đặt trong quá trình xây dựng image (build time).
- `WORKDIR`: Thiết lập thư mục làm việc mặc định bên trong container.
- `COPY`: Sao chép tệp từ máy thật (host) vào trong container. Tên đầu là nguồn, tên sau là đích.
- `ENTRYPOINT`: Lệnh mặc định sẽ được thực thi khi container được chạy.

### Xây Dựng Và Chạy Container (Build and Run)

Tiến hành build Docker image từ thư mục hiện tại:

```bash
docker build -t test:pandas .
```

* Image mới tạo sẽ có tên là `test` với tag là `pandas` (`test:pandas`). Nếu không chỉ định tag, Docker mặc định gán là `latest`. Dấu chấm `.` ở cuối đại diện cho đường dẫn build context hiện tại.

Khởi chạy container và truyền tham số ngày vào đường ống:

```bash
docker run -it test:pandas 10
```

Bạn sẽ nhận được kết quả in ra tương tự như khi bạn chạy script trên máy thật, nhưng lần này toàn bộ code và thư viện đều nằm trọn vẹn trong một container hoàn toàn cô lập!

> [!NOTE]
> Các hướng dẫn này yêu cầu tệp `pipeline.py` và `Dockerfile` nằm cùng một thư mục và lệnh `docker` được chạy từ chính thư mục đó.

---

## 2. Viết Dockerfile Hiện Đại Tối Ưu Với `uv`

Trong các hệ thống thực tế chuẩn công nghiệp, chúng ta nên sử dụng cơ chế multi-stage build kết hợp file khóa phiên bản `uv.lock` để đảm bảo tính tái lập 100% và tăng tốc bộ nhớ đệm (caching layers):

```dockerfile
# Sử dụng base image Python 3.13 slim nhẹ nhất
FROM python:3.13.10-slim

# Sao chép trực tiếp file thực thi uv từ image chính thức của Astral (multi-stage pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Thiết lập thư mục làm việc
WORKDIR /app

# Thêm đường dẫn môi trường ảo vào biến PATH để sử dụng trực tiếp các gói đã cài
ENV PATH="/app/.venv/bin:$PATH"

# Sao chép các tệp quản lý phụ thuộc trước (tối ưu cơ chế cache layer của Docker)
COPY "pyproject.toml" "uv.lock" ".python-version" ./

# Đồng bộ chính xác các phụ thuộc dựa trên file lock (đảm bảo môi trường nhất quán tuyệt đối)
RUN uv sync --locked

# Sao chép mã nguồn ứng dụng
COPY pipeline.py pipeline.py

# Điểm vào thực thi
ENTRYPOINT ["uv", "run", "python", "pipeline.py"]
```
