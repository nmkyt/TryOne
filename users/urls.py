from django.conf.urls.static import static
from django.urls import path

from TryOne import settings
from . import views

urlpatterns = [
    path('registration/', views.Registration.as_view(), name='registration'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/delete/', views.delete_user, name='delete_profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
