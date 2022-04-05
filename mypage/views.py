from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostList(ListView):
  #ListView는 (모델명)_list.html을 템플릿으로 인지
  model = Post
  ordering = '-pk'

class PostDetail(DetailView):
  model = Post

# def index(request):
#   posts = Post.objects.all().order_by('-pk')
#   return render(
#     request,
#     'mypage/index.html', #사용할 템플릿
#     {
#       'posts' : posts,
#     }
#   )

# def my_page_detail(request, pk):
#   post = Post.objects.get(pk=pk)

#   return render(
#     request,
#     'mypage/my_page_detail.html',
#     {
#       'post' : post
#     }
#   )