from django.shortcuts import redirect, render
from .models import Book

def index(request):
    mem=Book.objects.all()
    return render(request,'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['BookName']
    y=request.POST['AuthorName']
    z=request.POST['Price']
    mem=Book(BookName=x,AuthorName=y,Price=z)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Book.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Book.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['BookName']
    y=request.POST['AuthorName']
    z=request.POST['Price']
    mem=Book.objects.get(id=id)
    mem.BookName=x
    mem.AuthorName=y
    mem.Price=z
    mem.save()
    return redirect("/")
