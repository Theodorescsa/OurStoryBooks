import json
from django.core.exceptions import ObjectDoesNotExist
from home.models import BookModel, PageModel  # Thay 'myapp' bằng tên ứng dụng Django của bạn

def import_books_from_json(json_file):
    """
    Import dữ liệu sách từ file JSON vào database Django.
    
    :param json_file: Đường dẫn file JSON chứa dữ liệu sách.
    :return: None
    """
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Kiểm tra dữ liệu JSON
    if not isinstance(data, dict) or "bookname" not in data or "content" not in data:
        print("Dữ liệu JSON không hợp lệ!")
        return

    # Tạo hoặc lấy sách từ database
    book, created = BookModel.objects.get_or_create(
        bookname=data["bookname"],
        defaults={
            "author": data.get("author", "Unknown"),
            "pages": len(data["content"]),  # Số trang theo JSON
            "description": f"Imported from Project Gutenberg on {data.get('release_date', 'Unknown')}",
            "published": None,  # Nếu có ngày, chuyển đổi sang DateField
            "price": 0.0,  # Giá mặc định
        }
    )

    # Thêm các trang sách vào database
    pages_to_create = []
    for page_num, content in data["content"].items():
        try:
            page_number = int(page_num.replace("Trang ", "").strip())  # Lấy số trang
        except ValueError:
            continue  # Bỏ qua nếu không lấy được số

        # Kiểm tra xem trang đã tồn tại chưa
        if not PageModel.objects.filter(book=book, page_number=page_number).exists():
            pages_to_create.append(
                PageModel(book=book, page_number=page_number, content=content)
            )

    # Thêm toàn bộ trang vào database một lần (tối ưu)
    if pages_to_create:
        PageModel.objects.bulk_create(pages_to_create)
        print(f"Đã thêm {len(pages_to_create)} trang vào sách '{book.bookname}'.")

    print(f"Import thành công sách: {book.bookname} - Tổng số trang: {book.pages}")

# Gọi hàm import với file JSON đã crawl được
import_books_from_json("book_data.json")
