# Module 1: Đóng Gói Ứng Dụng (Containerization) và Hạ Tầng Dưới Dạng Mã Nguồn (IaC)

Module này trang bị cho bạn nền tảng vững chắc về công nghệ container với **Docker**, quản trị cơ sở dữ liệu với **PostgreSQL**, viết script nạp dữ liệu (data ingestion script) bằng **Python**, và tự động hóa khởi tạo hạ tầng đám mây Google Cloud Platform (GCP) bằng **Terraform**.

---

## Danh Sách Bài Học (Units)

1. [Giới thiệu về Docker (Introduction to Docker)](01-introduction.md)
2. [Môi trường ảo và Đường ống dữ liệu (Virtual Environments and Data Pipelines)](02-virtual-environment.md)
3. [Đóng gói đường ống vào Docker (Dockerizing the Pipeline)](03-dockerizing-pipeline.md)
4. [Khởi chạy PostgreSQL với Docker (Running PostgreSQL with Docker)](04-postgres-docker.md)
5. [Bộ dữ liệu NY Taxi và Quy trình nạp dữ liệu (NY Taxi Dataset & Data Ingestion)](05-data-ingestion.md)
6. [Xây dựng Script nạp dữ liệu (Creating the Data Ingestion Script)](06-ingestion-script.md)
7. [pgAdmin - Công cụ quản trị cơ sở dữ liệu (Database Management Tool)](07-pgadmin.md)
8. [Đóng gói Script nạp dữ liệu vào Docker (Dockerizing the Ingestion Script)](08-dockerizing-ingestion.md)
9. [Điều phối đa container với Docker Compose (Docker Compose)](09-docker-compose.md)
10. [Ôn tập kiến thức SQL thực chiến (SQL Refresher)](10-sql-refresher.md)
11. [Dọn dẹp môi trường và tài nguyên (Cleanup)](11-cleanup.md)
12. [Tổng quan về Terraform (Terraform Overview)](12-terraform-overview.md)
13. [Tổng quan về nền tảng Google Cloud (GCP Overview)](13-gcp-overview.md)

---

## Bài Tập Về Nhà (Homework)

* Kiểm tra đề bài và hướng dẫn làm bài tập trong thư mục `cohorts/` tương ứng (ví dụ: `cohorts/2026/01-docker-terraform/homework.md` hoặc `cohorts/2027/`).

---

## Hướng Dẫn Thiết Lập Môi Trường (Setup Guides)

* [Hướng dẫn cài đặt Terraform và cấu hình GCP](setup/terraform-and-gcp-setup.md)
* [Hướng dẫn cài đặt Terraform và GCP trên hệ điều hành Windows](setup/terraform-on-windows.md)

---

## Mã Nguồn Thực Hành (Workshop Code)

* [Đường ống dữ liệu mẫu (pipeline/)](pipeline/) — Mã nguồn đường ống nạp dữ liệu được đóng gói Docker xây dựng từ bài 3 đến bài 9.
* [Cấu hình Terraform (terraform/)](terraform/) — Các tệp khai báo hạ tầng Terraform sử dụng trong bài 12 và bài 13.

---

## Ghi Chú Của Cộng Đồng (Community Notes)

<details>
<summary>Bạn có ghi chép trong quá trình học? Nhấn để xem và đóng góp ghi chú</summary>

* [Ghi chú từ Alvaro Navas](https://github.com/ziritrion/dataeng-zoomcamp/blob/main/notes/1_intro.md)
* [Ghi chú từ Abd](https://itnadigital.notion.site/Week-1-Introduction-f18de7e69eb4453594175d0b1334b2f4)
* [Ghi chú từ Aaron](https://github.com/ABZ-Aaron/DataEngineerZoomCamp/blob/master/week_1_basics_n_setup/README.md)
* [Ghi chú từ Faisal](https://github.com/FaisalMohd/data-engineering-zoomcamp/blob/main/week_1_basics_n_setup/Notes/DE%20Zoomcamp%20Week-1.pdf)
* [Ghi chú từ Michael Harty](https://github.com/mharty3/data_engineering_zoomcamp_2022/tree/main/week01)
* [Bài viết từ Isaac Kargar](https://kargarisaac.github.io/blog/data%20engineering/jupyter/2022/01/18/data-engineering-w1.html)
* [Ghi chú viết tay của Mahmoud Zaher](https://github.com/zaherweb/DataEngineering/blob/master/week%201.pdf)
* [Ghi chú từ Candace Williams](https://teacherc.github.io/data-engineering/2023/01/18/zoomcamp1.html)
* [Ghi chú từ Marcos Torregrosa](https://www.n4gash.com/2023/data-engineering-zoomcamp-semana-1/)
* [Ghi chú từ Vincenzo Galante](https://binchentso.notion.site/Data-Talks-Club-Data-Engineering-Zoomcamp-8699af8e7ff94ec49e6f9bdec8eb69fd)
* [Ghi chú từ Victor Padilha](https://github.com/padilha/de-zoomcamp/tree/master/week1)
* [Ghi chú từ froukje](https://github.com/froukje/de-zoomcamp/blob/main/week_1_basics_n_setup/notes/notes_week_01.md)
* [Ghi chú từ adamiaonr](https://github.com/adamiaonr/data-engineering-zoomcamp/blob/main/week_1_basics_n_setup/2_docker_sql/NOTES.md)
* [Ghi chú từ Xia He-Bleinagel](https://xiahe-bleinagel.com/2023/01/week-1-data-engineering-zoomcamp-notes/)
* [Ghi chú từ Balaji](https://github.com/Balajirvp/DE-Zoomcamp/blob/main/Week%201/Detailed%20Week%201%20Notes.ipynb)
* [Ghi chú từ Erik](https://twitter.com/ehub96/status/1621351266281730049)
* [Ghi chú của Alain Boisvert](https://github.com/boisalai/de-zoomcamp-2023/blob/main/week1.md)
* [Ghi chú về Docker, Docker Compose và thiết lập Python chuẩn](https://medium.com/@verazabeida/zoomcamp-2023-week-1-f4f94cb360ae), bởi Vera
* [Thiết lập môi trường trên máy ảo Google VM](https://itsadityagupta.hashnode.dev/setting-up-the-development-environment-on-google-virtual-machine), bài blog của Aditya Gupta
* [Ghi chú từ Zharko Cekovski](https://www.zharconsulting.com/contents/data/data-engineering-bootcamp-2024/week-1-postgres-docker-and-ingestion-scripts/)
* [Video hướng dẫn Module 1 năm 2024 bởi ellacharmed trên YouTube](https://youtu.be/VUZshlVAnk4)
* [Ghi chú Docker bởi Linda](https://github.com/inner-outer-space/de-zoomcamp-2024/blob/main/1a-docker_sql/readme.md) • [Ghi chú Terraform bởi Linda](https://github.com/inner-outer-space/de-zoomcamp-2024/blob/main/1b-terraform_gcp/readme.md)
* [Ghi chú từ Hammad Tariq](https://github.com/hamad-tariq/HammadTariq-ZoomCamp2024/blob/9c8b4908416eb8cade3d7ec220e7664c003e9b11/week_1_basics_n_setup/README.md)
* [Ghi chú của Hùng](https://hung.bearblog.dev/docker/) & [Bảng tra cứu lệnh Docker (Docker Cheatsheet)](https://github.com/HangenYuu/docker-cheatsheet)
* [Ghi chú của Kemal](https://github.com/kemaldahha/data-engineering-course/blob/main/week_1_notes.md)
* [Ghi chú của Manuel Guerra (Môi trường Windows + WSL2)](https://github.com/ManuelGuerra1987/data-engineering-zoomcamp-notes/blob/main/1_Containerization-and-Infrastructure-as-Code/README.md)
* [Ghi chú từ Horeb SEIDOU](https://spotted-hardhat-eea.notion.site/Week-1-Containerization-and-Infrastructure-as-Code-15729780dc4a80a08288e497ba937a37)
* [Gitbook Notes năm 2025 từ Tinker0425](https://data-engineering-zoomcamp-2025-t.gitbook.io/tinker0425/introduction/introduction-and-set-up)
* [Ghi chú Docker năm 2025 của Alex](https://github.com/alexg9010/2025_data_engineering_zoomcamp/blob/master/01_docker/README.md) | [Ghi chú Terraform của Alex](https://github.com/alexg9010/2025_data_engineering_zoomcamp/blob/master/01_3_terraform/README.md)
* [Ôn tập SQL năm 2025 - Gabi Fonseca](https://github.com/fonsecagabriella/data_engineering/blob/main/01_docker_postgress/0_sql_refresh.ipynb)
* [Thiết lập môi trường năm 2025 - Gabi Fonseca](https://github.com/fonsecagabriella/data_engineering/blob/main/01_docker_postgress/_setting_up.md)
* [Mẹo Linux/Fedora từ Mercy Markus](https://mercymarkus.com/posts/2025/series/dtc-dez-jan-2025/dtc-dez-2025-module-1/)
* [[Video hướng dẫn 2026 - Khanh Nguyen] Thiết lập môi trường bài tập tuần 1](https://youtu.be/_iqCWi_UoOc)

</details>
