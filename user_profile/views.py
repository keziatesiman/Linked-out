from django.shortcuts import render
from .models import Person, Expertise, PhotoURL

# Create your views here.



def index(request):
    html = 'user_profile.html'

    person = Person.objects.create(name="Johann Sebastian Bach", birthdate="1685-03-31", gender="Male", description="Master of contrapuntal composition and professional harpsichord player", email="jsbach@gmail.com")
    expertise = Expertise.objects.create(expertise ="Contrapuntal composition")
    expertise = Expertise.objects.create(expertise ="Church leading musician")
    expertise = Expertise.objects.create(expertise ="Glorifying God")
    model_pic = expertise = PhotoURL.objects.create(model_pic ="http://www.bachsociety.org/wp-content/uploads/2017/01/Johann-sunglasses.jpg")

    response = {} #TODO Implement yourname
    response['author']= "Kezia Irene"
    response['name'] = Person.objects.all()[0].name
    response['birthdate'] = Person.objects.all()[0].birthdate
    response['gender'] = Person.objects.all()[0].gender
    response['expertise'] = Expertise.objects.all()[0:3]
    response['description'] = Person.objects.all()[0].description
    response['email'] = Person.objects.all()[0].email
    response['model_pic'] = PhotoURL.objects.all()[0].model_pic

    return render(request, html, response)