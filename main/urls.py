from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about-us', views.about),
    path('onreal', views.cruze),
    path('Homepage', views.hpage)
]