---
prev_url: 04-postgres-docker.md
next_url: 06-ingestion-script.md
---
# Bộ Dữ Liệu NY Taxi Và Quy Trình Nạp Dữ Liệu (NY Taxi Dataset & Data Ingestion)

Trong bài học này, chúng ta sẽ sử dụng Jupyter Notebook để khám phá bộ dữ liệu chuyến đi taxi thành phố New York (NYC Taxi), đọc tệp dữ liệu dạng nén `.csv.gz`, chuẩn hóa kiểu dữ liệu, và thực hiện nạp dữ liệu (data ingestion) vào cơ sở dữ liệu PostgreSQL theo từng khối (chunks) để tránh tràn bộ nhớ RAM.

---

## 1. Thiết Lập Môi Trường Jupyter Notebook

Cài đặt Jupyter vào dự án bằng công cụ `uv`:

```bash
uv add --dev jupyter
```

Khởi động Jupyter Notebook:

```bash
uv run jupyter notebook
```

Trình duyệt sẽ tự động mở giao diện làm việc của Jupyter. Hãy tạo một notebook mới mang tên `notebook.ipynb`.

---

## 2. Tìm Hiểu Về Bộ Dữ Liệu NYC Taxi

Chúng ta sử dụng dữ liệu thực tế từ [Website Dữ liệu Chuyến đi của NYC TLC](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page).

Cụ thể, chúng ta sử dụng tệp: [Yellow taxi trip records CSV tháng 01/2021](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz).

> [!NOTE]
> Mặc dù dữ liệu thực tế ngày nay thường được lưu ở định dạng Parquet, trong bài thực hành này chúng ta sử dụng định dạng CSV để rèn luyện kỹ năng tiền xử lý, kiểm soát kiểu dữ liệu và chia khối (chunking) trong đường ống nạp dữ liệu.  
> Bạn có thể tra cứu ý nghĩa từng cột trong [Từ điển dữ liệu NYC Taxi (Data Dictionary)](https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf).

---

## 3. Khám Phá Dữ Liệu Ban Đầu (Data Exploration)

Trong notebook, hãy chạy đoạn mã sau để đọc 100 dòng đầu tiên:

```python
import pandas as pd

# Đường dẫn tải dữ liệu
prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
df = pd.read_csv(prefix + 'yellow_tripdata_2021-01.csv.gz', nrows=100)

# Hiển thị các dòng đầu
df.head()

# Kiểm tra kiểu dữ liệu các cột
df.dtypes

# Kiểm tra kích thước DataFrame
df.shape
```

### Xử Lý Kiểu Dữ Liệu (Data Types)

Khi đọc toàn bộ tệp CSV lớn, Pandas có thể đưa ra cảnh báo kiểu dữ liệu không đồng nhất (`DtypeWarning: Columns (6) have mixed types`). Để đảm bảo tính toàn vẹn của dữ liệu và tối ưu bộ nhớ, chúng ta cần chủ động định nghĩa trước từ điển kiểu dữ liệu (`dtype`) và danh sách cột thời gian (`parse_dates`):

```python
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

df = pd.read_csv(
    prefix + 'yellow_tripdata_2021-01.csv.gz',
    nrows=100,
    dtype=dtype,
    parse_dates=parse_dates
)
```

---

## 4. Nạp Dữ Liệu Vào PostgreSQL (Ingesting to Postgres)

Quy trình nạp dữ liệu gồm 4 bước chính:
1. Tải và đọc tệp CSV theo từng khối (chunks).
2. Chuyển đổi định dạng các cột ngày giờ.
3. Tạo kết nối tới cơ sở dữ liệu PostgreSQL qua thư viện SQLAlchemy.
4. Ghi dữ liệu vào bảng trong cơ sở dữ liệu.

### Cài Đặt Thư Viện Kết Nối SQLAlchemy và Driver

```bash
uv add sqlalchemy "psycopg[binary,pool]"
```

### Khởi Tạo Kết Nối Cơ Sở Dữ Liệu (Engine)

```python
from sqlalchemy import create_engine

# Chuỗi kết nối dạng: postgresql+driver://user:password@host:port/database
engine = create_engine('postgresql+psycopg://root:root@localhost:5432/ny_taxi')
```

### Xem Cú Pháp DDL Tự Động Của Bảng (Schema DDL)

Pandas hỗ trợ sinh câu lệnh SQL DDL tự động tương ứng với DataFrame:

```python
print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))
```

Kết quả sinh ra cấu trúc bảng:

```sql
CREATE TABLE yellow_taxi_data (
    "VendorID" BIGINT,
    tpep_pickup_datetime TIMESTAMP WITHOUT TIME ZONE,
    tpep_dropoff_datetime TIMESTAMP WITHOUT TIME ZONE,
    passenger_count BIGINT,
    trip_distance FLOAT(53),
    "RatecodeID" BIGINT,
    store_and_fwd_flag TEXT,
    "PULocationID" BIGINT,
    "DOLocationID" BIGINT,
    payment_type BIGINT,
    fare_amount FLOAT(53),
    extra FLOAT(53),
    mta_tax FLOAT(53),
    tip_amount FLOAT(53),
    tolls_amount FLOAT(53),
    improvement_surcharge FLOAT(53),
    total_amount FLOAT(53),
    congestion_surcharge FLOAT(53)
)
```

### Tạo Bảng Rỗng Ban Đầu

Dùng cú pháp `df.head(n=0)` để chỉ tạo cấu trúc bảng (schema) mà không chèn dữ liệu:

```python
df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')
```

---

## 5. Nạp Dữ Liệu Theo Từng Khối (Chunking Ingestion)

Trong thực tế, các tệp dữ liệu có thể nặng hàng chục Gigabyte, việc đọc một lần toàn bộ tệp vào RAM sẽ dẫn đến lỗi tràn bộ nhớ (Out-of-Memory - OOM). Do đó, kỹ thuật chuẩn trong Data Engineering là sử dụng một **trình lặp (Iterator)** với tham số `chunksize`:

```python
df_iter = pd.read_csv(
    prefix + 'yellow_tripdata_2021-01.csv.gz',
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=100000  # Mỗi lần đọc 100,000 dòng
)
```

### Vòng Lặp Nạp Toàn Diện (Complete Ingestion Loop)

Đoạn mã sau đọc khối đầu tiên để tạo bảng mới (nếu chưa có), sau đó liên tục ghi thêm (`if_exists='append'`) từng khối vào bảng:

```python
first = True

for df_chunk in df_iter:
    if first:
        # Tạo bảng mới rỗng (ghi đè nếu đã tồn tại)
        df_chunk.head(0).to_sql(
            name="yellow_taxi_data",
            con=engine,
            if_exists="replace"
        )
        first = False
        print("Đã tạo bảng yellow_taxi_data thành công.")

    # Ghi thêm từng khối vào cơ sở dữ liệu
    df_chunk.to_sql(
        name="yellow_taxi_data",
        con=engine,
        if_exists="append"
    )

    print(f"Đã nạp thành công: {len(df_chunk)} dòng.")
```

### Bổ Sung Thanh Tiến Trình (Progress Bar với `tqdm`)

Để theo dõi trực quan tiến độ nạp dữ liệu:

```bash
uv add tqdm
```

Áp dụng trong code:

```python
from tqdm.auto import tqdm

for df_chunk in tqdm(df_iter):
    df_chunk.to_sql(
        name="yellow_taxi_data",
        con=engine,
        if_exists="append"
    )
```

---

## 6. Kiểm Tra Dữ Liệu Đã Nạp

Mở một cửa sổ dòng lệnh và kết nối vào PostgreSQL bằng `pgcli`:

```bash
uv run pgcli -h localhost -p 5432 -u root -d ny_taxi
```

Chạy câu lệnh kiểm tra số lượng bản ghi đã được nạp:

```sql
SELECT count(1) FROM yellow_taxi_data;
```
