from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm

# Create your views here.
class PostListView(ListView):
    model = Post
    paginate_by = 6

class PostDetailView(DetailView):
    model = Post

@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        post = form.save(commit=False)
        post.created_by = self.request.user
        post.save()
        return redirect('post_detail', pk=post.pk)

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'lost/post_form_update.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

@method_decorator(login_required, name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
