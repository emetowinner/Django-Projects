from django.shortcuts import render,get_list_or_404,redirect
from django.contrib import messages
from .models import Job
from .forms import PostForm

def home(request):
    jobs = Job.objects.all()
    context = {'jobs':jobs}
    return render(request,'jobs/home.html',context)

def detail_view(request,job_id):
    job = get_list_or_404(Job,pk=job_id)
    job[0].view_count += 1
    job[0].save()   
    context = {
        'jobs':job,
        }
    return render(request,'jobs/detail.html',context)

def update(request,id=0):
    if request.method == 'GET':
        if id==0:
            form = PostForm()
            context = {'form':form,}
        else:
            job = Job.objects.get(pk=id)
            form = PostForm(instance=job)
            context = {'form':form,}

        return render(request,'jobs/update.html',context)
    else:
        if id==0:
            form = PostForm(request.POST,request.FILES)
        else:
            job = Job.objects.get(pk=id)
            form = PostForm(request.POST,request.FILES,instance=job)

        if form.is_valid():
            print('It got to this point o')
            form.save()
        return redirect('home')

def delete_job(request,id):
    job = Job.objects.get(pk=id)
    job.delete()
    return redirect('home')
