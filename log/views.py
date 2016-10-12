from django.shortcuts import render

from django.http import HttpResponse
from log.models import Log
from log.forms import LogForm
from django.views.generic.edit import FormView


class LogView(FormView):
    template_name = 'date.html'
    form_class = LogForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print("form valid")
        return super(LogView, self).form_valid(form)

def index(request):
    model = Log
    form_class = LogForm
    return HttpResponse("Hello, world. You're at the logs index.")

