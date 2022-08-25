from django.shortcuts import render
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember, Post
import json
from django.views.decorators.csrf import csrf_exempt


def lobby(request):
    if request.user.is_authenticated != True:
        return render(request, 'user/invalid.html')

    context = dict()
    if request.user.superintendent:
        context['room_name'] = request.POST.get('create_room', '')
    else:
        context['room_name'] = request.POST.get('enter_room', '')
    return render(request, 'meeting/lobby.html', context)


def room(request):
    if request.user.is_authenticated != True or request.user.superintendent == True:
        return render(request, 'user/invalid.html')

    print("room: " + str(request.POST.get('room', '')))

    # roomName = RoomMember.objects.get()

    # print(request)
    # image = Post.objects.get(fileName=)
    #context['image'] = image

    return render(request, 'meeting/room.html')


def supervisorRoom(request):
    if request.user.is_authenticated != True or request.user.superintendent != True:
        return render(request, 'user/invalid.html')

    return render(request, 'meeting/supervisor_room.html')


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
