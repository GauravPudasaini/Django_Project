from django.contrib import admin
from django.urls import path, include
from accounts import views  
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),  # Admin dashboard
    path('accounts/', include('accounts.urls')),  # Include app-specific URLs
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Login page
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Logout redirects to login
    path('', views.index_view, name='index'),  # Authenticated home page
]
