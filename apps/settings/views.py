from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from .models import Faq, Settings, Slider, Reviews, Purchase
from apps.courses.models import Course, Video, Instructors, Category
from apps.blogs.models import Blog
from apps.events.models import Event
from .cart import Cart



def home(request):
    settings = Settings.objects.latest('id')
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
        'settings': settings,
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

def profile(request):
    return render(request, 'auth/profile.html')


def cart_add(request, course_id):
    cart = Cart(request)
    course = get_object_or_404(Course, id=course_id)
    cart.add(course=course)
    return redirect('cart_detail')


def cart_remove(request, course_id):
    cart = Cart(request)
    course = get_object_or_404(Course, id=course_id)
    cart.remove(course=course)
    return redirect('cart_detail')

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    category = Category.objects.all()[:6]
    context = {
        'cart': cart,
        'category': category,
        'cart_total_quantity': sum(item['quantity'] for item in cart),
        'cart_total_price': sum(float(item['price']) * item['quantity'] for item in cart),
    }
    return render(request, 'pages/cart.html', context)


def checkout_view(request):
    category = Category.objects.all()[:6]
    cart = Cart(request)

    if request.method == 'POST':
        for item in cart:
            Purchase.objects.get_or_create(user=request.user, course=item['course'])
        cart.clear()
        return redirect('success_page')  # или куда тебе нужно

    context = {
        'category': category,
        'cart': cart,
        'cart_total_price': cart.get_total_price(),
    }
    return render(request, 'pages/checkout.html', context)  


@csrf_exempt
def cart_add_ajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            course_id = data.get('course_id')
            quantity = int(data.get('quantity', 1))
        except (json.JSONDecodeError, ValueError, TypeError):
            return JsonResponse({'success': False, 'error': 'Invalid JSON data.'}, status=400)

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'course not found.'}, status=404)

        cart = request.session.get('cart', {})

        if str(course_id) in cart:
            cart[str(course_id)]['quantity'] += quantity
        else:
            cart[str(course_id)] = {
                'price': str(course.price),
                'quantity': quantity,
                'title': course.title,
                'banner': course.banner.url if course.banner else '',
            }

        request.session['cart'] = cart

        total_quantity = sum(item['quantity'] for item in cart.values())
        total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())

        return JsonResponse({
            'success': True,
            'cart_total_quantity': total_quantity,
            'cart_total_price': round(total_price, 2),
            'cart_currency': 'сом',
        })
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def cart_remove_ajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            course_id = data.get('course_id')
        except (json.JSONDecodeError, TypeError):
            return JsonResponse({'success': False, 'error': 'Invalid JSON data.'}, status=400)

        cart = request.session.get('cart', {})

        if str(course_id) in cart:
            del cart[str(course_id)]
            request.session['cart'] = cart

            total_quantity = sum(item['quantity'] for item in cart.values())
            total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())

            return JsonResponse({
                'success': True,
                'cart_total_quantity': total_quantity,
                'cart_total_price': round(total_price, 2),
                'cart_currency': 'сом',
            })

        return JsonResponse({'success': False, 'error': 'course not found in cart.'}, status=404)
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method.'}, status=400)
    