from datetime import date
from django.shortcuts import render, redirect, reverse

from django.views import View
from django.views.generic import ListView

from .models import *
from .forms import *



def get_date(post):
    return post['date']

# Create your views here.

class HomeView(View):
    def get(self, request):
        latest_posts  = All_Posts.objects.all().order_by("-date")[:3]
        year = date.today().year
        return render(request, 'blog/home.html', {'posts': latest_posts, "year": year })
    

    

class PostsView(ListView):
    template_name = "blog/all_posts.html"
    model = All_Posts
    context_object_name = "posts"
    ordering = ['-date']



def postdetail(request, slug):
    post = All_Posts.objects.get(slug = slug)
    form = CommentForm()
    comments = post.comments.all()
    stored_posts_id = request.session.get("read_later")

    if stored_posts_id == None or len(stored_posts_id) == 0 :
        read_later_check = False
    else:
        if post.id in stored_posts_id:
            read_later_check = True
        else:
            read_later_check = False
    
    if request.method == "POST":
        submitted_form = CommentForm(request.POST)

        if submitted_form.is_valid():
            comment = submitted_form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect(reverse("post-detail-page", args=[slug]))

        else:
            form = submitted_form
    
    return render(request, "blog/post-detail.html",{"post": post, "form": form, "comments": comments, "read_later_check": read_later_check} )






class ReadLaterView(View):
    def get(self, request):
        stored_posts_id = request.session.get("read_later")
        posts = All_Posts.objects.all()

        read_later_posts = []
        
        if stored_posts_id == None or len(stored_posts_id) == 0:
            posts_check = False
        else:    
            posts_check= True
            for post in posts:
                if post.id in stored_posts_id:
                    read_later_posts.append(post)

        return render(request, 'blog/read_later_posts.html', {"posts": read_later_posts, "check": posts_check })

    def post(self, request):
        post_id = int(request.POST["read-later"])
        slug_value = request.POST["slug"]

        stored_posts = request.session.get("read_later")

        if stored_posts is None:
            stored_posts = [post_id]
        else:
            if post_id not in stored_posts:
                stored_posts.append(post_id)

        request.session["read_later"] = stored_posts

        return redirect(reverse("post-detail-page", args=[slug_value]))





class RemoveReadLaterView(View):
    def post(self, request):
        post_id = int(request.POST["remove-read-later"])
        slug_value = request.POST["slug"]

        stored_posts = request.session.get("read_later")

        if post_id in stored_posts:
            stored_posts.remove(post_id)

        request.session["read_later"] = stored_posts

        return redirect(reverse("post-detail-page", args=[slug_value]))