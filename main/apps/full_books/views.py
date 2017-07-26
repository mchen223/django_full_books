# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Book
from django.contrib import messages

def index(request):
    context = {
    "books": Book.objects.all()}
    return render(request, 'full_books/index.html', context)

def create(request):
    if len(Book.objects.filter(title=request.POST['title'])) > 0:
        messages.error(request, 'Already a book by that name!')
    else:
        Book.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
        messages.success(request, 'Adding a book to the shelf!')
    return redirect("/")
