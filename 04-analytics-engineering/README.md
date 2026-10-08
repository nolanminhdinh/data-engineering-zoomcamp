# Module 4: Kỹ Thuật Phân Tích Dữ Liệu (Analytics Engineering)

Trong module này, bạn sẽ tìm hiểu vai trò của **Analytics Engineering** - cầu nối giữa kỹ thuật dữ liệu và phân tích nghiệp vụ, làm chủ công cụ chuyển đổi dữ liệu chuẩn công nghiệp **dbt (data build tool)**, thực hành mô hình hóa dữ liệu (Data Modeling) theo kiến trúc Star Schema (Fact & Dimension tables) kết hợp với **DuckDB** ở môi trường local và **Google BigQuery** trên đám mây.

---

## Danh Sách Bài Học (Units)

1. [Cơ bản về Analytics Engineering (Analytics Engineering Basics)](01-analytics-engineering-basics.md)
2. [dbt là gì? (What is dbt?)](02-what-is-dbt.md)
3. [So sánh dbt Core và dbt Cloud (dbt Core vs dbt Cloud)](03-dbt-core-vs-dbt-cloud.md)
4. [Cấu trúc một dự án dbt (dbt Project Structure)](04-dbt-project-structure.md)
5. [Định nghĩa nguồn dữ liệu trong dbt (dbt Sources)](05-dbt-sources.md)
6. [Xây dựng mô hình biến đổi dữ liệu (dbt Models)](06-dbt-models.md)
7. [Dữ liệu tĩnh và hàm mở rộng (dbt Seeds and Macros)](07-dbt-seeds-and-macros.md)
8. [Tạo tài liệu và sơ đồ dòng chảy dữ liệu tự động (Documentation & Lineage)](08-documentation.md)
9. [Kiểm thử chất lượng dữ liệu trong dbt (dbt Tests)](09-dbt-tests.md)
10. [Quản lý và sử dụng các gói mở rộng (dbt Packages)](10-dbt-packages.md)
11. [Các câu lệnh dbt thường dùng (dbt Commands)](11-dbt-commands.md)

---

## Bài Tập Về Nhà (Homework)

* Xem chi tiết trong thư mục `cohorts/` tương ứng (ví dụ: `cohorts/2026/04-analytics-engineering/` hoặc `cohorts/2027/`).

---

## Hướng Dẫn Thiết Lập (Setup Guides)

* [Thiết lập cục bộ (DuckDB + dbt Core)](setup/local_setup.md)
* [Thiết lập trên Cloud (BigQuery + dbt Cloud)](setup/cloud_setup.md)
* [Xử lý lỗi với DuckDB (DuckDB Troubleshooting)](setup/duckdb_troubleshooting.md)

---

## Mã Nguồn Đi Kèm (Companion Files)

* [`taxi_rides_ny/`](taxi_rides_ny/) — Dự án dbt hoàn chỉnh được xây dựng và phát triển xuyên suốt module này.
* [Ôn tập kiến thức SQL cho Analytics](refreshers/SQL.md)

---

## Ghi Chú Của Cộng Đồng (Community Notes)

<details>
<summary>Nhấn để xem ghi chú và đóng góp từ cộng đồng học viên</summary>

* [Slide bài giảng các năm trước](https://docs.google.com/presentation/d/1xSll_jv0T8JF4rYZvLHfkJXYqUjPtThA/edit?usp=sharing&ouid=114544032874539580154&rtpof=true&sd=true)
* [Ghi chú từ Alvaro Navas](https://github.com/ziritrion/dataeng-zoomcamp/blob/main/notes/4_analytics.md)
* [Blog học tập DE của Sandy](https://learningdataengineering540969211.wordpress.com/2022/02/17/week-4-setting-up-dbt-cloud-with-bigquery/)
* [Ghi chú từ Victor Padilha](https://github.com/padilha/de-zoomcamp/tree/master/week4)
* [Bài viết tiếng Tây Ban Nha của Marcos Torregrosa](https://www.n4gash.com/2023/data-engineering-zoomcamp-semana-4/)
* [Ghi chú từ froukje](https://github.com/froukje/de-zoomcamp/blob/main/week_4_analytics_engineering/notes/notes_week_04.md)
* [Ghi chú từ Alain Boisvert](https://github.com/boisalai/de-zoomcamp-2023/blob/main/week4.md)
* [Thiết lập Prefect với dbt bởi Vera](https://medium.com/@verazabeida/zoomcamp-week-5-5b6a9d53a3a0)
* [Blog của Xia He-Bleinagel](https://xiahe-bleinagel.com/2023/02/week-4-data-engineering-zoomcamp-notes-analytics-engineering-and-dbt/)
* [Cài đặt DBT với BigQuery bởi Tofag](https://medium.com/@fagbuyit/setting-up-your-dbt-cloud-dej-9-d18e5b7c96ba)
* [Bài viết của Dewi Oktaviani](https://medium.com/@oktavianidewi/de-zoomcamp-2023-learning-week-4-analytics-engineering-with-dbt-53f781803d3e)
* [Ghi chú từ Vincenzo Galante](https://binchentso.notion.site/Data-Talks-Club-Data-Engineering-Zoomcamp-8699af8e7ff94ec49e6f9bdec8eb69fd)
* [Ghi chú từ Balaji](https://github.com/Balajirvp/DE-Zoomcamp/blob/main/Week%204/Data%20Engineering%20Zoomcamp%20Week%204.ipynb)
* [Ghi chú của Linda](https://github.com/inner-outer-space/de-zoomcamp-2024/blob/main/4-analytics-engineering/readme.md)
* [Bản ghi lời thoại video năm 2024](https://drive.google.com/drive/folders/1V2sHWOotPEMQTdMT4IMki1fbMPTn3jOP?usp=drive)
* [Bài viết blog của Jonah Oliver](https://www.jonahboliver.com/blog/de-zc-w4)
* [Ghi chú năm 2025 từ Manuel Guerra](https://github.com/ManuelGuerra1987/data-engineering-zoomcamp-notes/blob/main/4_Analytics-Engineering/README.md)
* [Ghi chú năm 2025 từ Horeb SEIDOU](https://spotted-hardhat-eea.notion.site/Week-4-Analytics-Engineering-18929780dc4a808692e4e0ee488bf49c?pvs=74)
* [Ghi chú năm 2025 từ Daniel Lachner](https://github.com/mossdet/dlp_data_eng/blob/main/Notes/04_01_Analytics_Engineering.pdf)
* [Ghi chú năm 2026 về câu lệnh dbt bởi Sharad K. Gupta](https://github.com/sharadgupta27/data-engineering/blob/main/Notes/dbt_commands.md)
* [Tổng quan Analytics Engineering](https://github.com/khanhnguyen7802/DataEngineer101/tree/main/week4-analytics-engineering#readme) 
* [Ghi chú dbt 2026](https://github.com/khanhnguyen7802/DataEngineer101/blob/main/week4-analytics-engineering/dbt_installation.md) | [Thiết lập dbt + Duckdb qua Docker](https://github.com/khanhnguyen7802/DataEngineer101/blob/main/week4-analytics-engineering/dbt_installation.md) bởi Khanh Nguyen

</details>
