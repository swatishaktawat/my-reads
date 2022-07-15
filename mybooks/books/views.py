from django.urls import reverse_lazy
from .models import Book
from django.views.generic import CreateView, ListView, UpdateView, DetailView,DeleteView

class Index(ListView):
    model = Book
    template_name = 'books/index.html'

class AddBook(CreateView):
    model = Book
    fields = "__all__"

class UpdateBook(UpdateView):
    model = Book
    fields = ['status','description']
    
class BookDetail(DetailView):
    model = Book

class DeleteBook(DeleteView):
    model = Book
    success_url = reverse_lazy('books:index')

