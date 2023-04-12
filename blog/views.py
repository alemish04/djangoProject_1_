from django.views.generic import ListView, DetailView, TemplateView  # НЕ используем(пока что), может быть будем позже
from .models import Post, Category
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator


def post_list(request):  # отображение списка постов
    # поиск, проверка, был лы запрос с ключом search, сбор и фильтрация постов
    # на этом основании
    search_query = request.GET.get("search", '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()

    # отображение нужного кол-ва постов на странице и пагинаторов
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page", 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = "?page={}".format(page.previous_page_number())
    else:
        prev_url = ""

    if page.has_next():
        next_url = "?page={}".format(page.next_page_number())
    else:
        next_url = ""
    # отображение нужного кол-ва постов на странице и пагинаторов
    categories = Category.objects.all()
    context = {
        "posts": page,
        "is_paginated": is_paginated,  # собираем словарь свойств, которые передаём на рендер
        "next_url": next_url,
        "prev_url": prev_url,
        "categories": categories
    }
    return render(request, "index.html", context=context)


def post_detail(request, id):
    post = Post.objects.get(id__iexact=id)
    return render(request, 'post_detail.html', context={'post': post})


def category_list(request):
    categories = Category.objects.all()
    return render(request, "categories_list.html", context={"categories": categories})


def category_detail(request, id):
    category = Category.objects.get(id__iexact=id)
    categories = Category.objects.all()
    return render(request, "category_detail.html", context={"category": category, "categories": categories})


def about_project(request):
    categories = Category.objects.all()
    return render(request, "about.html", context={"categories": categories})
