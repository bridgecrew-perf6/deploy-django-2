from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),
    path('detail/<int:question_id>/', views.detailView, name='detail'),
    path('page2/', views.pages2, name='page2'),
    path('list/', views.viewQuestion, name='list_q'),
    path('<int:question_id>/', views.vote, name='vote'),
    path('home/', views.eventLogin, name='elogin')
]
