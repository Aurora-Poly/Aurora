from django.urls import path
from . import views


urlpatterns = [
  path('', views.ActList.as_view()),
  path('<int:pk>/', views.ActDetail.as_view())
]
