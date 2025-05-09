import schedule
import time
from baomoi_giaitri import crawl_baomoi_giaitri

schedule.every().day.at("06:00").do(crawl_baomoi_giaitri)

print("Đang chờ đến 06:00 mỗi ngày để chạy crawl dữ liệu...")
while True:
    schedule.run_pending()
    time.sleep(60)
