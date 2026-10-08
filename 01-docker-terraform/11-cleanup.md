---
prev_url: 10-sql-refresher.md
next_url: 12-terraform-overview.md
---
# Dọn Dẹp Tài Nguyên Sau Thực Hành (Cleanup)

Sau khi hoàn thành các bài thực hành, bạn nên tiến hành dọn dẹp các tài nguyên Docker và tệp tạm để giải phóng dung lượng ổ cứng.

---

## 1. Dừng Toàn Bộ Các Container Đang Chạy

Tại thư mục chứa tệp `docker-compose.yaml`:

```bash
docker compose down
```

---

## 2. Xóa Các Container Đã Dừng

```bash
# Xem danh sách tất cả các container
docker ps -a

# Xóa một container cụ thể theo ID hoặc tên
docker rm <container_id_hoac_name>

# Xóa toàn bộ các container đã dừng hoạt động
docker container prune
```

---

## 3. Xóa Các Docker Images Không Dùng Đến

```bash
# Liệt kê tất cả các images
docker images

# Xóa image thực hành nạp dữ liệu
docker rmi taxi_ingest:v001

# Dọn dẹp tất cả các images không còn container nào sử dụng
docker image prune -a
```

---

## 4. Xóa Các Docker Volumes (Ổ Đĩa Dữ Liệu)

```bash
# Liệt kê danh sách các volumes
docker volume ls

# Xóa cụ thể các volume thực hành
docker volume rm ny_taxi_postgres_data
docker volume rm pgadmin_data

# Xóa toàn bộ volumes rác không được gắn vào container nào
docker volume prune
```

---

## 5. Xóa Các Mạng Ảo Docker (Networks)

```bash
# Liệt kê các mạng ảo
docker network ls

# Xóa mạng pg-network đã tạo
docker network rm pg-network

# Xóa tất cả các mạng ảo không còn dùng đến
docker network prune
```

---

## 6. Lệnh Dọn Sạch Toàn Diện Cực Nhanh (Complete Cleanup)

> [!CAUTION]
> Lệnh này sẽ xóa TOÀN BỘ container đã dừng, toàn bộ images không dùng, toàn bộ networks và toàn bộ volumes. Hãy cẩn trọng nếu máy bạn có các dự án Docker khác đang lưu dữ liệu quan trọng!

```bash
docker system prune -a --volumes
```

---

## 7. Dọn Dẹp Các Tệp Tin Rác Trên Máy Cục Bộ

```bash
# Xóa các tệp parquet sinh ra khi chạy thử nghiệm
rm *.parquet

# Xóa bộ nhớ đệm Python
rm -rf __pycache__ .pytest_cache

# Xóa môi trường ảo nếu muốn cài đặt lại từ đầu
rm -rf .venv
```

---

Chúc bạn có những trải nghiệm học tập và thực hành hiệu quả! 🐳📊
