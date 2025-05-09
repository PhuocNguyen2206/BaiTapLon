import requests
from bs4 import BeautifulSoup
import csv
import time

def crawl_baomoi_giaitri():
    base_url = "https://baomoi.com/giai-tri.epi"
    visited = set()
    results = []

    while base_url:
        print(f"Đang xử lý: {base_url}")
        res = requests.get(base_url, timeout=10)
        soup = BeautifulSoup(res.content, "html.parser")

        articles = soup.select("h3 a")
        for a in articles:
            href = a["href"]
            full_link = "https://baomoi.com" + href if href.startswith("/") else href
            if full_link in visited:
                continue
            visited.add(full_link)

            try:
                article_res = requests.get(full_link, timeout=10)
                article_soup = BeautifulSoup(article_res.content, "html.parser")

                title_tag = article_soup.select_one("h1")
                desc_tag = article_soup.select_one("meta[name='description']")
                img_tag = article_soup.select_one("meta[property='og:image']")
                content_paragraphs = article_soup.select("div.article-content p")

                title = title_tag.text.strip() if title_tag else ""
                description = desc_tag["content"].strip() if desc_tag else ""
                image_url = img_tag["content"] if img_tag else ""
                content = "\n".join([p.text.strip() for p in content_paragraphs if p.text.strip()])

                results.append([title, description, image_url, content])
                print("✔ Lấy:", title)
                time.sleep(1)

            except Exception as e:
                print("❌ Lỗi:", e)

        # Lấy link trang tiếp theo
        next_btn = soup.select_one("a.next.page-link")
        if next_btn and "href" in next_btn.attrs:
            base_url = "https://baomoi.com" + next_btn["href"]
            time.sleep(2)
        else:
            break

    # Ghi dữ liệu ra file CSV
    with open("baomoi_giaitri.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Tiêu đề", "Mô tả", "Ảnh", "Nội dung"])
        writer.writerows(results)

    print(f"✅ Đã lưu {len(results)} bài viết vào baomoi_giaitri.csv")

if __name__ == "__main__":
    crawl_baomoi_giaitri()
