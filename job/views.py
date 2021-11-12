from django.contrib.auth import login
from django.db.models import query
from django.http import request
from django.shortcuts import redirect, render
from .models import Job, apply
from django.core.paginator import Paginator
from .form import AddForm, ApplyForm
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
# Create your views here.


def job_list(request):

    job_list = Job.objects.all()
    job_list2 = Job.objects.all()
    myfilter = JobFilter(request.GET, queryset=job_list2)
    job_list2 = myfilter.qs

    paginator = Paginator(job_list2, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs' : page_obj, 'jo':job_list, 'myfilter':myfilter}
    
    return render(request, 'job/job_list.html', context)


def job_details(request, slug):
    job_details = Job.objects.get(slug = slug)
    if request.method == "POST":
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_details
            myform.save()
            # print("amjaaaaaaaaaad",myform.created_at)
    else:
        form = ApplyForm()

    context = {'jobs' : job_details, 'form': form}
    return render(request, 'job/job_details.html', context)



@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        myform = form.save(commit=False)
        myform.owner = request.user
        myform.save()
        return redirect('job:job_list')
    else:
        form = AddForm()

    return render(request, 'job/add_job.html', {'form': form})