from django.contrib import admin
from .models import Category, Course, Instructors

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class InstructorsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Instructors, InstructorsAdmin)