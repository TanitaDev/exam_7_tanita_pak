from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import GuestBook
from webapp.forms import *


def index_view(request):
    guest_books = GuestBook.objects.order_by('create_at').filter(status="active")
    context = {
        'guest_books': guest_books
    }
    return render(request, 'index.html', context)


def add_entry_view(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            try:
                GuestBook.objects.create(**form.cleaned_data)
                return redirect('index')
            except:
                form.add_error(None, 'Ошибка добавления поста')

    else:
        form = EntryForm()
    context = {
        'form': form,
    }
    return render(request, 'add_entry.html', context)


def edit_entry_view(request):
    pass
