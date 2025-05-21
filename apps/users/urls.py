from apps.users.views import login_view, reg_view, logout_view, forgot
from django.urls import path
from django.views.generic import TemplateView



urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', reg_view, name='register'),
    path('forgot/', forgot, name='forgot'),
    path('forgot/done/', TemplateView.as_view(template_name='auth/password_reset_done.html'), name='password_reset_done'),
]