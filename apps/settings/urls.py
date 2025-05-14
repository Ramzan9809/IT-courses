from apps.settings.views import home, about, contact, faq, reviews
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('reviews/', reviews, name='reviews'),
]