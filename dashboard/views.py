from django.shortcuts import render
# TODO import status.models
# TODO import fiends.models
# TODO import user_profile.models

response = {}


def index(request):
    response["author"] = "Rayza"
    return render(request, 'dashboard/dashboard.html', response)
