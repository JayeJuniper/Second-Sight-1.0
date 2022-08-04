from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Sticky/New/', views.sticky_new, name='sticky_new'),
    path('Sticky/<int:pk>/edit/', views.sticky_edit, name='sticky_edit'),
    path('Sticky/<int:pk>/manage/', views.sticky_manage, name='sticky_manage'),
    path('Sticky/<int:pk>/delete/', views.sticky_delete, name='sticky_delete'),
    path('News/', views.news_list, name='news'),
    path('News/<int:pk>/', views.news_detail, name='news_detail'),
    path('News/Post/', views.news_post, name='news_post'),
    path('News/<int:pk>/edit/', views.news_edit, name='news_edit'),
    path('News/<int:pk>/manage/', views.news_manage, name='news_manage'),
    path('News/<int:pk>/delete/', views.news_delete, name='news_delete'),
    path('About/', views.about, name='about'),
    path('Archive/', views.comic_list, name='archive'),
    path('Comic/<int:pk>/', views.comic_detail, name='comic_detail'),
    path('Comic/New/', views.comic_new, name='comic_new'),
    path('Comic/<int:pk>/edit', views.comic_edit, name='comic_edit'),
    path('Extras/', views.extras_list, name='extras'),
    path('Gallery/', views.gallery, name='gallery'),
    path('Gallery/New/', views.gallery_new, name='gallery_new'),
    path('Gallery/<int:pk>/', views.gallery_detail, name='gallery_detail'),
    path('Gallery/<int:pk>/edit/', views.gallery_edit, name='gallery_edit'),
    path('Gallery/<int:pk>/manage/', views.gallery_manage, name='gallery_manage'),
    path('Gallery/<int:pk>/delete/', views.gallery_delete, name='gallery_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
