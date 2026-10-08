---
prev_url: 05-data-ingestion.md
next_url: 07-pgadmin.md
---
# Xây Dựng Script Nạp Dữ Liệu Tự Động (Creating the Data Ingestion Script)

Sau khi đã thử nghiệm thành công quy trình nạp dữ liệu trên Jupyter Notebook, bước tiếp theo là chuyển đổi (refactor) logic này thành một script Python độc lập có khả năng nhận tham số dòng lệnh (CLI arguments) để phục vụ tự động hóa và đóng gói vào container.

---

## 1. Chuyển Đổi Từ Notebook Sang Python Script

Bạn có thể xuất notebook thành tệp `.py` bằng lệnh:

```bash
uv run jupyter nbconvert --to=script notebook.ipynb
mv notebook.py ingest_data.py
```

---

## 2. Cấu Trúc Script Nạp Dữ Liệu Hoàn Chỉnh

Mã nguồn đầy đủ nằm trong thư mục `pipeline/`. Dưới đây là các phần cốt lõi:

```python
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

# Định nghĩa trước kiểu dữ liệu để đảm bảo an toàn bộ nhớ và tính toàn vẹn
dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]
```

---

## 3. Tích Hợp Giao Diện Dòng Lệnh Với Thư Viện `click`

Chúng ta sử dụng thư viện `click` để biến script thành một công cụ dòng lệnh (CLI tool) linh hoạt, cho phép truyền các thông số kết nối cơ sở dữ liệu và bảng đích từ bên ngoài:

```python
import click

@click.command()
@click.option('--pg-user', default='root', help='Tên người dùng PostgreSQL')
@click.option('--pg-pass', default='root', help='Mật khẩu PostgreSQL')
@click.option('--pg-host', default='localhost', help='Địa chỉ máy chủ PostgreSQL')
@click.option('--pg-port', default=5432, type=int, help='Cổng kết nối PostgreSQL')
@click.option('--pg-db', default='ny_taxi', help='Tên cơ sở dữ liệu')
@click.option('--target-table', default='yellow_taxi_data', help='Tên bảng lưu trữ')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table):
    # Toàn bộ logic kết nối database và nạp dữ liệu theo khối (chunking) tại đây
    pass
```

---

## 4. Thực Thi Script Nạp Dữ Liệu

Script đọc dữ liệu theo từng khối (chunk size = 100,000 dòng) giúp xử lý mượt mà ngay cả khi chạy trên máy chủ có cấu hình RAM khiêm tốn.

Ví dụ lệnh chạy thực tế:

```bash
uv run python ingest_data.py \
  --pg-user=root \
  --pg-pass=root \
  --pg-host=localhost \
  --pg-port=5432 \
  --pg-db=ny_taxi \
  --target-table=yellow_taxi_trips
```
