from cmath import log
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")


def sign_up(request):
    return render(request, "sign-up.html")


@login_required(login_url="/admin")
def stopwatch(request):
    return render(request, "stopwatch.html")
