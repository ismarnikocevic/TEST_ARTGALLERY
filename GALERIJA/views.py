from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import GalleryForm
from django.views.generic import UpdateView
from django.contrib import messages


def paintingslist(request):
    posts = Gallery.objects.all()
    posts = Gallery.objects.filter().order_by('-dateTime')
    return render(request, "painting.html", {'posts':posts})

def paintings_detail(request, id):
    post = Gallery.objects.filter(id=id).first()
   
    if request.method=="POST":
        user = request.user
        content = request.POST.get('content','')
        blog_id =request.POST.get('blog_id','')
        post = Gallery(user = user, content = content, blog=post)
        post.save()
    return render(request, "paintings_detail.html", {'post':post })

def Delete_Paintings(request, id):
    posts = Gallery.objects.filter(id=id)
    if request.method == "POST":
        posts.delete()
        return redirect('/paintingslist')
    return render(request, 'delete_paintings.html', {'posts':posts})

def ART_SEARCH(request):
    if request.method == "POST":
        searched = request.POST['searched']
        paintingslist = Gallery.objects.filter(title__contains=searched)
        return render(request, "ART_SEARCH.html", {'searched':searched, 'paintingslist':paintingslist})
    else:
        return render(request, "ART_SEARCH.html", {})

@login_required(login_url = '/login')
def add_paintings(request):
    if request.method=="POST":
        form = GalleryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.author = request.user
            gallery.save()
            obj = form.instance
            alert = True
            return render(request, "add_paintings.html",{'obj':obj, 'alert':alert})
    else:
        form=GalleryForm()
    return render(request, "add_paintings.html", {'form':form})

class UpdatePostView(UpdateView):
    model = Gallery
    template_name = 'edit_paintings.html'
    fields = ['title',  'content', 'image']






def Register(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, 'login.html')   
    return render(request, "register.html")

def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, 'painting.html')   
    return render(request, "login.html")

def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')







