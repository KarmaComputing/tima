from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from stopwatch.forms import SignupFirm

def index(request):
    return render(request, "index.html")


def sign_up(request):
    if request.method == "POST":
        form = SignupFirm(request.POST)
        if form.is_valid():
            breakpoint()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email, password)
    else:
        form = SignupFirm()
    return render(request, "sign-up.html", {"form": form})


@login_required(login_url="/admin")
def stopwatch(request):
    return render(request, "stopwatch.html")
