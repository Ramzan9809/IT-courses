from django.contrib import admin
from .models import Slider, Settings, Faq, Reviews, Purchase


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'created_at')
    list_filter = ('course', 'created_at')
    search_fields = ('user__username', 'course__title')


admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Reviews)
admin.site.register(Faq)
admin.site.register(Settings)
admin.site.register(Slider)