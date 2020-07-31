from django.urls import path
from jvirtual import views

urlpatterns = [
    path('virtualinfo', views.VirtualInfo.as_view())
]