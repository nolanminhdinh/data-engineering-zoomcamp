---
video_url: https://www.youtube.com/watch?v=18jIzE41fJ4
prev_url: 12-terraform-overview.md
next_url: ../02-workflow-orchestration/01-what-is-workflow-orchestration.md
---
# Tổng Quan Về Nền Tảng Google Cloud (GCP Overview)

Trong suốt khóa học này, chúng ta sẽ sử dụng nền tảng đám mây **Google Cloud Platform (GCP)** làm môi trường thực hành chính.

## Các Dịch Vụ Cốt Lõi Trên GCP Được Sử Dụng Trong Khóa Học:
* **Google Cloud Storage (GCS)**: Đóng vai trò là **Hồ dữ liệu (Data Lake)** — lưu trữ dữ liệu thô ở mọi định dạng (CSV, Parquet) với chi phí thấp và độ bền cao.
* **Google BigQuery**: Đóng vai trò là **Kho dữ liệu (Data Warehouse)** — công cụ phân tích dữ liệu quy mô Petabyte theo kiến trúc serverless, hỗ trợ SQL tiêu chuẩn và BigQuery ML.

Các nền tảng đám mây phân chia dịch vụ của họ thành các nhóm chuyên biệt như điện toán (compute), mạng (networking), lưu trữ (storage), dữ liệu lớn (big data), danh tính & bảo mật (identity), và máy học (machine learning):

![Các nhóm dịch vụ điện toán đám mây: Compute, Management, Networking, Storage & Databases, Big Data, Identity & Security, Machine Learning.](images/cloud-service-families.png)

---

## 1. Các Bước Khởi Tạo Tài Khoản Ban Đầu (Initial Setup)

Google Cloud cung cấp gói dùng thử miễn phí (Free Tier) với $300 tín dụng (credits) cho người dùng mới.

1. Đăng ký tài khoản tại [Google Cloud Console](https://console.cloud.google.com/) bằng địa chỉ Gmail của bạn.
2. Tạo một Dự án mới (Project):
   * Đặt tên gợi nhớ, ví dụ: `dtc-de-zoomcamp`, và ghi chú lại giá trị **Project ID** (chúng ta sẽ dùng ID này khi viết cấu hình Terraform).
3. Tạo **Tài khoản dịch vụ (Service Account)** phục vụ tự động hóa:
   * Vào mục *IAM & Admin* → *Service Accounts* → Nhấn *Create Service Account*.
   * Gán tạm quyền `Viewer`.
   * Tạo và tải về khóa xác thực dạng JSON (`service-account-key.json`).
4. Cài đặt công cụ dòng lệnh [Google Cloud CLI (gcloud SDK)](https://cloud.google.com/sdk/docs/quickstart).
5. Thiết lập biến môi trường trỏ tới tệp khóa JSON vừa tải về:
   ```bash
   # Trên Linux/macOS hoặc Git Bash:
   export GOOGLE_APPLICATION_CREDENTIALS="/duong/dan/toi/khoa-service-account.json"

   # Trên Windows PowerShell:
   $env:GOOGLE_APPLICATION_CREDENTIALS="C:\duong\dan\toi\khoa-service-account.json"

   # Đăng nhập Application Default Credentials (ADC)
   gcloud auth application-default login
   ```

---

## 2. Cấp Quyền Truy Cập Cần Thiết (IAM Roles)

1. Cấp quyền truy cập cho Service Account:
   * Vào mục [IAM & Admin](https://console.cloud.google.com/iam-admin/iam).
   * Nhấp biểu tượng sửa quyền của Service Account bạn vừa tạo.
   * Thêm các vai trò (roles) quan trọng sau:
     * **Storage Admin** (Quản trị toàn quyền Cloud Storage)
     * **Storage Object Admin** (Tạo, đọc, ghi đối tượng trong bucket)
     * **BigQuery Admin** (Quản trị toàn quyền BigQuery)
2. Kích hoạt các API cần thiết cho dự án:
   * [IAM API](https://console.cloud.google.com/apis/library/iam.googleapis.com)
   * [IAM Credentials API](https://console.cloud.google.com/apis/library/iamcredentials.googleapis.com)
3. Đảm bảo biến môi trường `GOOGLE_APPLICATION_CREDENTIALS` đã được thiết lập chính xác trên terminal của bạn trước khi chạy Terraform.

---

## Thực Hành Tạo Hạ Tầng GCP Bằng Terraform

Tiếp tục bài thực hành chi tiết tạo bucket và dataset trên GCP tại: [Thư mục cấu hình Terraform (terraform/)](./terraform).
