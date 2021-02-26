from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from .models import Job

def home(request):
    jobs = Job.objects.all()
    context = {'jobs':jobs}
    return render(request,'jobs/home.html',context)

def detail_view(request,job_id):
    job = get_list_or_404(Job,pk=job_id)
    print(job)
    context = {'job':job}
    return render(request,'jobs/detail.html',context)
