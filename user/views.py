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
        context["roomId"] = hash(request.user.nickname + str(datetime.now().timestamp()))
    return render(request, 'user/lobby.html', context=context)

# def upload(request):
#     form = 

def upLoad(request):
    print("시발")
    if request.method == 'POST':
        filePath = request.POST.get('filePath','')
        image = request.FILES.get("image",'')
        upload = Post(
            filePath=filePath,
            image=image,
        )
        upload.save()
        return redirect('upLoad')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'user/lobby.html', context)




class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")
