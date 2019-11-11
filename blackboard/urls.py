from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('home/',views.homeView, name='home'),
    path('student/',views.studentView, name='student'),
    path('teacher/',views.teacherView, name='teacher'),
    path('register/',views.registerView, name='register'),
    path('login/',auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/complete/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    url(r'^api/', include('blackboard.api.urls')),
]