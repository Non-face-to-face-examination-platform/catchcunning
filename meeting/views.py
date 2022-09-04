from django.shortcuts import render, redirect
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember, Post
import json
from django.views.decorators.csrf import csrf_exempt
import os


def lobby(request):
    if request.user.is_authenticated != True:
        return render(request, 'user/invalid.html')

    roomMove = str(request.user.nickname) + "님이 meeting:lobby로 입장했습니다."
    kakaoMessage = "python3 meeting/kakaoAlarm.py " + str(roomMove)
    os.system(kakaoMessage)

    context = dict()
    if request.user.superintendent:
        context['room_name'] = request.POST.get('create_room', '')
    else:
        context['room_name'] = request.POST.get('enter_room', '')
        try:
            context['image'] = Post.objects.get(fileName=context['room_name'])
            request.user.testPath = context['image'].image
            request.user.save()
        except Post.DoesNotExist:
            return render(request, 'user/invalid.html')
    return render(request, 'meeting/lobby.html', context)


def room(request):
    if request.user.is_authenticated != True or request.user.superintendent == True:
        return render(request, 'user/invalid.html')
    else:
        roomMove = str(request.user.nickname) + "님이 room으로 입장했습니다."
        kakaoMessage = "python3 meeting/kakaoAlarm.py " + str(roomMove)
        os.system(kakaoMessage)
        return render(request, 'meeting/room.html')

    #context['image'] = Post.objects.get(fileName=fileName)

    # print(request)
    # image = Post.objects.get(fileName=)
    #context['image'] = image


def supervisorRoom(request):
    if request.user.is_authenticated != True or request.user.superintendent != True:
        return render(request, 'user/invalid.html')

    roomMove = str(request.user.nickname) + "님이 supervisorRoom으로 입장했습니다."
    kakaoMessage = "python3 meeting/kakaoAlarm.py " + str(roomMove)
    os.system(kakaoMessage)
    return render(request, 'meeting/supervisor_room.html')


# def getImageName(request):
#     print("이미지")
#     context = dict()
#     context['presence'] = 0
#     if request.method == 'POST':
#         fileName = request.POST.get('room_name', '')
#         try:
#             print("성공")
#             context['image'] = Post.objects.get(fileName=fileName)
#             request.user.testPath = context['image'].image
#             request.user.save()
#             context['presence'] = 1
#             return render(request, 'meeting/lobby.html', context=context)
#         except Post.DoesNotExist:
#             context['presence'] = 0
#             print("실패")
#             return render(request, 'meeting/lobby.html', context=context)


def getToken(request):
    appId = "9316dc098a9b4edaa2d4ec0e7794c9a7"
    appCertificate = "512dadeaf564425bbce4e534f4d78885"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(
        appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name': data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')
    print(": " + str(room_name))
    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name': member.name}, safe=False)


@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    try:
        member = RoomMember.objects.get(
            name=data['name'],
            uid=data['UID'],
            room_name=data['room_name']
        )
        member.delete()
    except RoomMember.DoesNotExist:
        member = None
    return JsonResponse('Member deleted', safe=False)
