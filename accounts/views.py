from allauth.account.models import EmailAddress
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView

from accounts.models import CustomUser


class ProfileAccountView(DetailView):
    model = CustomUser
    slug_field = "username"
    template_name = "account/profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileAccountView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(CustomUser, username=self.kwargs['slug'])
        context['page_user'] = page_user
        context['emailaddress'] = EmailAddress.objects.all()
        return context


class ProfileSettingsAccountView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "account/settings.html"
    fields = ['last_name', 'first_name', 'middle_name', ]
    login_url = 'account_login'
