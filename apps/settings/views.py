from django.shortcuts import render
from .models import Faq, Settings, Slider, Reviews
from apps.courses.models import Course, Video, Instructors, Category
from apps.blogs.models import Blog
from apps.events.models import Event

def home(request):
    sliders = Slider.objects.all()[:2]
    category = Category.objects.all()[:4]
    faq = Faq.objects.all()[:3]
    event = Event.objects.all()[:3]
    reviews = Reviews.objects.all()
    blog = Blog.objects.all()[:3]
    instructor = [b.instructor for b in blog]

    category_slug = request.GET.get('category')

    if category_slug:
        course = Course.objects.filter(category__slug=category_slug)
    else:
        course = Course.objects.all()

    for c in course:
        rating = float(c.rating)
        full = int(rating)
        half = 1 if rating - full >= 0.5 else 0
        empty = 5 - full - half

        c.full_stars = range(full)
        c.half_star = half
        c.empty_stars = range(empty)

    context = {
        'sliders': sliders,
        'course': course,
        'category': category,
        'faq': faq,
        'event': event,
        'reviews': reviews,
        'blog': blog,
        'instructor': instructor,
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
    blog = Blog.objects.all()
    context = {
        'settings': settings,
        'blog': blog,
    }
    return render(request, 'footer.html', context)


def about(request):
    video = Video.objects.latest('id')
    course = Course.objects.latest('id')
    instructor = Instructors.objects.all()
    reviews = Reviews.objects.all()

    rating = float(course.rating)
    full = int(rating)
    half = 1 if rating - full >= 0.5 else 0
    empty = 5 - full - half

    course.full_stars = range(full)
    course.half_star = half
    course.empty_stars = range(empty)

    context = {
        'video': video,
        'course': course,
        'instructor': instructor,
        'reviews': reviews,
    }
    return render(request, 'pages/about.html', context)
