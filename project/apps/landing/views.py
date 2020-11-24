from django.views import View
from django.shortcuts import render


class LandingHome(View):
    def get(self, request):
        return render(request, 'landing/home.html', {})
