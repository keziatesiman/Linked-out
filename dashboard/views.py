from django.shortcuts import render
from status.models import Update_Form
from friend.models import Friend
from user_profile.models import Person, PhotoURL
# TODO import status.models
# TODO import fiends.models
# TODO import user_profile.models

response = {}


def index(request):
    html = "dashboard/dashboard.html"

    personName = Person.objects.all()[0].name
    personPic = PhotoURL.objects.all()[0].model_pic
    statusCount = Update_Form.objects.all().count()
    statusMsg = statusMsg = "Post" if statusCount <= 1 else "Posts"
    friendCount = Friend.objects.all().count()
    friendMsg = "Person" if friendCount <= 1 else "People"
    if (statusCount > 0):
        lastStatus = Update_Form.objects.all()[statusCount - 1]
        lastDesc = lastStatus.description
        lastDate = lastStatus.created_date
    else:
        lastDesc = "Tidak ada Status"
        lastDate = None

    response["author"] = "Rayza"
    response["personName"] = personName
    response["personPic"] = personPic
    response["statusCount"] = statusCount
    response["statusMsg"] = statusMsg
    response["friendCount"] = friendCount
    response["friendMsg"] = friendMsg
    response["lastDesc"] = lastDesc
    response["lastDate"] = lastDate

    return render(request, html, response)
