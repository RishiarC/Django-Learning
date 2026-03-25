from django.shortcuts import render
from .models import chaiVarity


def all_chai(request):
    chais=chaiVarity.objects.all()
    return render(request,'arogya/all_chai.html', {'chais': chais})

# Create your views here.
