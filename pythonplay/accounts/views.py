from django.contrib.auth.forms import UserCreationForm
from .forms import UserInfoForm, UserPasswordForm, ProfileForm
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserProfileView(generic.TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info_form'] = UserInfoForm(instance=self.request.user)
        context['profile_form'] = ProfileForm(instance=self.request.user.profile)
        context['password_form'] = UserPasswordForm(self.request.user)
        try:
            user = get_object_or_404(User, username=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404("Пользователь не найден")
        context['user_profile'] = user
        context['info_form'] = UserInfoForm(instance=self.request.user)
        context['profile_form'] = ProfileForm(instance=self.request.user.profile)
        context['password_form'] = UserPasswordForm(self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        if 'info_form' in request.POST or 'profile_form' in request.POST:
            info_form = UserInfoForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, instance=request.user.profile)
            if info_form.is_valid() and profile_form.is_valid():
                info_form.save()
                profile_form.save()
                messages.success(request, 'Данные успешно изменены')
                return redirect('profile', request.user)
            else:
                context = self.get_context_data(**kwargs)
                context['info_form'] = info_form
                context['profile_form'] = profile_form
                return render(request, self.template_name, context)
        elif 'password_form' in request.POST:
            form = UserPasswordForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Пароль успешно изменён')
                return self.get(request, *args, **kwargs)
            else:
                context = self.get_context_data(**kwargs)
                context['password_form'] = form
                return render(request, self.template_name, context)
        else:
            return self.get(request, *args, **kwargs)
