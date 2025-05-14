from django.shortcuts import render
from .models import Faq, Settings, Slider, Reviews
from apps.courses.models import Course
from apps.blogs.models import Blog
from apps.events.models import Event

def home(request):
    sliders = Slider.objects.all()[:2] 
    course = Course.objects.all()[:2]
    faq = Faq.objects.all()[:3]
    event = Event.objects.all()[:3]
    reviews = Reviews.objects.all()
    blog = Blog.objects.all()[:3]
    context = {
        'sliders': sliders,
        'course': course,
        'faq': faq, 
        'event': event,
        'reviews': reviews,
        'blog': blog,
    }
    return render(request, 'index.html', context)

def reviews(request):
    reviews = Reviews.objects.all()

    for r in reviews:
        rating = float(r.rating)
        full = int(rating)
        half = 1 if rating - full >= 0.5 else 0
        empty = 5 - full - half

        r.full_stars = range(full)
        r.half_star = half
        r.empty_stars = range(empty)

    context = {
        'reviews': reviews,
    }
    return render(request, 'pages/reviews.html', context) 

def faq(request):
    faq = Faq.objects.all()
    context = {
        'faq': faq,
    }
    return render(request, 'pages/faq.html', context)

def contact(request):
    settings = Settings.objects.latest('id')
    context = {
        'settings': settings,
    }
    return render(request, 'pages/contact.html', context)

def footer(request):
    settings = Settings.objects.latest('id')
    context = {
        'settings': settings,
    }
    return render(request, 'footer.html', context)


def about(request):
    return render(request, 'pages/about.html')