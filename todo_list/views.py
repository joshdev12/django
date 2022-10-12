from django.shortcuts import render

from .models import Task

def index(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, 'lol.html', context)






















# Create your views here.

# def index(request):
#     context = {
#         "fruits": [
#             {
#                 "name": "orange",
#                 "size": 12,
#                 "is_ripe": False
#             },
#             {
#                 "name": "banana",
#                 "size": 4,
#                 "is_ripe": True
#             },
#             {
#                 "name": "Papaya",
#                 "size": 8,
#                 "is_ripe": False
#             },
#             {
#                 "name": "Pawpaw",
#                 "size": 8,
#                 "is_ripe": False
#             },
#         ]
#     }
#     return render(request, 'lol.html', context)


