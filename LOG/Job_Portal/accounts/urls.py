from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),  # Name for login
    path('signup/', views.signup_view, name='signup'),  # Name for signup
    path('index/', views.index_view, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('delete-user/<int:user_id>/', views.delete_user_view, name='delete_user')
    
]



