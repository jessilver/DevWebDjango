from django.contrib import admin
from django.urls import path, include
from project.views import Login
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
]
