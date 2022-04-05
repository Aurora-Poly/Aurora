from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Act

# Create your views here.
class ActList(ListView):
  #ListView는 (모델명)_list.html을 템플릿으로 인지
  model = Act
  ordering = '-pk'

class ActDetail(DetailView):
  model = Act