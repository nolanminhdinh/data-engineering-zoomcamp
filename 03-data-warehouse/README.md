# Module 3: Kho Dữ Liệu (Data Warehousing)

Trong module này, bạn sẽ tìm hiểu sâu về kiến trúc **Kho dữ liệu (Data Warehouse)** hiện đại trên nền tảng đám mây với **Google BigQuery**, cách tối ưu hóa chi phí và hiệu năng truy vấn thông qua kỹ thuật **Phân vùng dữ liệu (Partitioning)** và **Gom cụm dữ liệu (Clustering)**, hiểu rõ cơ chế vận hành bên trong của BigQuery, và xây dựng mô hình **Machine Learning trực tiếp bằng SQL (BigQuery ML)**.

---

## Danh Sách Bài Học (Units)

1. [Kho dữ liệu và Google BigQuery (Data Warehouse and BigQuery)](01-data-warehouse-and-bigquery.md)
2. [Phân vùng so với Gom cụm dữ liệu (Partitioning vs Clustering)](02-partitioning-vs-clustering.md)
3. [Các phương pháp tối ưu hóa tốt nhất trên BigQuery (BigQuery Best Practices)](03-bigquery-best-practices.md)
4. [Bản chất cấu trúc và cơ chế bên trong của BigQuery (Internals of BigQuery)](04-internals-of-bigquery.md)
5. [Ứng dụng Machine Learning trong BigQuery (Machine Learning in BigQuery)](05-machine-learning-in-bigquery.md)
6. [Triển khai mô hình Machine Learning từ BigQuery (Deploying a Machine Learning Model)](06-deploying-a-machine-learning-model.md)

---

## Bài Tập Về Nhà (Homework)

* Kiểm tra đề bài trong thư mục `cohorts/` tương ứng (ví dụ: `cohorts/2026/03-data-warehouse/` hoặc `cohorts/2027/`).

---

## Các Tệp Khác Trong Module

* [`extras/`](extras/README.md) — Script độc lập tải các file CSV taxi và nạp thẳng lên Cloud Storage dưới dạng định dạng cột Parquet mà không cần công cụ điều phối (orchestrator).

---

## Ghi Chú Của Cộng Đồng (Community Notes)

<details>
<summary>Nhấn để xem ghi chú và tài liệu tổng hợp từ các học viên</summary>

* [Ghi chú từ Alvaro Navas](https://github.com/ziritrion/dataeng-zoomcamp/blob/main/notes/3_data_warehouse.md)
* [Bài viết từ Isaac Kargar](https://kargarisaac.github.io/blog/data%20engineering/jupyter/2022/01/30/data-engineering-w3.html)
* [Bài viết tiếng Tây Ban Nha từ Marcos Torregrosa](https://www.n4gash.com/2023/data-engineering-zoomcamp-semana-3/) 
* [Ghi chú từ Victor Padilha](https://github.com/padilha/de-zoomcamp/tree/master/week3)
* [Ghi chú từ Xia He-Bleinagel](https://xiahe-bleinagel.com/2023/02/week-3-data-engineering-zoomcamp-notes-data-warehouse-and-bigquery/)
* [Bài viết tổng hợp về Data Lakes, Data Warehouses và công cụ](https://medium.com/@verazabeida/zoomcamp-week-4-b8bde661bf98), bởi Vera
* [Ghi chú từ froukje](https://github.com/froukje/de-zoomcamp/blob/main/week_3_data_warehouse/notes/notes_week_03.md)
* [Ghi chú từ Alain Boisvert](https://github.com/boisalai/de-zoomcamp-2023/blob/main/week3.md)
* [Ghi chú từ Vincenzo Galante](https://binchentso.notion.site/Data-Talks-Club-Data-Engineering-Zoomcamp-8699af8e7ff94ec49e6f9bdec8eb69fd)
* [Bản ghi lời thoại video năm 2024](https://drive.google.com/drive/folders/1quIiwWO-tJCruqvtlqe_Olw8nvYSmmDJ?usp=sharing) bởi Maria Fisher 
* [Ghi chú từ Linda](https://github.com/inner-outer-space/de-zoomcamp-2024/blob/main/3a-data-warehouse/readme.md)
* [Bài viết blog của Jonah Oliver](https://www.jonahboliver.com/blog/de-zc-w3)
* [Hướng dẫn gửi dữ liệu lên GCS và tạo bảng ngoại vi (external table)](https://drive.google.com/file/d/1GIi6xnS4070a8MUlIg-ozITt485_-ePB/view?usp=drive_link) bởi Maria Fisher
* [Script nạp file parquet lên Google bucket](https://github.com/amohan601/dataengineering-zoomcamp2024/blob/main/week_3_data_warehouse/mage_scripts/green_taxi_2022_v2.py) bởi Anju Mohan
* [Ghi chú từ HongWei](https://github.com/hwchua0209/data-engineering-zoomcamp-submission/blob/main/03-data-warehouse/README.md)
* [Ghi chú năm 2025 từ Manuel Guerra](https://github.com/ManuelGuerra1987/data-engineering-zoomcamp-notes/blob/main/3_Data-Warehouse/README.md)
* [Ghi chú từ Horeb SEIDOU](https://spotted-hardhat-eea.notion.site/Week-3-Data-Warehouse-and-BigQuery-17c29780dc4a80c8a226f372543ae388)
* [Ghi chú năm 2025 từ Gabi Fonseca](https://github.com/fonsecagabriella/data_engineering/blob/main/03_data_warehouse/00_notes.md)
* [Gitbook Notes năm 2025 từ Tinker0425](https://data-engineering-zoomcamp-2025-t.gitbook.io/tinker0425/module-3/introduction-to-module-3)
* [Ghi chú năm 2025 từ Daniel Lachner](https://drive.google.com/file/d/105zjtLFi0sRqqFFgdMSCTzfcLPx2rfv4/view?usp=sharing)
* [Ghi chú năm 2026 từ Catherine Frost](https://docs.google.com/document/d/1j3jeNnBI2fw1nq7JwEauPx2G8FybDfTqmMk7eRu0vSo/edit?tab=t.0)

</details>
