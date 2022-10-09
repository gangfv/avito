from django.urls import path

from accounts.views import ProfileAccountView, ProfileSettingsAccountView

urlpatterns = [
    path('profile/<slug>', ProfileAccountView.as_view(), name='profile'),
    path('profile/settings/<uuid:pk>/edit/', ProfileSettingsAccountView.as_view(), name='settings'),
]
