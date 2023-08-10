from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from .models import BlogPost

def fbv_greet(request):
    return HttpResponse("Hello from Function-Based View!")

class CBVGreetView(View):
    def get(self, request):
        return HttpResponse("Hello from Class-Based View!")

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'viewsdemocbv/blogpost_list.html'
    context_object_name = 'blogposts'
