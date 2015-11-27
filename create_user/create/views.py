from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import CreateView, UpdateView, View, TemplateView
from create.models import Profile


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/accounts/login'

def indexview(request):
    return HttpResponse("working")

class RedirectView(View):

    def get(self, request):
        if request.user.profile.position == 'teacher':
            return HttpResponseRedirect(reverse('teacher'))
        elif request.user.profile.position == 'student':
            return HttpResponseRedirect(reverse('student'))
        else:
            return HttpResponseRedirect(reverse('profile_update', kwargs={"pk": request.user.id}))

class TeacherView(TemplateView):
    model = Profile
    template_name='teacher.html'

class StudentView(View):
    model = Profile
    template_name='student.html'

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ["position"]
    success_url = "/redirect"