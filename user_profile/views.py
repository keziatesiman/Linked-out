from django.shortcuts import render
from .models import Person, Expertise, PhotoURL

# Create your views here.
#name = 'Hepzibah Smith' 
#gender = 'Female'
#expertise = [" Play piano ", " Play violin ", " Play flute ", " Music arragement "," Music composition ", " Film Scoring "]
#description = 'Antique expert. Experience as marketer for 10 years'
#email = 'hello@smith.com'

def index(request):
    html = 'user_profile.html'
    person = Person.objects.all()

    response = {} #TODO Implement yourname
    response['name'] = Person.objects.all()[0].name
    response['birthdate'] = Person.objects.all()[0].birthdate
    response['gender'] = Person.objects.all()[0].gender
    response['expertise'] = Expertise.objects.all()[0]
    response['description'] = Person.objects.all()[0].description
    response['email'] = Person.objects.all()[0].email
    response['model_pic'] = PhotoURL.objects.all()[0].model_pic

    return render(request, html, response)