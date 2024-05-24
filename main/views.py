from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile_view(request):
    user = request.user
    return render(request, 'main/profile.html', {'user': user})


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

