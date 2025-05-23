from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Course, Instructors, Video
from apps.settings.models import Reviews, Purchase


def course(request):
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
        'course': course,
    }
    return render(request, 'pages/course.html', context)


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    instructor = course.instructor
    reviews = Reviews.objects.filter(course=course)[:2]  # ✅ правильно — привязка по course

    purchased = False
    video = []
    if request.user.is_authenticated:
        purchased = Purchase.objects.filter(user=request.user, course=course).exists()
        if purchased:
            video = Video.objects.filter(course=course)

    rating = float(course.rating)
    full = int(rating)
    half = 1 if rating - full >= 0.5 else 0
    empty = 5 - full - half

    course.full_stars = range(full)
    course.half_star = half
    course.empty_stars = range(empty)

    context = {
        'course': course,
        'instructor': instructor,
        'reviews': reviews,
        'video': video,
        'purchased': purchased,
    }
    return render(request, 'detail/course-details.html', context)


def instructor(request):
    instructor = Instructors.objects.all()
    context = {
        'instructor': instructor,
    }
    return render(request, 'pages/instructor.html', context)

def instructor_detail(request, slug):
    instructor = get_object_or_404(Instructors, slug=slug)
    courses = Course.objects.filter(instructor=instructor)

    for cours in courses:
        rating = float(cours.rating)
        full = int(rating)
        half = 1 if rating - full >= 0.5 else 0
        empty = 5 - full - half
        cours.full_stars = range(full)
        cours.half_star = half
        cours.empty_stars = range(empty)

    context = {
        'instructor': instructor,
        'courses': courses,
    }
    return render(request, 'detail/instructor-details.html', context)