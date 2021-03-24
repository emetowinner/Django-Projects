from django.shortcuts import render,get_list_or_404
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
        'job':job,
        }
    return render(request,'jobs/detail.html',context)

def update(request, job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully')
            return render(request, 'jobs/update.html', {'form': form})
        else:
            form = PostForm(instance=job)
            messages.error(request, 'Something went wrong try again')
            return render(request, 'jobs/update.html', {'form': form})
    else:
        form = PostForm(instance=job)
        return render(request, 'jobs/update.html', {'form': form})
