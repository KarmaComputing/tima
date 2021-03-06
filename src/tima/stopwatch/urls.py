from importlib.resources import path
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sign-up/", views.sign_up, name="sign-up"),
    path("stopwatch/", views.stopwatch, name="stopwatch"),
]
