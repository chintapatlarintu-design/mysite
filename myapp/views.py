from django.shortcuts import render
from django.http import HttpResponse
from .models import Item


# Create your views here.
def index(request):
    #Geting item list from database
    item_list = Item.objects.all()
    #Creating context dictionary to pass to template
    context = {'item_list': item_list}
    # Passing the contest object to the render method along with the template name
    return render(request, 'myapp/index.html',context )

def details(request,id):
    item = Item.objects.get(id=id)
    context = {'item': item}
    return render(request, 'myapp/detail.html',context)



def item (request):
    return HttpResponse("<h1>You are looking at item </h1>")



