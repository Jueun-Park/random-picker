from django.urls import path
from picker import views

urlpatterns = [
    path('', views.index),
    path('pick/<lines>', views.pick),
]