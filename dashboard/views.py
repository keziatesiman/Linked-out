from django.shortcuts import render
from status.models import Update_Form
from friend.models import Friend
from user_profile.models import Person, PhotoURL
# TODO import status.models
# TODO import fiends.models
# TODO import user_profile.models

response = {}


def index(request):
    response["author"] = "Rayza"
    return render(request, 'dashboard/dashboard.html', response)
