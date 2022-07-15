from unicodedata import name
from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('add/',views.AddBook.as_view(),name='add'),
    path('detail/<int:pk>/',views.BookDetail.as_view(),name='detail'),
    path('update/<int:pk>/',views.UpdateBook.as_view(),name='update'),
    path('delete/<int:pk>/',views.DeleteBook.as_view(),name='delete'),
]