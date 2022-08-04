from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.forms.models import model_to_dict
from django.utils import timezone

from . import models
from . import forms


#GLOBALS


# index View
def index(request):
    post = []
    all_posts = models.Newspost.objects.filter(Q(manage__contains='s') 
        | Q(manage__contains='d')).order_by('-id')
    for i in all_posts:
        post.append(i)

    comics = []
    all_comics = models.Comic.objects.all().order_by('id')
    for comic in all_comics:
        comics.append(comic)

    sticky = []
    all_posts2 = models.Sticky.objects.all().order_by('id')
    for i in all_posts2:
        sticky.append(i)

    first = []
    first_comic = models.Comic.objects.all().order_by('page_number')
    for i in first_comic:
        first.append(i)

    last = []
    last_comic = models.Comic.objects.all().order_by('-page_number')
    for i in last_comic:
        last.append(i)

    cover_banner = []
    banners= models.CoverBanner.objects.all().order_by('-id')
    for i in banners:
        cover_banner.append(i)

    return render(request, 'secondsight/index.html', {
                    'post': post[0],
                    'comics': comics,
                    'sticky': sticky,
                    "first": first[0],
                    "last": last[0],
                    "cover_banner": cover_banner[0]
                    })

# New Sticky
def sticky_new(request):
    title = 'Submit a New Sticky.'
    if request.method == "POST":
        form = forms.StickyForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_date = timezone.now()
            form.save()
            return redirect('index')
    else:
        form = forms.StickyForm()
    return render(request, 'secondsight/new.html', {
                    'form': form,
                    'title': title
                    })

def sticky_edit(request, pk):
    title = 'Edit Post'
    post = get_object_or_404(models.Sticky, pk=pk)
    form = forms.StickyForm(instance=post)
    if request.method == "POST":
        form = forms.StickyForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('sticky_manage', pk)
    return render(request, 'secondsight/new.html', {
                    'form': form,
                    'title': title
                    })

def sticky_manage(request, pk):
    sticky = model_to_dict(get_object_or_404(models.Sticky, pk=pk))
    return render(request, 'secondsight/sticky_manage.html',{
                    "sticky": sticky,
                    })

def sticky_delete(request, pk):
    sticky = get_object_or_404(models.Sticky, pk=pk)
    sticky.delete()
    return redirect('index')


# News View
def news_list(request):
    """List the 10 most recent News Posts"""
    posts = []
    all_posts = models.Newspost.objects.all().order_by('-id')[:10]
    for post in all_posts:
        posts.append(post)

    comics = []
    all_comics = models.Comic.objects.all().order_by('id')
    for comic in all_comics:
        comics.append(comic)

    first = []
    first_comic = models.Comic.objects.all().order_by('page_number')
    for i in first_comic:
        first.append(i)

    last = []
    last_comic = models.Comic.objects.all().order_by('-page_number')
    for i in last_comic:
        last.append(i)

    sticky = []
    all_posts2 = models.Sticky.objects.all().order_by('id')
    for i in all_posts2:
        sticky.append(i)
    return render(request, 'secondsight/news_list.html', {
                    'posts': posts,
                    'comics': comics,
                    "first": first[0],
                    "last": last[0],
                    'sticky': sticky
                    })

# news detail view
def news_detail(request, pk):
    post = model_to_dict(get_object_or_404(models.Newspost, pk=pk))
    comics = models.Comic.objects.all(
            ).filter(Q(group_id__exact=post['group_id']))

    first = []
    first_comic = models.Comic.objects.all().order_by('page_number')
    for i in first_comic:
        first.append(i)

    last = []
    last_comic = models.Comic.objects.all().order_by('-page_number')
    for i in last_comic:
        last.append(i)

    return render(request, 'secondsight/news_detail.html',{
                    "post": post,
                    "comics": comics,
                    "first": first[0],
                    "last": last[0]
                    })

# news new/edit/delete
def news_post(request):
    title = 'Submit an Update.'
    if request.method == "POST":
        form = forms.NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_date = timezone.now()
            form.save()
            return redirect('news')
    else:
        form = forms.NewsForm()
    return render(request, 'secondsight/new.html', {
                    'form': form,
                    'title': title
                    })

def news_edit(request, pk):
    title = 'Edit Post'
    post = get_object_or_404(models.Newspost, pk=pk)
    form = forms.NewsForm(instance=post)
    if request.method == "POST":
        form = forms.NewsForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('news_manage', pk)
    return render(request, 'secondsight/new.html', {
                    'form': form,
                    'title': title
                    })

def news_manage(request, pk):
    post = model_to_dict(get_object_or_404(models.Newspost, pk=pk))
    return render(request, 'secondsight/news_manage.html',{
                    "post": post,
                    })

def news_delete(request, pk):
    post = get_object_or_404(models.Newspost, pk=pk)
    post.delete()
    return redirect('news')

# About View
def about(request):
    users = []
    all_users = models.User.objects.all().order_by('id')
    for user in all_users:
        users.append(user)

    sticky = []
    all_posts2 = models.Sticky.objects.all().order_by('id')
    for i in all_posts2:
        sticky.append(i)

    first = []
    first_comic = models.Comic.objects.all().order_by('page_number')
    for i in first_comic:
        first.append(i)

    last = []
    last_comic = models.Comic.objects.all().order_by('-page_number')
    for i in last_comic:
        last.append(i)

    return render(request, 'secondsight/about.html', {
                    'users': users,
                    "first": first[0],
                    "last": last[0],
                    'sticky': sticky
                    })

# Archive View
def comic_list(request):
    chapters = models.Chapter.objects.all().order_by('id')

    first = []
    first_comic = models.Comic.objects.all().order_by('page_number')
    for i in first_comic:
        first.append(i)

    last = []
    last_comic = models.Comic.objects.all().order_by('-page_number')
    for i in last_comic:
        last.append(i)

    return render(request, 'secondsight/comic_list.html', {
                    'chapters': chapters,
                    "first": first[0],
                    "last": last[0]
                    })

def comic_detail(request, pk):
    comic = models.Comic.objects.get(id=pk)

    previous = models.Comic.objects.filter(Q(page_number__lt=comic.page_number) | Q(page_number=comic.page_number, id__lt=comic.id))
    if previous:
        previous = previous.order_by("-page_number", "id")[0]

    next = models.Comic.objects.filter(Q(page_number__gt=comic.page_number) | Q(page_number=comic.page_number, id__gt=comic.id))
    if next:
        next = next.order_by("page_number", "id")[0]

    first = []
    first_comic = models.Comic.objects.all().order_by('page_number')
    for i in first_comic:
        first.append(i)

    last = []
    last_comic = models.Comic.objects.all().order_by('-page_number')
    for i in last_comic:
        last.append(i)

    return render(request, 'secondsight/comic_detail.html',{
                    "comic": comic,
                    "first": first[0],
                    "last": last[0],
                    "previous": previous,
                    "next": next
                    })

# comic new/edit/delete
def comic_new(request):
    title = 'Submit a New Comic Page.'
    if request.method == "POST":
        form = forms.ComicForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_date = timezone.now()
            form.save()
            return redirect('archive')
    else:
        form = forms.ComicForm()
    return render(request, 'secondsight/new.html', {
                    'form': form,
                    'title': title
                    })

def comic_edit(request, pk):
    title = 'Edit Comic'
    post = get_object_or_404(models.Comic, pk=pk)
    form = forms.ComicForm(instance=post)
    if request.method == "POST":
        form = forms.ComicForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('archive')
    return render(request, 'secondsight/new.html', {
                    'form': form,
                    'title': title
                    })

# Extras View
def extras_list(request):
    images = []

    all_images = models.Image.objects.all().order_by('-id')[:7]
    for image in all_images:
        images.append(image)

    first = []
    first_comic = models.Comic.objects.all().order_by('page_number')
    for i in first_comic:
        first.append(i)

    last = []
    last_comic = models.Comic.objects.all().order_by('-page_number')
    for i in last_comic:
        last.append(i)

    return render(request, 'secondsight/extras_list.html', {
                    'images': images,
                    "first": first[0],
                    "last": last[0]
                    })

def gallery(request):
    images = []

    all_images = models.Image.objects.all().order_by('-id')
    for image in all_images:
        images.append(image)

    first = []
    first_comic = models.Comic.objects.all().order_by('page_number')
    for i in first_comic:
        first.append(i)

    last = []
    last_comic = models.Comic.objects.all().order_by('-page_number')
    for i in last_comic:
        last.append(i)

    return render(request, 'secondsight/extras_gallery.html', {
                    'images': images,
                    "first": first[0],
                    "last": last[0]
                    })

#not implemented
def gallery_detail(request, pk):
    image = model_to_dict(get_object_or_404(models.Image, pk=pk))
    return render(request, 'secondsight/gallery_detail.html',{
                    "image": image
                    })

def gallery_new(request):
    title = 'Submit New Artwork.'
    if request.method == "POST":
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_date = timezone.now()
            form.save()
            return redirect('gallery')
    else:
        form = forms.ImageForm()
    return render(request, 'secondsight/new.html', {
                    'form': form,
                    'title': title
                    })

#not implemented
def gallery_edit(request, pk):
    title = 'Edit Art'
    image = get_object_or_404(models.Image, pk=pk)
    form = forms.ImageForm(instance=image)
    if request.method == "POST":
        form = forms.ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            image = form.save(commit=False)
            image.save()
            return redirect('gallery_manage', pk)
    return render(request, 'secondsight/new.html', {
                    'form': form,
                    'title': title
                    })

#not implemented
def gallery_manage(request, pk):
    image = model_to_dict(get_object_or_404(models.Imagepost, pk=pk))
    return render(request, 'secondsight/gallery_manage.html',{
                    "image": image,
                    })

#not implemented
def gallery_delete(request, pk):
    image = get_object_or_404(models.Image, pk=pk)
    image.delete()
    return redirect('gallery')