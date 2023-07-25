from django.shortcuts import render
from .models import Person,Runner,Fruit
from  django.shortcuts   import get_object_or_404
# Create your views here.
from django.http import HttpResponse

def detail(request):
    #person=get_object_or_404(Person)
    p=Person.objects.filter(shirt_size="Large")
    print(p)

    return HttpResponse(f"Your are looking t person ",p)

    
def runner(request):
    Run=get_object_or_404(Runner)
    return HttpResponse("runner")

def fruit(request,fruit_id):
    fr=get_object_or_404(Fruit,pk=fruit_id)
    return HttpResponse("fruit",fr)