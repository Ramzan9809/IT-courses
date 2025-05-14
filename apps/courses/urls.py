from apps.courses.views import course, course_detail, instructor, instructor_detail
from django.urls import path


urlpatterns = [
    path('', course, name='course'),
    path('course_detail/<slug:slug>/', course_detail, name='course_detail'),
    path('instructor/', instructor, name='instructor'),
    path('instructor_detail/<slug:slug>/', instructor_detail, name='instructor_detail'),

]