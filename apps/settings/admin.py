from django.contrib import admin
from .models import Slider, Settings, Faq, Reviews, Purchase


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_courses', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'course__title')

    def get_courses(self, obj):
        return ", ".join([course.title for course in obj.course.all()])
    get_courses.short_description = 'Courses'

admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Reviews)
admin.site.register(Faq)
admin.site.register(Settings)
admin.site.register(Slider)