from apps.events.views import event, event_detail
from django.urls import path


urlpatterns = [
    path('', event, name='event'),
    path('event_detail/<slug:slug>/', event_detail, name='event_detail'),
]