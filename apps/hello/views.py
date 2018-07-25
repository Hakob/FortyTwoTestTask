from django.views.generic import View
from django.shortcuts import render

from .models import Account


class HomeView(View):

    def get(self, request):
        acs = Account.objects.all()
        context = {
         'account': acs
        }
        return render(request, 'home.html', context=context)
