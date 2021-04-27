from django.shortcuts import render
from . import models

def home_view(request):
    usecases = models.UserCase.objects.all()
    ui_project = models.UIProject.objects.all()
    personal_data = models.PersonalData.objects.get(id=1)
    asset = models.Assets.objects.get(id=1)
    context = {
        'title':'Omah - (index)',
        'usecases': usecases,
        'UIProject':ui_project,
        'personalData': personal_data,
        'asset':asset,
    }
    return render(request,'portfolio/index.html',context)

def about_view(request):
    asset = models.Assets.objects.get(id=1)
    personal_data = models.PersonalData.objects.get(id=1)
    context = {
        'title':'Omah - (About)',
        'personalData': personal_data,
        'asset':asset,
    }
    return render(request,'portfolio/about.html',context)

def portfolio_detail_view(request):
    context = {}
    return render(request,'portfolio/portfolio-detail.html',context)
