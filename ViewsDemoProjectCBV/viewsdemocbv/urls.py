from django.urls import path
from . import views

urlpatterns = [
    path('fbv-greet/', views.fbv_greet, name='fbv_greet'),
    path('cbv-greet/', views.CBVGreetView.as_view(), name='cbv_greet'),
    path('blogposts/', views.BlogPostListView.as_view(), name='blogpost_list'),
]
