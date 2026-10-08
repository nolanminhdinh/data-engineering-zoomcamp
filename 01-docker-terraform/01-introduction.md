---
next_url: 02-virtual-environment.md
---
# Giới Thiệu Về Docker (Introduction to Docker)

Docker là một phần mềm **đóng gói ứng dụng (containerization software)** cho phép chúng ta cô lập phần mềm tương tự như các máy ảo (virtual machines), nhưng nhẹ hơn và tiết kiệm tài nguyên hơn rất nhiều.

Một **Docker image** là một bản chụp (snapshot/blueprint) của container mà chúng ta định nghĩa để chạy ứng dụng của mình — trong trường hợp của khóa học này là các đường ống dữ liệu (data pipelines). Bằng cách đẩy các Docker images lên các nhà cung cấp đám mây như Amazon Web Services (AWS) hoặc Google Cloud Platform (GCP), chúng ta có thể khởi chạy và vận hành container ở bất cứ đâu.

---

## Tại Sao Nên Dùng Docker? (Why Docker?)

Docker đem lại 3 ưu thế vượt trội:

- **Tính tái lập (Reproducibility)**: Cùng một môi trường thực thi nhất quán ở mọi nơi (máy cá nhân, máy đồng nghiệp, máy chủ test, hay môi trường production).
- **Tính cô lập (Isolation)**: Các ứng dụng chạy độc lập, không xung đột thư viện hay phiên bản phần mềm với nhau.
- **Tính di động (Portability)**: Chạy được trên bất kỳ hệ điều hành nào đã cài đặt Docker (Linux, Windows, macOS).

Docker được ứng dụng rộng rãi trong rất nhiều tình huống thực tế:

- Kiểm thử tích hợp (Integration tests) trong đường ống CI/CD.
- Chạy các pipeline trên Cloud: AWS Batch, Kubernetes jobs.
- Apache Spark: Động cơ phân tích dữ liệu quy mô lớn.
- Kiến trúc Serverless: AWS Lambda, Google Cloud Functions.

---

## Các Lệnh Docker Cơ Bản (Basic Docker Commands)

Kiểm tra phiên bản Docker đã cài đặt:

```bash
docker --version
```

Khởi chạy một container đơn giản để kiểm tra cài đặt:

```bash
docker run hello-world
```

Khởi chạy một hệ điều hành hoàn chỉnh trong container (ví dụ Ubuntu):

```bash
docker run ubuntu
```

Bạn sẽ thấy container thoát ngay lập tức vì không có tiến trình nào chạy ngầm. Để tương tác trực tiếp với container qua dòng lệnh, ta cần thêm cờ `-it` (interactive & tty):

```bash
docker run -it ubuntu
```

Lúc này bạn đã ở bên trong container Ubuntu. Mặc định Ubuntu chưa có sẵn `python`, hãy cài đặt thử:

```bash
apt update && apt install python3
python3 -V
```

---

## Tính Phi Trạng Thái Của Container (Stateless Containers)

> [!IMPORTANT]
> **Điểm cốt lõi:** Các Docker container mang tính **phi trạng thái (stateless)** — mọi thay đổi bạn thực hiện bên trong container sẽ **KHÔNG** được lưu lại khi container bị tắt và khởi động lại mới.

Khi bạn gõ `exit` để thoát container và chạy lại lệnh sau, Python bạn vừa cài đặt sẽ biến mất:

```bash
docker run -it ubuntu
python3 -V
```

Đặc tính này rất an toàn vì nó hoàn toàn cô lập với hệ điều hành máy thật (host system) của bạn. Giả sử bạn lỡ gõ một lệnh phá hủy:

```bash
docker run -it ubuntu
rm -rf / # Tuyệt đối KHÔNG chạy lệnh này trên máy thật của bạn!
```

Thì ở lần khởi chạy tiếp theo, toàn bộ tệp tin của image Ubuntu vẫn nguyên vẹn như ban đầu.

---

## Quản Lý Containers (Managing Containers)

Mặc dù container thoát ra không lưu trạng thái vào image, nhưng thực thể container đã dừng vẫn tồn tại trên ổ cứng. Ta có thể liệt kê tất cả container (kể cả đã tắt):

```bash
docker ps -a
```

Các container đã tắt sẽ chiếm dụng dung lượng ổ cứng. Bạn có thể xóa toàn bộ các container đã dừng bằng lệnh:

```bash
docker rm $(docker ps -aq)
```

Để tự động xóa sạch container ngay sau khi nó dừng chạy, hãy luôn thêm cờ `--rm`:

```bash
docker run -it --rm ubuntu
```

---

## Sử Dụng Các Base Images Khác Nhau (Different Base Images)

Ngoài `hello-world` và `ubuntu`, Docker Hub có hàng ngàn base images chuyên dụng khác. Ví dụ với Python:

```bash
docker run -it --rm python:3.9.16
# Thêm hậu tố -slim để tải phiên bản nhẹ hơn (python:3.9.16-slim)
```

Lệnh trên sẽ mở thẳng trình thông dịch tương tác của `python`. Nếu bạn muốn mở terminal bash của container đó, hãy ghi đè điểm vào (`entrypoint`):

```bash
docker run -it \
    --rm \
    --entrypoint=bash \
    python:3.9.16-slim
```

---

## Cơ Chế Gắn Ổ Đĩa (Volumes)

Như đã biết, container là stateless và độc lập. Vậy làm thế nào để lưu trữ dữ liệu hoặc chia sẻ mã nguồn từ máy thật vào container? Giải pháp chuẩn mực là sử dụng **Volumes** (hoặc Bind Mounts).

Tệp tin từ máy thật (host machine) có thể được chia sẻ vào container thông qua một volume được gắn kết:

![Các tệp tin từ máy thật có thể được chia sẻ với Docker container thông qua ổ đĩa volume gắn kết.](images/docker-volume-mapping.png)

Hãy cùng thực hành tạo một thư mục dữ liệu `test` trên máy thật:

```bash
mkdir test
cd test
touch file1.txt file2.txt file3.txt
echo "Hello from host" > file1.txt
cd ..
```

Tiếp theo, tạo một script Python đơn giản `test/list_files.py` để liệt kê các file trong thư mục:

```python
from pathlib import Path

current_dir = Path.cwd()
current_file = Path(__file__).name

print(f"Files in {current_dir}:")

for filepath in current_dir.iterdir():
    if filepath.name == current_file:
        continue

    print(f"  - {filepath.name}")

    if filepath.is_file():
        content = filepath.read_text(encoding='utf-8')
        print(f"    Content: {content}")
```

Bây giờ, hãy ánh xạ thư mục `test` này từ máy thật vào đường dẫn `/app/test` bên trong container Python:

```bash
docker run -it \
    --rm \
    -v $(pwd)/test:/app/test \
    --entrypoint=bash \
    python:3.9.16-slim
```

Bên trong terminal của container, bạn hãy kiểm tra:

```bash
cd /app/test
ls -la
cat file1.txt
python list_files.py
```

Bạn sẽ thấy toàn bộ tệp tin từ máy chủ thật xuất hiện và có thể truy cập, đọc/ghi bình thường ngay từ trong container!
