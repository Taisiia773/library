from django.shortcuts import render

# Create your views here.


def showauthor(request):
    return render(request, "author.html")

