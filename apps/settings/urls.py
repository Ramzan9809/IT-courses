from apps.settings.views import (home, about, contact, faq, reviews,
                                 cart_detail, cart_add, cart_remove, cart_remove_ajax, cart_add_ajax,
                                 checkout_view, cart_clear)
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('reviews/', reviews, name='reviews'),

    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:course_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:course_id>/', cart_remove, name='cart_remove'),
    path('cart/clear/', cart_clear, name='cart_clear'),
    path('cart/add/ajax/', cart_add_ajax, name='cart_add_ajax'),
    path('cart/remove/ajax/', cart_remove_ajax, name='cart_remove_ajax'),
    path('checkout/', checkout_view, name='checkout')
]