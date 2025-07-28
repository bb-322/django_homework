from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest
from main.forms import SignUpForm, LogInForm, LogInModelForm
from main.models import SignUpModel, LogInModel

# Create your views here.
class SignUp(TemplateView):
    template_name = 'signup.html'

    def get_context_data(self, form: SignUpForm | None = None, **kwargs):
        if not form:
            form = SignUpForm()
        return {
            'form': form
        }
    
    def post(self, request: HttpRequest, **kwagrs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            SignUpModel.objects.create(**data)
        return self.render_to_response(self.get_context_data(form = form))

class Login(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, form: LogInForm | None = None, **kwargs):
        if not form:
            form = LogInForm()
        return {
            'form': form
        }
    
    def post(self, request: HttpRequest, **kwagrs):
        form = LogInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            LogInModel.objects.create(**data)
        return self.render_to_response(self.get_context_data(form = form))

class LoginWModel(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, form: LogInModelForm | None = None, **kwargs):
        if not form:
            form = LogInModelForm()
        return {
            'form': form
        }
    
    def post(self, request: HttpRequest, **kwagrs):
        form = LogInModelForm(request.POST)
        if form.is_valid():
            form.save()
        return self.render_to_response(self.get_context_data(form = form))