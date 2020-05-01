from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("첫번째 만들 웹페이지 입니다!")