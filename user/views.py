from django.shortcuts import render
from allauth.account.views import PasswordChangeView
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'user/index.html')

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")