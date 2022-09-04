from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from allauth.account.views import PasswordChangeView
from django.urls import reverse
from meeting.models import Post
from datetime import datetime
from meeting.forms import FileUploadForm
import os
import random
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import base64
# Create your views here.


def index(request):
    roomMove = str()
    if request.user.is_authenticated == False:
        roomMove = str(request.user) + "님이 index로 입장했습니다."
    else:
        roomMove = str(request.user.nickname) + "님이 index로 입장했습니다."

    kakaoMessage = "python3 meeting/kakaoAlarm.py " + str(roomMove)
    os.system(kakaoMessage)

    return render(request, 'user/index.html')


def lobby(request):
    context = dict()
    if request.user.is_authenticated:
        roomMove = str(request.user.nickname) + "님이 user:lobby로 입장했습니다."
        kakaoMessage = "python3 meeting/kakaoAlarm.py " + str(roomMove)
        os.system(kakaoMessage)

        context["roomId"] = hash(
            request.user.nickname + str(datetime.now().time()))
        return render(request, 'user/lobby.html', context=context)
    else:
        return render(request, 'user/invalid.html')


def upLoad(request):
    if request.user.is_authenticated != True:
        return render(request, 'user/invalid.html')

    if request.method == 'POST':
        fileName = request.POST.get('room_id', '')
        image = request.FILES.get("question_uploads", '')
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


@csrf_exempt
def sendmail(request):
    data = request.POST.__getitem__('imgSrc')
    data = data[22:]        # 앞의 'data:image/png;base64'부분을 제거
    # print("data: " + data)
    number = random.randrange(1, 10000)    # 동시에 다른 사용자가 접근시 최대한 중복을 막기위함.

    # 저장할 경로 및 파일명을 지정
    path = os.path.join(settings.MEDIA_ROOT + "/")
    print("path = == = = = =", path)
    filename = 'image' + str(number) + '.png'

    # "wb"(즉, 바이너리파일 쓰기전용)으로 파일을 open
    image = open(path+filename, "wb")
    # `base64.b64decode()`를 통하여 디코딩을 하고 파일에 써준다.
    image.write(base64.b64decode(data))
    image.close()

    # filename을 json형식에 맞추어 response를 보내준다.

    email = EmailMessage(
        'title',
        'content',
        to=['hn06038@gmail.com'],
    )

    email.attach_file(path+filename)
    email.send()
    return redirect("/")
