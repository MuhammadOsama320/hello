from django.shortcuts import render
from django.http import HttpResponse
from home.models import Entry


# Create your views here.
def home(request):
    return render(request, "home.html")


def show(request):
    data = Entry.objects.all()
    return render(request, "show.html", {'data': data})


def send(request):
    if request.method == 'POST':
        ID = request.POST['id']
        data1 = request.POST['data1']
        data2 = request.POST['data2']
        Entry(ID=ID, data1=data1, data2=data2).save()
        msg = "Data Stored Successfully"
        return render(request, "home.html", {'msg': msg})

    else:
        return HttpResponse("<h1> 404 Error</h1>")
