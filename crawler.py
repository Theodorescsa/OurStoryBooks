import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def crawl_book_details_selenium(book_url, output_file="book_data.json"):
    """
    Crawler chi tiết sách từ trang Project Gutenberg bằng Selenium và lưu vào file JSON.

    :param book_url: URL trang đọc online
    :param output_file: Tên file JSON để lưu dữ liệu
    :return: None (Lưu file JSON)
    """

    # Khởi tạo trình duyệt Chrome (có thể đổi thành Edge hoặc Firefox)
    driver = webdriver.Chrome()

    try:
        driver.get(book_url)
        time.sleep(3)  # Đợi trang tải hoàn tất
        
        # Lấy tên sách (bookname)
        try:
            bookname = driver.find_element(By.ID, "pg-title-no-subtitle").text.strip()
        except:
            bookname = "Không rõ"

        # Lấy tác giả (author)
        try:
            author_element = driver.find_element(By.XPATH, '//p[strong[contains(text(),"Author")]]')
            author = author_element.text.replace("Author:", "").strip()
        except:
            author = "Không rõ"

        # Lấy ngày phát hành (release date)
        try:
            release_element = driver.find_element(By.XPATH, '//p[strong[contains(text(),"Release date")]]')
            release_date = release_element.text.replace("Release date:", "").strip()
        except:
            release_date = "Không rõ"

        # Lấy toàn bộ nội dung từ <body>
        try:
            body_text = driver.find_element(By.TAG_NAME, "body").text.strip()
        except:
            return {"error": "Không thể lấy nội dung sách."}

        # Xóa phần metadata nếu có
        start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK"
        if start_marker in body_text:
            body_text = body_text.split(start_marker, 1)[-1].strip()

        # Chia nội dung thành các trang 1000 từ
        words = body_text.split()
        pages = [" ".join(words[i:i + 600]) for i in range(0, len(words), 600)]

        # Đánh số trang
        numbered_pages = {f"Trang {i+1}": page for i, page in enumerate(pages)}

        # Tạo dictionary chứa dữ liệu sách
        book_data = {
            "bookname": bookname,
            "author": author,
            "release_date": release_date,
            "content": numbered_pages
        }

        # Lưu dữ liệu vào file JSON
        with open(output_file, "w", encoding="utf-8") as json_file:
            json.dump(book_data, json_file, ensure_ascii=False, indent=4)

        print(f"Dữ liệu đã được lưu vào {output_file}")

    except Exception as e:
        print(f"Lỗi khi crawler: {str(e)}")

    finally:
        driver.quit()  # Đóng trình duyệt khi hoàn thành

# Ví dụ sử dụng
book_url = "https://www.gutenberg.org/ebooks/75705.html.images"  # Thay bằng URL thực tế
crawl_book_details_selenium(book_url)
