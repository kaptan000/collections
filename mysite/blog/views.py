from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from datetime import date
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.views.generic import ListView,DetailView
from django.views import View
from .forms import CommentForm
# Create your views here.



class StartingPageView(ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ['-date']
    context_object_name = 'posts'
    def get_queryset(self):
        query_set = super().get_queryset()
        data = query_set[:3]
        return data
    # latest_posts = Post.objects.all().order_by('-date')[:3]
    # return render(request,"blog/index.html" , {"posts": latest_posts})

class Posts(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"
    ordering = ['-date']
    # all_posts = Post.objects.all().order_by("-date")
    # return render(request,"blog/all-posts.html",{"all_posts":all_posts})

class PostDetail(View):
    # model = Post
    # template_name = "blog/post-detail.html"
    def is_stored_post(self,request,post_id):
        stored_post = request.session.get("stored_posts")
        print(stored_post)
        if stored_post!=None :
            has_stored = post_id in stored_post
        else:
            has_stored = False
        return has_stored        

    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        return render(request,"blog/post-detail.html",{
            "post" : post,
            "post_tags" : post.tag.all(),
            "comment_form" : CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "has_stored" : self.is_stored_post(request,post.id)
        })
         
    def post(self,request,slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post-detail-page',args=[slug]))
        
        return render(request,"blog/post-detail.html",{
            "post" : post,
            "post_tags" : post.tag.all(),
            "comment_form" : comment_form,
            "comments":post.comments.all().order_by("-id"),
            "has_stored" : self.is_stored_post(request,post.id)
        })
    
class ReadLaterView(View):
    def get(self,request):
        stored_posts = request.session.get("stored_posts")
        print(stored_posts)
        context = {}
        if stored_posts is None or len(stored_posts) == 0 :
            context["posts"] = []
            context["has_posts"] = False
        else:
            context["posts"] = Post.objects.filter(id__in = stored_posts)
            context["has_posts"] = True
        return render(request,'blog/stored-posts.html',context)    
    
            

    def post(self,request):
        post_id = int(request.POST.get('post_id'))
        stored_posts = request.session.get("stored_posts")
        print(stored_posts)
        print(post_id)
        if stored_posts is None:
            stored_posts = []
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:   
            stored_posts.remove(post_id) 
        request.session['stored_posts'] = stored_posts
        return HttpResponseRedirect('/')    
       
    # model = Post
    # template_name = "blog/post-detail.html"
    # def get_context_data(self, **kwargs: Any):
    #     context =  super().get_context_data(**kwargs)
    #     context["post_tags"] = self.object.tag.all()
    #     context["comment"] = CommentForm()
    #     return context
    # identified_post = get_object_or_404(Post,slug=slug)
    # return render(request,"blog/post-detail.html",{"post":identified_post,"post_tags":identified_post.tag.all()})
