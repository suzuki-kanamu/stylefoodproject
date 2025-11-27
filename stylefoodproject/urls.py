from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('book/', views.reserve_view, name='book'),
    path('takeout/', views.takeout, name='takeout'),
    path('contact/', views.contact, name='contact'),
    path('reserve/', views.reserve_view, name='reserve'),
    path('thanks/', views.thanks, name='thanks'),
    path('review/', views.review, name='review'),
]