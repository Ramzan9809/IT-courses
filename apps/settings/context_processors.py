from .models import Settings

def settings_context(request):
    try:
        settings = Settings.objects.latest('id')
    except Settings.DoesNotExist:
        settings = None
    return {'settings': settings}