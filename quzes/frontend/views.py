from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView


class Home(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/home.html')


