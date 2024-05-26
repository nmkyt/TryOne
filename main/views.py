from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from users.models import User


@login_required
def profile_view(request):
    user = request.user
    context = {"user": User.objects.filter(id=user.id).prefetch_related("groups").first()}
    return render(request, 'main/profile.html', context)


def index(request):
    return render(request, 'main/index.html')


def contacts(request):
    return render(request, 'main/contacts.html')
