from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from math import ceil
# Create your views here.
def index(request):
    # books = Book.objects.all()
    # print(books)
    # n = len(books)
    # nSlides = n//4 + ceil((n/4) + (n//4))
    allBooks = []
    catbooks = Book.objects.values('category', 'id')
    cats = {item['category'] for item in catbooks }
    for cat in cats:
        bookk = Book.objects.filter(category = cat)
        n = len(bookk)
        nSlides = (n // 4 + ceil((n / 4) - (n // 4)))
        allBooks.append([bookk, range(1,nSlides), nSlides])
    # params = {'no_of_slide':nSlides, 'range' : range(1,nSlides), 'book' : books}
    # allBooks = [[books,range(1,nSlides),nSlides], [books,range(1,nSlides),nSlides]]
    params ={'allBooks' : allBooks }
    return render(request, 'shop/index.html', params )

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact page")

def tracker(request):
    return HttpResponse("We are at tracker page")

def search(request):
    return HttpResponse("We are at search page")

def productView(request):
    return HttpResponse("We are at product view page")

def checkout(request):
    return HttpResponse("We are at checkout page")
