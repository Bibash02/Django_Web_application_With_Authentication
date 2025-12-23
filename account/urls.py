from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('', signin, name='login'),
    path('logout/', signout, name='logout'),

    path('home', home, name='home'),
    path('profile/', profile, name='profile'),
    path('blog/', blog, name='blog'),
    path('blog/create/', create_blog, name='create_blog'),
    path('blog/<int:post_id>/', blog_detail, name='blog_detail'),
    path('blog/delete/<int:post_id>/', delete_blog, name='delete_blog'),

    path(
        'forgot-password/',
        auth_views.PasswordResetView.as_view(
            template_name='forgot_password.html'
        ),
        name='password_reset'
    ),

    path(
        'forgot-password/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset-password/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='reset_password.html'
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset-password/complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),

]