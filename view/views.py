
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class Home(View):
    def get(self, request):
        return HttpResponse("This is a Django project")


