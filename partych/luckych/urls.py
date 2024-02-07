from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('accounts/login/', views.LoginView.as_view(), name="login"),
    path('register/', views.RegView.as_view(), name="registration"),
    path('base/', views.BaseView.as_view(), name="base"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/', logout_user, name="logout"),
    path('add_note/', addpage, name='add_note'),
    path('<int:post_id>/delete_post', views.DelitePostView.as_view(), name='delete_post'),
]