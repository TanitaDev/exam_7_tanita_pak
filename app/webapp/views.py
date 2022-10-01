from django.shortcuts import render

from webapp.models import GuestBook


def index_view(request):
    guest_books = GuestBook.objects.order_by('create_at').filter(status="active")
    context = {
        'guest_books': guest_books
    }
    return render(request, 'index.html', context)
