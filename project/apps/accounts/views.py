from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib import messages
from apps.accounts.forms import CreateUserForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class SignupView(View):
    template_name = 'accounts/auth/signup.html'
    form = CreateUserForm
    redirect_url = 'accounts:signup_done'
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form()
        self.context['form'] = form
        return render(request, self.template_name, self.context)
    
    def post(self, request, *args, **kwargs):
        form  = self.form(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully.')
            return redirect(self.redirect_url)
        else:
            form = self.form(request.POST)
            messages.warning(request, 'Can\'t create the account')
        
        self.context['form'] = form
        return render(request, self.template_name, self.context)


class AccountProfileView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        print(request.user)
        return render(request, 'accounts/profile/profile.html', {})
