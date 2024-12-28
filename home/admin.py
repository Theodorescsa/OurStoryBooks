from django.contrib import admin
from .models import BookModel, PageModel

class BookModelAdmin(admin.ModelAdmin):
    # Các trường sẽ hiển thị trong danh sách
    list_display = ('bookname','book_image', 'author', 'pages','price', 'published', 'created_at', 'updated_at')
    
    # Thêm bộ lọc bên phải
    list_filter = ('published', 'author')
    
    # Thêm ô tìm kiếm
    search_fields = ('bookname', 'author', 'description')
    
    # Sắp xếp các trường trong form chi tiết
    fieldsets = (
        (None, {
            'fields': ('bookname','book_image', 'author', 'genres')
        }),
        ('Details', {
            'fields': ('pages','price', 'description', 'published')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    
    # Sử dụng filter_horizontal cho trường ManyToManyField
    filter_horizontal = ('genres',)
    
    # Tự động chỉ định các trường chỉ để đọc
    readonly_fields = ('created_at', 'updated_at')
    
admin.site.register(BookModel, BookModelAdmin)
admin.site.register(PageModel)