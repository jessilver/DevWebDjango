from django.contrib import admin
from django.urls import path, include
from project import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('login/', views.Login.as_view(), name='login'),
]
