from django.shortcuts import render
from .models import Book
from django.http import Http404
from django.db.models import Avg

# Create your views here.
def index(request):
    try:
        books = Book.objects.all().order_by('-rating')
        num_books = books.count()
        avg_rating = books.aggregate(Avg('rating'))
    except:
        raise Http404()    
    return render(request,"book_outlet/index.html",{'books':books,
    "total_number_of_books":num_books,
    "average_rating":avg_rating})

def book_detail(request,slug):
    book = Book.objects.get(slug=slug)
    return render(request,"book_outlet/book_detail.html",{
        "title":book.title,
        "author":book.author,
        "rating":book.rating,
        "is_bestseller":book.is_bestselling,
    })    