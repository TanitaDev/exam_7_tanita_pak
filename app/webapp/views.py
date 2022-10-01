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


def edit_entry_view(request, pk):
    guest_book = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        return render(request, 'edit_entry.html', context={'guest_book': guest_book})
    elif request.method == 'POST':
        guest_book.name = request.POST.get('name')
        guest_book.mail = request.POST.get('mail')
        guest_book.text = request.POST.get('text')
        guest_book.save()
        return redirect('index', pk=guest_book.pk)


def delete_entry_view(request, pk):
    guest_book = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'guest_book': guest_book})
    elif request.method == 'POST':
        guest_book.delete()
        return redirect('index')
