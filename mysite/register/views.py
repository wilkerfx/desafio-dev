from django.contrib.auth.models import User
from django.views.generic import UpdateView
from .forms import ProfileForm
from django.urls import reverse_lazy


class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('logout')
    template_name = 'register/profile.html'
