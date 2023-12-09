import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.views.generic import FormView, UpdateView
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddPostModel, ProfileForm
from django.contrib import messages
from .models import *



class LoginView(TemplateView):
    template_name = 'luckych/auth.html'

    def post(self, request):
        if request.method == 'POST':
            name_2 = request.POST.get('username')
            passw_2 = request.POST.get('password')

            user = authenticate(username=name_2, password=passw_2)
            if user is not None:
                login(request,user)
                return redirect('main')
            else:
                messages.error(request,'Неправильно введенные данные')
                return redirect('login')





class RegView(TemplateView):
    template_name = 'luckych/registration.html'

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('newUsername')
            passw = request.POST.get('newPassword')

            user = User.objects.create_user(username=name, password=passw)
            user.save()
            return redirect('login')






def main(request):
    Appoint = AppointMeeting.objects.filter()
    return render(request, 'luckych/main.html', locals())

class BaseView(TemplateView):
    template_name = 'luckych/base.html'



class ProfileView(UpdateView):
    template_name = 'luckych/profile.html'
    form_class = ProfileForm

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user  # Присваиваем текущего пользователя
        instance.save()

        messages.success(self.request, f'Ваш профиль обновлен')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, f'Ваш профиль не обновлен')
        return super().form_invalid(form)


def logout_user(reqest):
    logout(reqest)
    return redirect('login')






logger = logging.getLogger(__name__)

class AddNoteView(LoginRequiredMixin, CreateView):
    model = AppointMeeting
    fields = ['title', 'description']
    template_name = 'luckych/addnote.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        logger.debug(form.cleaned_data)  # Логгирование информации
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)