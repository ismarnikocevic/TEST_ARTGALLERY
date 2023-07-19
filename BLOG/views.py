from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import  BlogPostForm
from django.views.generic import UpdateView
from django.contrib import messages
from django.shortcuts import render, HttpResponse
from datetime import datetime




def home(request):
    return render(request, 'home.html', locals())


def blogslist(request):
    posts = BlogPost.objects.all()
    posts = BlogPost.objects.filter().order_by('-dateTime')
    return render(request, "blog.html", {'posts':posts})

def blogs_detail(request, id):
    post = BlogPost.objects.filter(id=id).first()
   
    if request.method=="POST":
        user = request.user
        content = request.POST.get('content','')
        blog_id =request.POST.get('blog_id','')
        post = BlogPost(user = user, content = content, blog=post)
        post.save()
    return render(request, "blogs_detail.html", {'post':post})

def Delete_Blog_Post(request, id):
    posts = BlogPost.objects.get(id=id)
    if request.method == "POST":
        posts.delete()
        return redirect('/blogslist')
    return render(request, 'delete_blog_post.html', {'posts':posts})

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        blogs = BlogPost.objects.filter(title__contains=searched)
        return render(request, "search.html", {'searched':searched, 'blogs':blogs})
    else:
        return render(request, "search.html", {})

@login_required(login_url = '/login')
def add_blogs(request):
    if request.method=="POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return render(request, "add_blogs.html",{'obj':obj, 'alert':alert})
    else:
        form=BlogPostForm()
    return render(request, "add_blogs.html", {'form':form})

class UpdatePostView(UpdateView):
    model = BlogPost
    template_name = 'edit_blog_post.html'
    fields = ['title',  'content', 'image']











def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login')



def biography(request):
    return render(request, 'biography.html', locals())

