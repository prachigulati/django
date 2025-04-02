from django.shortcuts import render
# from django.http import HttpResponse
# def home(request):
#     return HttpResponse('<h1>Hello World</h1>')

def home(request):
    return render(request,'home.html')
