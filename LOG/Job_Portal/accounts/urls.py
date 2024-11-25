from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Name for login
    path('signup/', views.signup_view, name='signup'),  # Name for signup
    path('index/', views.index_view, name='index'),
]



