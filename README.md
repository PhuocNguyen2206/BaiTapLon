-Cài đặt

Clone project về máy:

git clone https://github.com/ten-ban/baomoi-crawler.git
cd baomoi-crawler

Tạo môi trường ảo (khuyến nghị):

Windows:
python -m venv venv
venv\Scripts\activate

macOS/Linux:
python3 -m venv venv
source venv/bin/activate

-Cài đặt thư viện:

pip install -r requirements.txt

- Cách sử dụng

Chạy thủ công một lần:

python baomoi_giaitri.py

→ Sau khi chạy xong, dữ liệu sẽ được lưu trong file baomoi_giaitri.csv

Chạy tự động mỗi ngày lúc 6:00 sáng:

python scheduler.py
