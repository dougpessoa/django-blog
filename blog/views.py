from django.views.generic import DetailView, ListView

from .models import Post 

class PostListView(ListView):
  model = Post 

class PostDetailsView(DetailView):
  model = Post 