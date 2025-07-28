from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest
from main.forms import ReviewForm
from main.models import ReviewModel

# Create your views here.
class ReviewPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, form: ReviewForm | None = None, **kwargs):
        if not form:
            form = ReviewForm()
        return {
            'form': form
        }
    
    def post(self, request: HttpRequest, **kwagrs):
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ReviewModel.objects.create(**data)
        return self.render_to_response(self.get_context_data(form = form))