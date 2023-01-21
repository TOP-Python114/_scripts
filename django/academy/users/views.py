from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic import FormView


# Create your views here.


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect(self.next_page)


class UserRegistrationView(FormView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = '/auth/login/'

    def form_valid(self, form: UserCreationForm):
        form.save()
        return redirect(self.get_success_url())
