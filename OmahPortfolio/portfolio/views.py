from django.shortcuts import render

def home_view(request):
    context = {}
    return render(request,'portfolio/index.html',context)

def about_view(request):
    context = {}
    return render(request,'portfolio/about.html',context)

def portfolio_detail_view(request):
    context = {}
    return render(request,'portfolio/portfolio-detail.html',context)
