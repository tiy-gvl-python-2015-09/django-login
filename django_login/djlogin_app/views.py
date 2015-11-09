from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import CreateView, UpdateView, View, TemplateView
from djlogin_app.models import Profile


class UserCreate(CreateView):
    model = User
    success_url = "/accounts/login"
    form_class = UserCreationForm


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ["user_type"]
    success_url = "/"


class TeacherIndex(TemplateView):

    template_name = "teacher_index.html"

    def get_context_data(self, **kwargs):
        context = super(TeacherIndex, self).get_context_data(**kwargs)
        context['object'] = User.objects.filter(id=kwargs["pk"])[0]
        return context


class StudentIndex(TemplateView):

    template_name = "student_index.html"

    def get_context_data(self, **kwargs):
        context = super(StudentIndex, self).get_context_data(**kwargs)
        context['object'] = User.objects.filter(id=kwargs["pk"])[0]
        return context


class UserRedirectView(View):

    def get(self, request):
        if request.user.profile.user_type == "student":
            return HttpResponseRedirect(reverse("student_index", kwargs={"pk": request.user.id}))
        elif request.user.profile.user_type == "teacher":
            return HttpResponseRedirect(reverse("teacher_index", kwargs={"pk": request.user.id}))
        else:
            return HttpResponseRedirect(reverse("update_profile", kwargs={"pk": request.user.id}))


class IndexView(View):

    def get(self, request):
        if request.user.id == None:
            return HttpResponseRedirect(reverse("welcome"))
        elif request.user.profile.user_type == "teacher":
            return HttpResponseRedirect(reverse("teacher_index", kwargs={"pk": request.user.id}))
        elif request.user.profile.user_type == "student":
            return HttpResponseRedirect(reverse("student_index", kwargs={"pk": request.user.id}))


class WelcomeView(TemplateView):

    template_name = "welcome.html"