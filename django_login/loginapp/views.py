from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import CreateView, FormView, TemplateView, UpdateView
from loginapp.models import Profile


def home_view(request):
    context = {}
    return render_to_response(template_name="index.html", context=context)

class HomeView(TemplateView):
    template_name = "index.html"


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/create_account/"

    def validate(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


class UpdateProfileView(UpdateView):
    model = Profile
    fields = ["user_type"]
    success_url = "/"

    def form_valid(self, form):
        model = form.save(commit=False)
        model.user = self.request.user
        return super().form_valid(form)
