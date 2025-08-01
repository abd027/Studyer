from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Message, Topic, User
from .forms import RoomForm, UserForm, MyUserCreationForm
from django.db.models import Q,Count
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


rooms = [
    {"id": 1, "name": "CR-1"},
    {"id": 2, "name": "CR-2"},
]

# Create your views here.


def loginUser(request):
    page = 'login'
    if request.method == "POST":
        email = request.POST.get("email").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(email = email)
        except:
            messages.error(request, "An error has occured")

        user = authenticate(email = email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "email or password is incorrect")

    if 'next' in request.GET:
        messages.warning(request, "You need to login first...")

    context = {'page': page}
    return render(request, "base/login_register.html", context)


def signupUser(request):
    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error("An error has occured.")
    context = {'form': form}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q) |
                                Q(name__icontains=q) |
                                Q(description__icontains=q) |
                                Q(host__username__icontains=q)).order_by("-updated", "-created")
    
    topics = Topic.objects.annotate(num_rooms=Count('room')).order_by('-num_rooms')[:5]
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    context = {'rooms': rooms, 'topics': topics,
               'room_count': room_count, 'room_messages': room_messages}
    return render(request, 'base/home.html', context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    topics = Topic.objects.all()
    room_messages = user.message_set.all()
    context = {'user': user, 'rooms': rooms,
               'topics': topics, 'room_messages': room_messages}

    return render(request, 'base/profile.html', context)


def room(request, pk):
    room = Room.objects.get(id=int(pk))
    room_messages = room.message_set.all()
    participants = room.participants.all()
    if request.method == "POST":
        comment = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {'room': room, 'room_messages': room_messages,
               'participants': participants}
    return render(request, "base/room.html", context)


@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()

    if request.method == "POST":
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        # form = RoomForm(request.POST)
        # if form.is_valid():
        #     room = form.save(commit=True)
        #     room.host = request.user
        #     room.save()
        return redirect('home')
    context = {'form': form, 'topics': topics}
    return render(request, "base/room_form.html", context)


@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()

    if request.user != room.host:
        return redirect('home')

    if request.method == "POST":
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.description = request.POST.get('description')
        room.topic = topic
        room.save()
        return redirect('home')
    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, "base/room_form.html", context)


@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return redirect('home')
    if request.method == "POST":
        room.delete()
        return redirect('home')
    context = {"obj": room}
    return render(request, "base/delete.html", context)


def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    room_id = message.room.id

    context = {'obj': message}
    if request.method == "POST":
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', context)


def updateUser(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES , instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)
    context = {'form': form}
    return render(request, 'base/update_user.html', context)


def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains = q)
    context = {'topics': topics}
    return render(request, 'base/topics.html', context)

def activityPage(request):
    room_messages = Message.objects.all()
    context = {'room_messages': room_messages}
    return render(request, 'base/activity.html', context)

# def room(request, pk):
#     room = None

#     for r in rooms:
#         if r["id"] == int(pk):
#             room = r
#     print(room)
#     return render(request, 'base/room.html', {
#         "room": room
#     })
