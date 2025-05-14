from django.contrib import admin
from .models import Category, Course, Instructors, Video


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CourseVideoInline(admin.TabularInline):
    model = Video
    readonly_fields = ('id',)
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CourseVideoInline] 


class InstructorsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Instructors, InstructorsAdmin)