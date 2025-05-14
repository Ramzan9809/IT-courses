from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Event


def event(request):
    event = Event.objects.all()
    context = {
        'event': event,
    }
    return render(request, 'pages/event.html', context)

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    context = {
        'event': event,
        'slug': slug,
    }
    return render(request, 'detail/event-details.html', context)
 