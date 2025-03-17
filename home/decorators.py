from functools import wraps
from django.http import JsonResponse
from django.shortcuts import redirect
from .models import PurchasedBook, BookModel  # Ensure these models are correctly imported
from .serializers import PurchasedBookSerializer

def check_payment_status(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        book_id = kwargs.get('book_id')  # Assuming book_id is passed in the URL
        user = request.user

        if not user.is_authenticated:
            return JsonResponse({"error": "Authentication required."}, status=401)

        try:
            book = BookModel.objects.get(id=book_id)  # Check if the book exists
            purchase, created = PurchasedBook.objects.get_or_create(user=user, book=book)  # Get the purchase record

            if not purchase.is_paid:  # If not paid, redirect to payment page
                return redirect(f"/payment/payment/?book_id={book_id}&price={book.price}")

        except BookModel.DoesNotExist:
            return JsonResponse({"error": "Book not found."}, status=404)
        except PurchasedBook.DoesNotExist:
            return JsonResponse({"error": "No purchase record found."}, status=404)

        return view_func(request, *args, **kwargs)  # Proceed if paid
    return _wrapped_view
