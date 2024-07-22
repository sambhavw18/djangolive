from django.shortcuts import render,HttpResponse

# Create your views here.
def views(request):
    return HttpResponse("<h1>Hello World</h1>")