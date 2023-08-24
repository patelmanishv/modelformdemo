from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.BookCreateView.as_view(), name='book_add'),
]