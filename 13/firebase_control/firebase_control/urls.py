from django.contrib import admin
from django.urls import path
from relay_control import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.relay_control, name='relay_control'),
]