
from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname", "superintendent"]
    
    def signup(self, request, user):
        user.nickname = self.cleaned_data['nickname']
        user.superintendent = self.cleaned_data['superintendent']
        user.save()