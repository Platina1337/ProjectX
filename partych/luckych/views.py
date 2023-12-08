from django.views.generic import TemplateView
from django.views.generic import FormView, UpdateView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddPostModel, ProfileForm
from django.contrib import messages



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






class MainView(TemplateView):
    template_name = 'luckych/main.html'



class BaseView(TemplateView):
    template_name = 'luckych/base.html'



class ProfileView(UpdateView):
    template_name = 'luckych/profile.html'
    form_class = ProfileForm

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        messages.success(self.request, f'Ваш профиль обновлен')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f'Ваш профиль не обновлен')
        return super().form_invalid(form)


def logout_user(reqest):
    logout(reqest)
    return redirect('login')


class AddNoteView(FormView):
    template_name = 'luckych/addnote.html'
    form_class = AddPostModel
    # success_url =

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)