from django.shortcuts import render
from django.utils import timezone
from .models import Post, Articleupload, Comment
#from .models import Articleupload
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, CommentForm
#from django.shortcuts import redirect
from tablib import Dataset
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_details.html', {'post' : post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

#def post_draft_list(request):


def simple_upload(request):
    if request.method == 'POST':
        articleupload_resource = ArticluploadResource()
        dataset = Dataset()
        new_articleupload = request.FILES['myfile']

        imported_data = dataset.load(new_articleupload.read())
        result = articleupload_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            articleupload_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'blog/simple_upload.html')


def news(request):
    articles_list = Articleupload.objects.filter(postdate__lte=timezone.now()).order_by('-postdate')[:100]
    paginator = Paginator(articles_list, 15)

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'blog/news.html', {'articles': articles})


def news_detail(request, pk):
    articles = get_object_or_404(Articleupload, pk=pk)
    return render(request, 'blog/news_details.html', {'articles': articles})


def world_news(request):
    articles = Articleupload.objects.filter(subreddit='worldnews').order_by('-postdate')[:15]
    return render(request, 'blog/news.html', {'articles': articles})


def us_news(request):
    articles = Articleupload.objects.filter(subreddit='news').order_by('-postdate')[:15]
    return render(request, 'blog/news.html', {'articles': articles})


def politics_news (request):
    articles = Articleupload.objects.filter(subreddit='Politics').order_by('-postdate')[:15]
    return render(request, 'blog/news.html', {'articles': articles})


def add_comment_to_post(request, pk):
    articles = get_object_or_404(Articleupload, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = articles
            comment.save()
            return redirect('news_detail', pk=articles.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('news_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('news_detail', pk=comment.post.pk)

#@login_required
#def vote_up(request, pk):
#    articles = get_object_or_404(Articleupload, pk=pk)
#    #if not article.votes.exist(Post.author):
#    articles.votes += 1
#    articles.votes.save()
#    return redirect('news')

#def search_form(request):
#    return render(request, 'blog/search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        articles = Articleupload.objects.filter(title__icontains=q).order_by('-postdate')[:15]
        return render(request, 'blog/search_results.html',
                      {'articles': articles, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')