# Module 6: Xử Lý Dữ Liệu Theo Lô (Batch Processing)

Trong module này, bạn sẽ làm chủ công nghệ xử lý dữ liệu lớn theo lô phân tán (Distributed Batch Processing) với **Apache Spark** và **PySpark** - chuẩn mực công nghiệp cho xử lý dữ liệu quy mô lớn (Large-Scale Data Processing). Bạn sẽ đi từ cách sử dụng Spark DataFrame và Spark SQL, đến việc mổ xẻ kiến trúc bên trong của Spark Cluster, cơ chế xáo trộn dữ liệu (Shuffle) trong phép GroupBy & Join, thao tác tầng thấp với RDDs, và kết nối Spark với **Google Cloud Storage (GCS)**, **Dataproc** và **BigQuery**.

---

## Danh Sách Bài Học (Units)

1. [Giới thiệu về Xử lý dữ liệu theo lô (Introduction to Batch Processing)](01-introduction-to-batch-processing.md)
2. [Giới thiệu về Apache Spark (Introduction to Spark)](02-introduction-to-spark.md)
3. [Cài đặt Apache Spark và môi trường PySpark (Installing Spark)](03-installing-spark.md)
4. [Làm quen và chạy thử Spark/PySpark (First Look at Spark/PySpark)](04-first-look-at-spark.md)
5. [Làm việc với Spark DataFrames (Spark DataFrames)](05-spark-dataframes.md)
6. [Chuẩn bị dữ liệu Yellow và Green Taxi (Preparing Taxi Data)](06-preparing-taxi-data.md)
7. [Truy vấn dữ liệu bằng Spark SQL (SQL with Spark)](07-sql-with-spark.md)
8. [Kiến trúc nội bộ của một Cụm Spark (Anatomy of a Spark Cluster)](08-anatomy-of-a-spark-cluster.md)
9. [Bản chất cơ chế GroupBy trong Spark (GroupBy in Spark)](09-groupby-in-spark.md)
10. [Bản chất các phép kết nối Joins trong Spark (Joins in Spark)](10-joins-in-spark.md)
11. [Thao tác với cấu trúc RDD trong Spark (Operations on Spark RDDs - Tùy chọn)](11-operations-on-spark-rdds.md)
12. [Hàm mapPartition trong Spark RDD (Spark RDD mapPartition - Tùy chọn)](12-spark-rdd-mappartition.md)
13. [Kết nối Spark với Google Cloud Storage (Connecting to GCS)](13-connecting-to-google-cloud-storage.md)
14. [Tạo cụm Spark cục bộ (Creating a Local Spark Cluster)](14-creating-a-local-spark-cluster.md)
15. [Khởi tạo và vận hành cụm Google Cloud Dataproc (Dataproc Cluster)](15-setting-up-a-dataproc-cluster.md)
16. [Kết nối Spark trực tiếp với BigQuery (Connecting Spark to BigQuery)](16-connecting-spark-to-bigquery.md)

> [!NOTE]
> Bài 11 và 12 về RDDs là phần nâng cao tùy chọn (vì hầu hết công việc thực tế sử dụng DataFrames), tương tự như phần chuẩn bị dữ liệu taxi trong bài 6 và bài cài đặt Spark trên Linux ở bài 3.

---

## Bài Tập Về Nhà (Homework)

* Kiểm tra đề bài trong thư mục `cohorts/` tương ứng (ví dụ: `cohorts/2026/06-batch/` hoặc `cohorts/2027/`).

---

## Ghi Chú Của Cộng Đồng (Community Notes)

<details>
<summary>Nhấn để xem ghi chú và hướng dẫn từ cộng đồng học viên</summary>

* [Ghi chú từ Alvaro Navas](https://github.com/ziritrion/dataeng-zoomcamp/blob/main/notes/5_batch_processing.md)
* [Blog học tập DE của Sandy: Cài đặt Spark trên Linux](https://learningdataengineering540969211.wordpress.com/2022/02/24/week-5-de-zoomcamp-5-2-1-installing-spark-on-linux/)
* [Ghi chú từ Alain Boisvert](https://github.com/boisalai/de-zoomcamp-2023/blob/main/week5.md)
* [Cách khác: Dùng docker-compose để khởi chạy Spark](https://gist.github.com/rafik-rahoui/f98df941c4ccced9c46e9ccbdef63a03) bởi rafik
* [Bài viết tiếng Tây Ban Nha của Marcos Torregrosa](https://www.n4gash.com/2023/data-engineering-zoomcamp-semana-5-batch-spark)
* [Ghi chú từ Victor Padilha](https://github.com/padilha/de-zoomcamp/tree/master/week5)
* [Ghi chú từ Oscar Garcia](https://github.com/ozkary/Data-Engineering-Bootcamp/tree/main/Step5-Batch-Processing)
* [Ghi chú từ HongWei](https://github.com/hwchua0209/data-engineering-zoomcamp-submission/blob/main/05-batch-processing/README.md)
* [Bản ghi lời thoại video năm 2024](https://drive.google.com/drive/folders/1XMmP4H5AMm1qCfMFxc_hqaPGw31KIVcb?usp=drive_link) bởi Maria Fisher 
* [Ghi chú năm 2025 từ Manuel Guerra](https://github.com/ManuelGuerra1987/data-engineering-zoomcamp-notes/blob/main/5_Batch-Processing-Spark/README.md)
* [Ghi chú năm 2025 từ Gabi Fonseca](https://github.com/fonsecagabriella/data_engineering/blob/main/05_batch_processing/00_notes.md)
* [Cài đặt Spark trên MacOS (Anaconda + brew) bởi Gabi Fonseca](https://github.com/fonsecagabriella/data_engineering/blob/main/05_batch_processing/01_env_setup.md)
* [Ghi chú năm 2025 từ Daniel Lachner](https://github.com/mossdet/dlp_data_eng/blob/main/Notes/05_01_Batch_Processing_Spark_GCP.pdf)
* [Ghi chú năm 2026 từ Ajay Katte](https://github.com/mushroomsandchai/dtdez/tree/main/06_batch_processing/notes)
* [Video cài đặt PySpark trên Windows (không dùng pip install) bởi Khanh](https://www.youtube.com/watch?v=8OYBW4Lwu60)

</details>
