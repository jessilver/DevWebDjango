from django.urls import path, include
from django.contrib.auth import views
from django.contrib import admin
from project import views
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('veiculo/', include('veiculo.urls'), name='veiculo'),
]
