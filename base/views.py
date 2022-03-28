from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'names': 'Lets Learn Python'},
    {'id': 2, 'names': 'Desing with me'},
    {'id': 3, 'names': 'Front end developers'},
]

def home(request):
    context = { 'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)