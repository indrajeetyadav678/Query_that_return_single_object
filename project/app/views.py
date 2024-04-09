from django.shortcuts import render
from django.http import HttpResponse
from .models import Studentmodel,Marksheetmodel
# Create your views here.
def home(request):
    data=Studentmodel.objects.create(
        Name="Mohan singh",
        City="Gujrat",
        Email="gaurav@gmail.com",
        Contact="7888283663"
    )
    print(data)
    return HttpResponse(data)

# def home1(request):
#     data=Studentmodel.objects.filter(Name="neeraj").delete()
#     print(data)
#     return HttpResponse(data)
# def home1(request):
#     data=Studentmodel.objects.first()
#     print(data)
#     return HttpResponse(data)
# def home1(request):
#     data=Studentmodel.objects.last()
#     print(data)
#     return HttpResponse(data)
# def home(request):
#     data=Studentmodel.objects.filter(Name="Gaurav").update(
#         Name="Saurav",
#         Contact="788828366300000"
#     )
#     print(data)
#     return HttpResponse(data)

# def home(request):
#     data=Studentmodel.objects.filter(Name="Mohan singh").delete()
#     print(data)
#     return HttpResponse(data)
#last()
#get()

# ========================================MarksheetModel  =================================
# def mark(request):
#     data=Marksheetmodel.objects.create(
#         Name="indrajeet",

#     )