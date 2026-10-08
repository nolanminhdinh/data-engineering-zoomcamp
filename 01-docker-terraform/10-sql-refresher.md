---
video_url: https://www.youtube.com/watch?v=QEcps_iskgg
prev_url: 09-docker-compose.md
next_url: 11-cleanup.md
---
# Ôn Tập Kiến Thức SQL Thực Chiến (SQL Refresher)

**Điều kiện tiên quyết**: Đảm bảo Docker Compose đang khởi chạy các container `pgdatabase` và `pgadmin`.

Truy cập giao diện pgAdmin tại `http://localhost:8085` trên trình duyệt. (Nếu chưa thấy bảng mới tạo, nhấp chuột phải vào database hoặc mục Tables và chọn **Refresh**).

Bây giờ chúng ta bắt đầu viết các câu lệnh SQL thực tế trên bộ dữ liệu Yellow Taxi!

---

## 1. Phép Kết Nối Trong (INNER JOIN)

### Cú pháp INNER JOIN ẩn (Implicit INNER JOIN)
Kết nối bảng dữ liệu chuyến đi `yellow_taxi_trips` với bảng danh mục địa điểm `zones` cho điểm đón (pickup) và điểm trả (dropoff):

```sql
SELECT
    tpep_pickup_datetime,
    tpep_dropoff_datetime,
    total_amount,
    CONCAT(zpu."Borough", ' | ', zpu."Zone") AS "pickup_loc",
    CONCAT(zdo."Borough", ' | ', zdo."Zone") AS "dropoff_loc"
FROM
    yellow_taxi_trips t,
    zones zpu,
    zones zdo
WHERE
    t."PULocationID" = zpu."LocationID"
    AND t."DOLocationID" = zdo."LocationID"
LIMIT 100;
```

### Cú pháp INNER JOIN tường minh (Explicit INNER JOIN)

```sql
SELECT
    tpep_pickup_datetime,
    tpep_dropoff_datetime,
    total_amount,
    CONCAT(zpu."Borough", ' | ', zpu."Zone") AS "pickup_loc",
    CONCAT(zdo."Borough", ' | ', zdo."Zone") AS "dropoff_loc"
FROM
    yellow_taxi_trips t
JOIN
    zones zpu ON t."PULocationID" = zpu."LocationID"
JOIN
    zones zdo ON t."DOLocationID" = zdo."LocationID"
LIMIT 100;
```

---

## 2. Kiểm Tra Chất Lượng Dữ Liệu (Data Quality Checks)

### Kiểm tra các bản ghi có ID địa điểm bị NULL

```sql
SELECT
    tpep_pickup_datetime,
    tpep_dropoff_datetime,
    total_amount,
    "PULocationID",
    "DOLocationID"
FROM
    yellow_taxi_trips
WHERE
    "PULocationID" IS NULL
    OR "DOLocationID" IS NULL
LIMIT 100;
```

### Kiểm tra các ID địa điểm không tồn tại trong bảng danh mục `zones`

```sql
SELECT
    tpep_pickup_datetime,
    tpep_dropoff_datetime,
    total_amount,
    "PULocationID",
    "DOLocationID"
FROM
    yellow_taxi_trips
WHERE
    "DOLocationID" NOT IN (SELECT "LocationID" from zones)
    OR "PULocationID" NOT IN (SELECT "LocationID" from zones)
LIMIT 100;
```

---

## 3. Các Phép Kết Nối Ngoài: LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN

Để minh họa tình huống một số địa điểm bị khuyết thiếu trong danh mục, ta thử xóa một ID:

```sql
DELETE FROM zones WHERE "LocationID" = 142;
```

### LEFT JOIN (Giữ lại toàn bộ chuyến đi kể cả khi không tìm thấy địa điểm đón):

```sql
SELECT
    tpep_pickup_datetime,
    tpep_dropoff_datetime,
    total_amount,
    CONCAT(zpu."Borough", ' | ', zpu."Zone") AS "pickup_loc",
    CONCAT(zdo."Borough", ' | ', zdo."Zone") AS "dropoff_loc"
FROM
    yellow_taxi_trips t
LEFT JOIN
    zones zpu ON t."PULocationID" = zpu."LocationID"
JOIN
    zones zdo ON t."DOLocationID" = zdo."LocationID"
LIMIT 100;
```

---

## 4. Gom Nhóm Dữ Liệu (GROUP BY) Và Sắp Xếp (ORDER BY)

### Tính tổng số chuyến đi theo từng ngày:

```sql
SELECT
    CAST(tpep_dropoff_datetime AS DATE) AS "day",
    COUNT(1) AS "total_trips"
FROM
    yellow_taxi_trips
GROUP BY
    CAST(tpep_dropoff_datetime AS DATE)
ORDER BY
    "day" ASC
LIMIT 100;
```

### Tìm những ngày có số lượng chuyến đi cao nhất:

```sql
SELECT
    CAST(tpep_dropoff_datetime AS DATE) AS "day",
    COUNT(1) AS "count"
FROM
    yellow_taxi_trips
GROUP BY
    CAST(tpep_dropoff_datetime AS DATE)
ORDER BY
    "count" DESC
LIMIT 100;
```

### Kết hợp nhiều hàm tổng hợp (Aggregations: COUNT, MAX, AVG):

```sql
SELECT
    CAST(tpep_dropoff_datetime AS DATE) AS "day",
    COUNT(1) AS "count",
    MAX(total_amount) AS "max_total_amount",
    MAX(passenger_count) AS "max_passengers"
FROM
    yellow_taxi_trips
GROUP BY
    CAST(tpep_dropoff_datetime AS DATE)
ORDER BY
    "count" DESC
LIMIT 100;
```

### Gom nhóm theo nhiều trường (Grouping by Multiple Fields):

```sql
SELECT
    CAST(tpep_dropoff_datetime AS DATE) AS "day",
    "DOLocationID",
    COUNT(1) AS "count",
    MAX(total_amount) AS "max_total_amount",
    MAX(passenger_count) AS "max_passengers"
FROM
    yellow_taxi_trips
GROUP BY
    1, 2
ORDER BY
    "day" ASC,
    "DOLocationID" ASC
LIMIT 100;
```
