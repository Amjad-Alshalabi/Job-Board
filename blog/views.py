from django.shortcuts import render
from .models import Category, blog
from django.core.paginator import Paginator
from django.db.models import Count

# Create your views here.


def post_list(request):

    categoryy = Category.objects.all()
    posts = blog.objects.all()

    recent_posts = blog.objects.filter().order_by('-published_at')[:2]

    posts = blog.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts':page_obj, 'category':categoryy,'all_post':posts,'recent_posts':recent_posts}
    return render(request, 'blog/blog.html', context)

def post_details(request, slug):
    post_details = blog.objects.get(slug = slug)

    recent_posts = blog.objects.filter().order_by('-published_at')[:2]

    return render(request, 'blog/single-blog.html', {'post_details':post_details,'recent_posts':recent_posts})


    
