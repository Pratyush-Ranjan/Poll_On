from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns=[
path('signup/', views.signup_view, name='signup'),
path('', views.home, name='home'),
path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name="login"),
path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]