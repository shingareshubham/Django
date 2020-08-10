from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    """Home page"""
    # return render(request: HttpRequest("Hello world")))
    return HttpResponse('Hello, World!')