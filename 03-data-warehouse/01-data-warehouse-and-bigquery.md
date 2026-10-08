---
video_url: https://www.youtube.com/watch?v=jrHljAoD6nM
prev_url: ../02-workflow-orchestration/18-additional-resources.md
next_url: 02-partitioning-vs-clustering.md
---
# Kho Dữ Liệu Và Google BigQuery (Data Warehouse & BigQuery)

Trong bài học này, chúng ta sẽ tìm hiểu tổng quan về **Kho dữ liệu (Data Warehouse)** và nghiên cứu điển hình với **Google BigQuery**: sự khác biệt bản chất giữa cơ sở dữ liệu phân tích (OLAP) và cơ sở dữ liệu giao dịch (OLTP), kiến trúc phân tầng của một kho dữ liệu hiện đại, và trải nghiệm thực hành trực tiếp với BigQuery — giao diện làm việc, tập dữ liệu công khai (public datasets), bảng ngoại vi (external tables), mô hình chi phí, và hai kỹ thuật tối ưu hóa cốt lõi: **Phân vùng dữ liệu (Partitioning)** và **Gom cụm dữ liệu (Clustering)**.

---

## 1. So Sánh OLTP và OLAP (OLTP vs OLAP)

Hệ thống cơ sở dữ liệu được chia làm hai trường phái chính dựa trên mục đích sử dụng nghiệp vụ:

* **OLTP (Online Transaction Processing - Xử lý giao dịch trực tuyến)**: Là loại cơ sở dữ liệu vận hành đứng sau các ứng dụng backend hàng ngày. Bạn thực hiện nhiều câu truy vấn SQL ngắn gom lại trong một giao dịch (transaction) tuân thủ tính toàn vẹn ACID, và có thể khôi phục (rollback) nếu một thao tác thất bại.  
  *Ví dụ điển hình:* Hệ thống thương mại điện tử — khi khách đặt hàng: tạo đơn hàng, trừ tiền thanh toán, và giảm số lượng tồn kho phải đồng thời thành công hoặc cùng bị hủy bỏ.
* **OLAP (Online Analytical Processing - Xử lý phân tích trực tuyến)**: Là loại cơ sở dữ liệu được thiết kế chuyên biệt cho việc tiếp nhận khối lượng dữ liệu khổng lồ và khám phá những thông tin ẩn sâu (insights). Được sử dụng chủ yếu bởi các Chuyên viên Phân tích Dữ liệu (Data Analysts) và Nhà Khoa học Dữ liệu (Data Scientists).

Hai trường phái này khác nhau ở hầu hết mọi góc độ:

- Trong **OLTP**, các thao tác cập nhật diễn ra liên tục, tức thì nhưng với kích thước dữ liệu rất nhỏ (từng bản ghi). Trong **OLAP**, dữ liệu được nạp làm mới định kỳ theo các mẻ lớn (batch), và dung lượng dữ liệu tổng thể lớn hơn gấp nhiều lần.
- Cơ sở dữ liệu **OLTP** được thiết kế **Chuẩn hóa (Normalized - dạng 3NF)** để tối ưu tính toàn vẹn và tốc độ ghi. Cơ sở dữ liệu **OLAP** được thiết kế **Phi chuẩn hóa (Denormalized - Star Schema, Snowflake Schema)** để tối ưu tốc độ đọc và phân tích.
- **OLTP** phục vụ người dùng cuối (khách hàng, nhân viên bán hàng). **OLAP** phục vụ người ra quyết định (Business Analysts, Data Scientists, ban giám đốc).

| Tiêu chí so sánh | Hệ thống OLTP | Hệ thống OLAP |
| :--- | :--- | :--- |
| **Mục đích chính** | Điều khiển và thực thi các nghiệp vụ kinh doanh cốt lõi theo thời gian thực | Hoạch định chiến lược, phân tích dữ liệu lớn, hỗ trợ ra quyết định kinh doanh |
| **Cơ chế cập nhật** | Các thao tác ghi/sửa ngắn, cực nhanh do người dùng kích hoạt | Làm mới định kỳ bằng các tác vụ xử lý theo lô (batch jobs) chạy dài |
| **Thiết kế cơ sở dữ liệu** | Chuẩn hóa dữ liệu (Normalized) để tránh trùng lặp dữ liệu và ghi nhanh | Phi chuẩn hóa (Denormalized) tối ưu hóa truy vấn đọc và tổng hợp |
| **Dung lượng lưu trữ** | Thường vừa và nhỏ nếu dữ liệu lịch sử được lưu trữ định kỳ | Thường rất lớn (hàng Terabyte đến Petabyte) do tổng hợp lịch sử dài hạn |

---

## 2. Kho Dữ Liệu Là Gì? (What is a Data Warehouse?)

**Kho dữ liệu (Data Warehouse)** là giải pháp lưu trữ tập trung phục vụ mục đích phân tích (OLAP) và xây dựng báo cáo phân tích kinh doanh (Business Intelligence - BI).

Một kho dữ liệu điển hình bao gồm: Dữ liệu thô (raw data), siêu dữ liệu (metadata) và dữ liệu tổng hợp (summary data). Hệ thống tiếp nhận từ nhiều nguồn dữ liệu khác nhau (hệ thống vận hành, tệp tin phẳng CSV/JSON, cơ sở dữ liệu OLTP) thông qua một vùng đệm trung gian (Staging Area), sau đó chuyển đổi và nạp vào Kho dữ liệu trung tâm.

Ở đầu ra, dữ liệu từ Data Warehouse có thể được phân tách tiếp thành các **Data Marts**: các phân vùng nhỏ phục vụ các phòng ban chuyên trách cụ thể như mua hàng, bán hàng, kho vận.  
- Đối với các Analyst, làm việc qua Data Marts là môi trường lý tưởng nhất vì dữ liệu đã được làm sạch và mô hình hóa gọn gàng.  
- Đối với các Data Scientist, việc truy vấn trực tiếp dữ liệu thô (raw data) trong Data Warehouse lại mang lại nhiều giá trị khám phá hơn. Một Kho dữ liệu chuẩn mực đáp ứng tốt cả hai nhu cầu này.

![Kiến trúc Data Warehouse: Sources, Staging Area, Data Warehouse, Data Marts, Users](images/01-data-warehouse-and-bigquery-02-data-warehouse-diagram.png)

---

## 3. Tổng Quan Về Google BigQuery

**BigQuery** là giải pháp Kho dữ liệu đám mây của Google, và ưu điểm vượt trội nhất của nó là kiến trúc **Serverless**: Bạn không cần phải cài đặt phần mềm cơ sở dữ liệu, không cần quản trị máy chủ, không cần cấu hình ổ đĩa hay cụm máy ảo.

Điều này loại bỏ hoàn toàn gánh nặng vận hành hạ tầng thường ngốn nhiều tháng trời của doanh nghiệp. BigQuery cung cấp cả phần mềm lẫn hạ tầng với khả năng tự động mở rộng (scalability) và tính sẵn sàng cao (high availability). Bạn có thể bắt đầu với vài Megabyte và mở rộng lên hàng Petabyte mà không gặp bất kỳ trở ngại nào.

### Các Tính Năng Nổi Bật Tích Hợp Sẵn:
- **BigQuery ML**: Huấn luyện và dự đoán mô hình Machine Learning trực tiếp bằng câu lệnh SQL tiêu chuẩn.
- **Dữ liệu Không gian Địa lý (Geospatial Data)**: Hỗ trợ các hàm phân tích bản đồ GIS mạnh mẽ.
- **Tối ưu hóa Truy vấn BI**: Tích hợp chặt chẽ với Looker Studio và các công cụ trực quan hóa dữ liệu.

### Tách Biệt Tính Toán Và Lưu Trữ (Separation of Compute and Storage):
Trong các hệ thống máy chủ truyền thống, bộ xử lý (CPU/RAM) và ổ cứng gắn liền trong một cỗ máy, khi dữ liệu tăng thì bắt buộc phải nâng cấp toàn bộ máy tính rất tốn kém. BigQuery tách rời hoàn toàn động cơ tính toán (Compute Engine - Dremel) khỏi tầng lưu trữ (Storage - Colossus). Bạn chỉ trả tiền cho lượng dữ liệu lưu trữ thực tế và lượng dữ liệu được quét khi chạy câu lệnh.

---

## 4. Mô Hình Chi Phí Trên BigQuery (BigQuery Pricing)

BigQuery có hai mô hình tính phí chính:

1. **Tính phí theo dung lượng quét (On-demand pricing)**: Tính tiền dựa trên khối lượng dữ liệu bạn quét qua khi chạy truy vấn: mỗi Terabyte (TB) dữ liệu được quét có giá khoảng $5.
2. **Tính phí cố định (Flat rate / Capacity-based pricing)**: Dựa trên số lượng slots (đơn vị năng lực tính toán của BigQuery) đăng ký trước. Gói 100 slots có giá khoảng $2,000/tháng (tương đương với khoảng 400 TB dữ liệu quét theo gói On-demand). Do đó mô hình này chỉ phù hợp với các doanh nghiệp lớn xử lý thường xuyên trên 200 TB dữ liệu mỗi tháng.

---

## 5. Tập Dữ Liệu Công Khai (Public Datasets)

BigQuery tích hợp sẵn hàng ngàn bộ dữ liệu mở công cộng (Open-source Public Data) cho phép bạn truy vấn thực hành ngay lập tức mà không cần tự tải lên.

Ví dụ: Bộ dữ liệu các trạm xe đạp Citi Bike tại New York. Bạn có thể tìm kiếm bảng `citibike_stations` và thực hiện truy vấn:

```sql
SELECT
    station_id,
    name
FROM bigquery-public-data.new_york_citibike.citibike_stations
LIMIT 100;
```

---

## 6. Bảng Ngoại Vi (External Tables)

Trong module này, chúng ta sử dụng dữ liệu chuyến đi taxi NYC đã được tải lên Google Cloud Storage (GCS). BigQuery cho phép bạn tạo một **Bảng Ngoại Vi (External Table)** trỏ trực tiếp vào các tệp này: Dữ liệu thực tế vẫn nằm trên Cloud Storage, BigQuery chỉ lưu giữ Siêu dữ liệu (Metadata):

Cấu trúc phân cấp của BigQuery: `Project` → `Dataset` → `Table`.

```sql
CREATE OR REPLACE EXTERNAL TABLE `taxi-rides-ny.nytaxi.external_yellow_tripdata`
OPTIONS (
    format = 'CSV',
    uris = [
        'gs://nyc-tl-data/trip data/yellow_tripdata_2019-*.csv',
        'gs://nyc-tl-data/trip data/yellow_tripdata_2020-*.csv'
    ]
);
```

Khi bảng được tạo, BigQuery sẽ tự động đọc header của tệp CSV để suy luận kiểu dữ liệu của từng cột (Auto-detect schema). Tuy nhiên, vì dữ liệu nằm bên ngoài tại GCS nên kích thước bảng hiển thị trong BigQuery là 0 Bytes.

Truy vấn bảng ngoại vi tương tự như bất kỳ bảng cơ sở dữ liệu thông thường nào:

```sql
SELECT *
FROM taxi-rides-ny.nytaxi.external_yellow_tripdata
LIMIT 10;
```

---

## 7. Kỹ Thuật Phân Vùng Dữ Liệu (Partitioning)

**Phân vùng (Partitioning)** là một trong những tính năng quan trọng nhất trong việc tối ưu hóa chi phí và hiệu năng BigQuery.

Nếu bảng của bạn có hàng triệu bản ghi theo thời gian, nhưng các câu truy vấn thực tế chủ yếu lọc theo một khoảng ngày nhất định (ví dụ: chỉ phân tích tháng 6/2019). Khi bạn phân vùng bảng theo cột ngày (`DATE`), mỗi ngày sẽ trở thành một phân vùng độc lập (partition): các bản ghi ngày 01/06 vào phân vùng 1, ngày 02/06 vào phân vùng 2,...

Khi câu lệnh SQL có điều kiện `WHERE DATE(pickup_date) = '2019-06-02'`, BigQuery sẽ **chỉ quét đúng phân vùng ngày hôm đó và bỏ qua toàn bộ phần còn lại của bảng**.

![Mô phỏng cơ chế Phân vùng dữ liệu theo ngày](images/01-data-warehouse-and-bigquery-05-partitioning-diagram-crisp.png)

### Thực Hành So Sánh Giữa Bảng Thường Và Bảng Phân Vùng

Tạo bảng thường (không phân vùng):

```sql
CREATE OR REPLACE TABLE taxi-rides-ny.nytaxi.yellow_tripdata_non_partitioned AS
SELECT *
FROM taxi-rides-ny.nytaxi.external_yellow_tripdata;
```

Tạo bảng có phân vùng theo ngày đón xe (`PARTITION BY DATE(tpep_pickup_datetime)`):

```sql
CREATE OR REPLACE TABLE taxi-rides-ny.nytaxi.yellow_tripdata_partitioned
PARTITION BY DATE(tpep_pickup_datetime) AS
SELECT *
FROM taxi-rides-ny.nytaxi.external_yellow_tripdata;
```

Chạy cùng một câu truy vấn lọc dữ liệu tháng 6/2019 trên cả 2 bảng:

```sql
SELECT DISTINCT(VendorID)
FROM taxi-rides-ny.nytaxi.yellow_tripdata_non_partitioned
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2019-06-30';
```

### Kết Quả Tiết Kiệm Chi Phí Vượt Trội:

* **Trên bảng không phân vùng**: BigQuery phải quét tới **1.6 GB** dữ liệu (quét toàn bộ bảng).
* **Trên bảng có phân vùng**: BigQuery chỉ quét **105.9 MB** (giảm tới hơn 15 lần lượng dữ liệu quét!).

| Bảng dữ liệu | Dự toán lượng dữ liệu quét | Thực tế quét sau khi chạy |
| :--- | :--- | :--- |
| **Bảng không phân vùng** | 1.6 GB | 1.6 GB |
| **Bảng có phân vùng (Partitioned)** | 105.9 MiB | 105.9 MiB |

---

## 8. Kỹ Thuật Gom Cụm Dữ Liệu (Clustering)

Sau phân vùng, kỹ thuật tiếp theo là **Gom cụm dữ liệu (Clustering)**.

Nếu như Phân vùng chia dữ liệu theo ngày ở cấp độ vĩ mô, thì Gom cụm sẽ sắp xếp các hàng dữ liệu có cùng giá trị của cột gom cụm nằm liền kề nhau bên trong từng khối lưu trữ (storage blocks).

![Mô phỏng cơ chế gom cụm Clustering bên trong các Partition](images/01-data-warehouse-and-bigquery-07-clustering-diagram-crisp.png)

Tạo bảng vừa phân vùng theo ngày vừa gom cụm theo `VendorID`:

```sql
CREATE OR REPLACE TABLE taxi-rides-ny.nytaxi.yellow_tripdata_partitioned_clustered
PARTITION BY DATE(tpep_pickup_datetime)
CLUSTER BY VendorID AS
SELECT * 
FROM taxi-rides-ny.nytaxi.external_yellow_tripdata;
```

Chạy truy vấn đếm số chuyến của nhà cung cấp số 1 (`VendorID = 1`) từ tháng 6/2019 đến tháng 12/2020:

```sql
SELECT count(*) as trips
FROM taxi-rides-ny.nytaxi.yellow_tripdata_partitioned_clustered
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2020-12-31'
  AND VendorID = 1;
```

### So Sánh Lợi Ích:

* Bảng chỉ phân vùng: Quét **1.1 GB** dữ liệu.
* Bảng kết hợp cả phân vùng và gom cụm: Quét chỉ **843.5 MB** dữ liệu (BigQuery tự động bỏ qua các khối lưu trữ không chứa VendorID = 1 bên trong phân vùng).

| Loại bảng | Dự toán ban đầu | Lượng dữ liệu thực tế được quét |
| :--- | :--- | :--- |
| **Bảng chỉ phân vùng** | 1.1 GB | 1.1 GB |
| **Bảng Phân vùng + Gom cụm** | 1.1 GB | **843.5 MB** |

Bài học tiếp theo [Partitioning vs Clustering](02-partitioning-vs-clustering.md) sẽ phân tích chi tiết khi nào nên dùng phân vùng, khi nào nên dùng gom cụm, và khi nào nên kết hợp cả hai.

---

## Tài Liệu Tham Khảo

- [Slide bài giảng toàn bộ Module 3](https://docs.google.com/presentation/d/1a3ZoBAXFk8-EhUsd7rAZd-5p_HpltkzSeujjRGB2TAI/edit?usp=sharing)
- Mã nguồn SQL sử dụng xuyên suốt module: [`big_query.sql`](big_query.sql)
