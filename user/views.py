from django.shortcuts import render, redirect
from allauth.account.views import PasswordChangeView
from django.urls import reverse
from meeting.models import Post
from datetime import datetime
from meeting.forms import FileUploadForm

# Create your views here.


def index(request):
    return render(request, 'user/index.html')

#    return render(request, 'user/index.html')

def lobby(request):
    context = dict()
    if request.user.is_authenticated :
        context["roomId"] = hash(request.user.nickname)
        return render(request, 'user/lobby.html', context=context)
    else:
        return render(request, 'user/invalid.html')

# def upload(request):
#     form = 

def upLoad(request):
    if request.user.is_authenticated != True : 
        return render(request, 'user/invalid.html')

    if request.method == 'POST':
        fileName = request.POST.get('room_id','')
        image = request.FILES.get("question_uploads",'')
        upload = Post(
            fileName=fileName,
            image=image,
        )
        upload.save()
        return redirect('lobby')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'user/lobby.html', context)


def changePassword(request):
    return render(request, 'account/password_reset_from_key.html')


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")
