---
video_url: https://www.youtube.com/watch?v=18jIzE41fJ4
prev_url: 11-cleanup.md
next_url: 13-gcp-overview.md
---
# Tổng Quan Về Terraform (Terraform Overview)

## 1. Các Khái Niệm Nền Tảng (Core Concepts)

### Terraform là gì?
1. **[Terraform](https://www.terraform.io)**:
   * Là một công cụ mã nguồn mở phát triển bởi tập đoàn [HashiCorp](https://www.hashicorp.com), chuyên dụng cho việc tự động khởi tạo, quản lý và cấp phát tài nguyên hạ tầng đám mây.
   * Áp dụng các nguyên lý thực hành tốt nhất của DevOps trong việc quản lý thay đổi hệ thống.
   * Quản lý các tệp cấu hình hạ tầng trực tiếp trên hệ thống quản lý phiên bản (Git), giúp duy trì trạng thái hạ tầng lý tưởng và đồng nhất giữa môi trường phát triển (dev/staging) và môi trường thực tế (production).

2. **Khái niệm IaC (Infrastructure as Code - Hạ tầng dưới dạng mã nguồn)**:
   * Xây dựng, chỉnh sửa và quản trị hạ tầng máy chủ, mạng, lưu trữ một cách an toàn, nhất quán và có khả năng tự động hóa lặp lại nhiều lần.
   * Toàn bộ tài nguyên cloud được mô tả bằng code, cho phép đánh số phiên bản, tái sử dụng và chia sẻ dễ dàng giữa các thành viên trong đội ngũ kỹ thuật.

3. **Các ưu thế vượt trội của Terraform**:
   * Quản lý toàn bộ vòng đời của hạ tầng từ lúc tạo mới, cập nhật cho đến khi hủy bỏ.
   * Theo dõi lịch sử thay đổi thông qua từng commit trên Git.
   * Hỗ trợ đa nền tảng đám mây lớn (Google Cloud Platform, AWS, Azure) cũng như các nền tảng container (Kubernetes, Docker).
   * Tiếp cận theo mô hình trạng thái (State-driven): so sánh chính xác giữa cấu hình mong muốn trong mã nguồn và tài nguyên thực tế đang chạy trên Cloud.

Terraform chạy trên máy tính cục bộ của bạn, giao tiếp với nhà cung cấp đám mây thông qua các plugin Provider để lập kế hoạch (Plan) và áp dụng thay đổi (Apply):

![Terraform chạy trên máy cục bộ và quản lý tài nguyên trên nhà cung cấp đám mây qua Provider.](images/terraform-provider-flow.png)

---

## 2. Cấu Trúc Các Tệp Tin Trong Dự Án Terraform

* `main.tf`: Tệp khai báo chính định nghĩa các dịch vụ đám mây (Google Cloud Storage buckets, BigQuery datasets, v.v.).
* `variables.tf`: Khai báo các tham số đầu vào (Project ID, khu vực vùng Region, tên bucket,...).
* `output.tf` (Tùy chọn): Khai báo các thông tin đầu ra sau khi tạo tài nguyên thành công.
* `terraform.tfstate`: Tệp lưu trữ trạng thái thực tế của toàn bộ tài nguyên đã được Terraform tạo ra trên đám mây.

---

## 3. Các Khối Cú Pháp Cơ Bản (Declarations)

* **Khối `terraform`**: Cấu hình các thiết lập nền tảng của Terraform:
  * `required_version`: Phiên bản Terraform tối thiểu được phép chạy.
  * `required_providers`: Khai báo danh sách các plugin provider cần tải (ví dụ: Google Provider).
  * `backend`: Nơi lưu trữ tệp trạng thái `terraform.tfstate` (lưu cục bộ trên máy hoặc lưu trên GCS bucket để làm việc nhóm).
* **Khối `provider`**: Định nghĩa nhà cung cấp dịch vụ đám mây cụ thể (Google Cloud, AWS).
* **Khối `resource`**: Định nghĩa một tài nguyên hạ tầng cụ thể được tạo ra (ví dụ: `google_storage_bucket`, `google_bigquery_dataset`).
* **Khối `variable` và `locals`**: Khai báo các biến truyền vào và các biến cục bộ tái sử dụng trong code.

---

## 4. Bốn Lệnh Thực Thi Cốt Lõi Trong Quy Trình Vận Hành

1. **`terraform init`**:
   * Khởi tạo dự án, tự động tải các plugin Provider cần thiết từ Terraform Registry.
2. **`terraform plan`**:
   * Đọc cấu hình code, đối chiếu với trạng thái thực tế trên Cloud, và đưa ra một bản kế hoạch thực thi chi tiết (những tài nguyên nào sẽ được tạo mới, cập nhật, hoặc bị xóa).
3. **`terraform apply`**:
   * Yêu cầu xác nhận từ lập trình viên, sau đó trực tiếp gọi API của Cloud để triển khai toàn bộ hạ tầng đúng theo kế hoạch đã đề ra.
4. **`terraform destroy`**:
   * Tự động xóa sạch toàn bộ các tài nguyên đám mây đã được Terraform tạo ra, giúp tiết kiệm triệt để chi phí khi không còn nhu cầu sử dụng.

---

## Tài Liệu Thực Hành Kế Tiếp

Tiếp tục bài thực hành chi tiết tạo hạ tầng GCP bằng Terraform tại: [Thư mục thực hành Terraform (terraform/)](./terraform).
