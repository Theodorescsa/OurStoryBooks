from django.contrib import admin
from .models import BookModel, PageModel, PurchasedBook

class BookModelAdmin(admin.ModelAdmin):
    # Các trường sẽ hiển thị trong danh sách
    list_display = ('id', 'bookname', 'book_image', 'author', 'pages', 'price', 'published', 'created_at', 'updated_at')

    # Thêm bộ lọc bên phải
    list_filter = ('published', 'author', 'genres')

    # Thêm ô tìm kiếm
    search_fields = ('bookname', 'author', 'description')

    # Sắp xếp các trường trong form chi tiết
    fieldsets = (
        (None, {
            'fields': ('bookname', 'book_image', 'author', 'genres')
        }),
        ('Details', {
            'fields': ('pages', 'price', 'description', 'published')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    # Sử dụng filter_horizontal cho trường ManyToManyField
    filter_horizontal = ('genres',)

    # Tự động chỉ định các trường chỉ để đọc
    readonly_fields = ('created_at', 'updated_at')

    # Thêm hành động để cập nhật giá nhanh
    actions = ['update_price_to_zero']

    def update_price_to_zero(self, request, queryset):
        """Hành động tự động cập nhật giá sách về 0."""
        queryset.update(price=0)
    update_price_to_zero.short_description = "Set price to zero for selected books"

# Register model and admin
admin.site.register(BookModel, BookModelAdmin)
class PageModelAdmin(admin.ModelAdmin):
    # Các trường sẽ hiển thị trong danh sách
    list_display = ('id','book', 'chapter', 'page_number', 'created_at', 'updated_at')

    # Thêm bộ lọc bên phải
    list_filter = ('book', 'page_number')

    # Thêm ô tìm kiếm
    search_fields = ('book__bookname', 'chapter', 'content')

    # Sắp xếp các trường trong form chi tiết
    fieldsets = (
        (None, {
            'fields': ('book', 'chapter', 'page_number', 'content')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    readonly_fields = ('created_at', 'updated_at')

# Register model and admin
admin.site.register(PageModel, PageModelAdmin)
class PurchasedBookAdmin(admin.ModelAdmin):
    # Các trường sẽ hiển thị trong danh sách
    list_display = ('id','user', 'book', 'purchase_date', 'price_at_purchase', 'is_paid')

    # Thêm bộ lọc bên phải
    list_filter = ('purchase_date', 'is_paid', 'book')

    # Thêm ô tìm kiếm
    search_fields = ('user__username', 'book__bookname')

    # Sắp xếp các trường trong form chi tiết
    fieldsets = (
        (None, {
            'fields': ('user', 'book', 'purchase_date', 'price_at_purchase', 'is_paid')
        }),
    )

    # Tự động chỉ định các trường chỉ để đọc
    readonly_fields = ('purchase_date',)

# Register model and admin
admin.site.register(PurchasedBook, PurchasedBookAdmin)
