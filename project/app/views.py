from django.shortcuts import render
from django.http import HttpResponse
from .models import Studentmodel
# Create your views here.
# def home(request):
#     data=Studentmodel.objects.create(
#         Name="neeraj",
#         City="bhopal",
#         Email="indrajeet@gmail.com",
#         Contact="999776855"
#     )
#     print(data)
#     return HttpResponse(data)

def home(request):
    data=Studentmodel.objects.last().delete()
    print(data)
    return HttpResponse(data)
#last()
#get()