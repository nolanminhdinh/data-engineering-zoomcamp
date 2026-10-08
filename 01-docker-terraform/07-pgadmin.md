---
prev_url: 06-ingestion-script.md
next_url: 08-dockerizing-ingestion.md
---
# pgAdmin - Công Cụ Quản Trị Cơ Sở Dữ Liệu Trực Quan (Database Management Tool)

Mặc dù `pgcli` rất tiện lợi trên dòng lệnh, nhưng khi cần kiểm tra cấu trúc bảng phức tạp, xem sơ đồ dữ liệu, hoặc thực thi nhiều truy vấn phân tích lớn, một giao diện đồ họa trực quan (GUI) sẽ tiện dụng hơn rất nhiều. [**pgAdmin** là một công cụ nền web](https://www.pgadmin.org/) phổ biến nhất thế giới để quản lý PostgreSQL.

Chúng ta có thể chạy pgAdmin trực tiếp dưới dạng một Docker container song song với container PostgreSQL. Tuy nhiên, hai container này phải nằm trong cùng một **Mạng ảo Docker (Docker Virtual Network)** để có thể nhìn thấy và liên lạc được với nhau qua mạng nội bộ.

---

## 1. Khởi Chạy Container pgAdmin

```bash
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -v pgadmin_data:/var/lib/pgadmin \
  -p 8085:80 \
  dpage/pgadmin4
```

* Thiết lập volume `-v pgadmin_data:/var/lib/pgadmin` giúp lưu lại toàn bộ cấu hình máy chủ và sở thích người dùng, tránh việc phải cấu hình lại mỗi khi khởi động container.
* Ánh xạ cổng `-p 8085:80`: Cổng 80 mặc định bên trong container được đưa ra cổng `8085` trên máy thật để tránh trùng với cổng web khác.

> [!WARNING]
> Nếu chạy hai container độc lập như trên, pgAdmin sẽ **không thể kết nối** được tới container PostgreSQL vì chúng chưa thuộc cùng một mạng (Docker Network). Hãy thực hiện bước tạo mạng bên dưới.

---

## 2. Tạo Mạng Ảo Docker (Docker Network)

Khởi tạo một mạng ảo mang tên `pg-network`:

```bash
docker network create pg-network
```

> Bạn có thể kiểm tra danh sách mạng bằng `docker network ls`, hoặc xóa mạng sau khi dùng xong bằng lệnh `docker network rm pg-network`.

### Khởi Chạy Cả Hai Container Trên Cùng Mạng

Dừng các container cũ và khởi chạy lại chúng kèm cờ mạng `--network=pg-network` cùng tên container xác định (`--name`):

```bash
# Khởi chạy PostgreSQL trên mạng pg-network với tên định danh 'pgdatabase'
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql \
  -p 5432:5432 \
  --network=pg-network \
  --name pgdatabase \
  postgres:18

# Mở một cửa sổ dòng lệnh khác, khởi chạy pgAdmin trên cùng mạng pg-network
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -v pgadmin_data:/var/lib/pgadmin \
  -p 8085:80 \
  --network=pg-network \
  --name pgadmin \
  dpage/pgadmin4
```

* Nhờ cơ chế phân giải tên DNS nội bộ của Docker Network, container `pgadmin` có thể trỏ thẳng tới hostname `pgdatabase` thay vì phải cấu hình địa chỉ IP cố định.

---

## 3. Kết Nối pgAdmin Tới Cơ Sở Dữ Liệu PostgreSQL

1. Mở trình duyệt web và truy cập địa chỉ: `http://localhost:8085`
2. Đăng nhập bằng tài khoản: Email `admin@admin.com`, Mật khẩu `root`.
3. Nhấp chuột phải vào mục **Servers** ở thanh điều hướng bên trái → Chọn **Register** → Chọn **Server...**
4. Điền thông tin cấu hình:
   - **Tab General**: Đặt tên gợi nhớ tại ô Name: `Local Docker`
   - **Tab Connection**:
     - Host name/address: `pgdatabase` (chính là tên container đã khai báo trong cờ `--name`)
     - Port: `5432`
     - Maintenance database: `ny_taxi`
     - Username: `root`
     - Password: `root`
5. Nhấn **Save** để hoàn tất.

Giờ đây bạn đã có thể duyệt cơ sở dữ liệu `ny_taxi`, xem bảng `yellow_taxi_data` và chạy các câu lệnh SQL trực quan ngay trên giao diện web của pgAdmin!
