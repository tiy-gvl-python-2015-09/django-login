from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/create_profile/"

    def validate(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)

c