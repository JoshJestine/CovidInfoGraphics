from django.shortcuts import render
from django.http import Http404, JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import Destination, RoomMember
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# Create your views here.
def error_404(request, exception):
    return render(request, '404.html')

@login_required(login_url='login')
def news_pages(request, news_url):
    if Destination.objects.filter(url=news_url).exists():
        return render(request, "news_single.html", {"dest": Destination.objects.get(url=news_url)})
    else:
        raise Http404("No such Event exists")

@login_required(login_url='login')
def info(request):
    return render(request, 'info.html')

@login_required(login_url='login')
def lobby(request):
    return render(request, 'lobby.html')

def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def room(request):
    return render(request, 'room.html' )

@login_required(login_url='login')
def dynamic(request):
    dests= Destination.objects.all().order_by('-createdTime')
    return render(request, 'dynamic.html', {'dests':dests})

def chatroom(request):
    return render(request, 'chatroom.html')

@login_required(login_url='login')
def hospital(request):
    return render(request, 'hospital.html')

def getToken(request):
    appId = "22b451f5433a4e66980a445ce5dd59ae"
    appCertificate = "3cb6ed1ca6684c5e95c2793785cc04de"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)

