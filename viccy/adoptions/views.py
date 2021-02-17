from django.shortcuts import render
from django.http import Http404
from .models import Pet

def home(request):
    pets = Pet.objects.all()
    context = {'pets':pets}
    return render(request,'home.html',context)

def pet_detail(requst,pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found!')
    context = {'pet':pet}
    return render(requst,'pet_detail.html',context)
