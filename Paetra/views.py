from django.shortcuts import render

# Create your views here.
from . models import Person
def create_person(request):
    person = Person.objects.create(
        Hair = 'black',
        Complexion = 'Light',
        Height = 'Medium',
    )

    context ={
        'data':person,
    }

    return render(request,'index.html',context)