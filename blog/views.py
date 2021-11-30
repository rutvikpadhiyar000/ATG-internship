from .models import BlogPost
from django.db import reset_queries
from django.http import request
from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.


def blog_home(request):

    all_posts = BlogPost.objects.filter(is_ready=True)

    return render(request, 'blog/blog.html', {'all_posts': all_posts[::-1]})


def view_post(request, post_id):
    context = {}
    post = BlogPost.objects.get(id=post_id)
    context['post'] = post
    return render(request, 'blog/post.html', context)


def user_blog(request, username):

    user = request.user
    if user.is_authenticated:
        if user.profile.is_doctor:
            if user.username == username:
                all_posts = BlogPost.objects.filter(author=user)
                return render(request, 'blog/user_blog.html', {'all_posts': all_posts[::-1]})
    return redirect('blog_home')


def create_post(request, is_ready=True):
    if request.method == 'POST':

        if request.user.profile.is_doctor:

            title = request.POST['post-title']
            author = request.user
            image = request.POST['post-image']
            summary = request.POST['post-summary']
            content = request.POST['post-content']
            catag = request.POST['post-catagory']
            BlogPost.objects.create(
                title=title,
                author=author,
                image=image,
                summary=summary,
                content=content,
                catagory=catag,
                is_ready=is_ready
            )
        return redirect(f'/blog/{request.user.username}')

    if request.user.profile.is_doctor:
        return render(request, 'blog/create_post.html')

    return redirect('blog_home')


def create_draft(request, post_id=None):
    if post_id is not None:
        return edit_post(request, post_id=post_id, is_ready=False)
    return create_post(request, is_ready=False)


def edit_post(request, post_id=None, is_ready=True):

    try:
        post = BlogPost.objects.get(id=post_id)
    except BlogPost.DoesNotExist:
        return redirect('/blog')

    if request.method == 'POST':

        title = request.POST['post-title']
        author = request.user
        image = request.POST['post-image']
        summary = request.POST['post-summary']
        content = request.POST['post-content']
        try:
            catag = request.POST['post-catagory']
        except MultiValueDictKeyError:
            catag = post.catagory
        if post.author == author:
            post.title = title
            post.author = author
            post.image = image or post.image
            post.summary = summary
            post.content = content
            post.catagory = catag
            post.is_ready = is_ready
            post.save()
        return redirect('/blog')
    if request.user.profile.is_doctor:
        return render(request, 'blog/create_post.html')

    return redirect('blog_home')


def delete_post(request, post_id):
    if request.user.is_authenticated:
        post = BlogPost.objects.filter(author=request.user, id=post_id)
        if post:
            post.delete()
        return redirect(f'/blog/{request.user.username}')
    return redirect('/blog')
