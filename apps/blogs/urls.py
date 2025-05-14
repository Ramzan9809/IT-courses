from apps.blogs.views import blog, blog_detail
from django.urls import path


urlpatterns = [
    path('', blog, name='blog'),
    path('blog_detail/<slug:slug>/', blog_detail, name='blog_detail'),
]