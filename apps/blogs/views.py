from django.shortcuts import render
from .models import Blog, Comment, Category
from django.shortcuts import get_object_or_404


def blog(request):
    blog = Blog.objects.all()
    category = Category.objects.all()
    context = {
        'blog': blog,
        'category': category,
    }
    return render(request, 'pages/blog.html', context)

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    category = Category.objects.all()
    comments = Comment.objects.all()[:2]
    context = {
        'blog': blog,
        'category': category,
        'slug': slug,
        'comments': comments,
    }
    return render(request, 'detail/blog-details.html', context)
