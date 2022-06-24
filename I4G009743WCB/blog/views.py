from django.shortcuts import render

#import views
from django.views import generic
from .models import Post

# Create your views here
# class PostListView(generic.ListView()):
    #   queryset = Post.published.all()
    #   context_object_name = 'posts'
    #   paginate_by = 4
    #   template_name = 'blog/post/list.html'
# 

class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return super().get_queryset().filter(status="published")
    paginate_by = 4
    template_name = "blog/post_list.html"



class PostCreateView(generic.CreateView):
    model = Post
    fields ="__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView(generic.DetailView):
    model = Post

class PostUpdateView(generic.UpdateView):
    model = Post
    fields ="__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(generic.DeleteView):
    model = Post
    fields ="__all__"
    success_url = reverse_lazy("blog:all")

   

