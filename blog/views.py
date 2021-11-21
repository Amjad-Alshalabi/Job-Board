from django.shortcuts import render, redirect
from .models import  Post, Comments
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib.auth.decorators import login_required
import datetime
from .forms import NewCommentForm, NewPostForm
from django.shortcuts import get_object_or_404

# Create your views here.


def post_list(request):

    all_posts = Post.objects.all()

    recent_posts = Post.objects.filter().order_by('-published_at')[:4]

    

    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts':page_obj,'all_post':all_posts,'recent_posts':recent_posts}
    return render(request, 'blog/blog.html', context)




@login_required
def post_details(request, slug):
	post_details = get_object_or_404(Post, slug=slug)
    # comm = 
    # post_details = Post.objects.get(slug = slug)
	user = request.user
	recent_posts = Post.objects.filter().order_by('-published_at')[:4]
	if request.method == 'POST':
		form = NewCommentForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			data.post = post_details
			data.owner = user
			data.save()
			return redirect('blog:post_details', slug = slug)
	else:
		form = NewCommentForm()
	return render(request, 'blog/single-blog.html', {'post_details':post_details, 'form':form, 'recent_posts':recent_posts})




@login_required
def add_post(request):
    user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            data = form.save(commit = False)
            data.owner = user
            data.save()
            return redirect('blog:posts_list')
    else:
        form = NewPostForm()
    return render(request, 'blog/add_post.html', {'form':form})