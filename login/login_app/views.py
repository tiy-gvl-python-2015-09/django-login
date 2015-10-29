from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import CreateView, ListView
from login_app.models import Profile


def default_view(request):
    context = {}
    return render_to_response(template_name='home.html', context=context)

class ProfileListView(ListView):
    model = Profile

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/create_profile/"

    def form_valid(self, form):
      #save the new user first
      form.save()
      #get the username and password
      username = self.request.POST['username']
      password = self.request.POST['password1']
      #authenticate user then login
      user = authenticate(username=username, password=password)
      login(self.request, user)
      return super().form_valid(form)

class ProfileCreateView(CreateView):
    model = Profile
    fields = ['credit_card', 'classification']
    success_url = "/"

    def form_valid(self, form):
        model = form.save(commit=False)
        model.user = self.request.user
        return super().form_valid(form)
