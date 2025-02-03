from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchasedBook

@receiver(post_save, sender=PurchasedBook)
def update_price_at_purchase(sender, instance, created, **kwargs):
    if created:
        # Nếu là bản ghi mới, lấy giá của sách và cập nhật vào price_at_purchase
        instance.price_at_purchase = instance.book.price
        instance.save()
