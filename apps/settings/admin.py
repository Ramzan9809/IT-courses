from django.contrib import admin
from .models import Slider, Settings, Faq, Reviews


admin.site.register(Reviews)
admin.site.register(Faq)
admin.site.register(Settings)
admin.site.register(Slider)