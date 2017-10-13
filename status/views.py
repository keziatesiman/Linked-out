from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Status_Form
from .models import Status

expertise=['Web Development','Java Language','Gaming']
description='this is test'
name='Hadlina Rahmadinni'
gender='female'
email='hadlinar@gmail.com'
author='Hadlina Rahmadinni'


# Create your views here.
response = {}

def index(request):
    response['author'] = author #TODO Implement yourname
    status = Status.objects.all().order_by('-created_date')
    response['database'] = status
    html = 'update_status/update_status.html'
    response['status_form'] = Status_Form
    response['profile_name'] = name
    return render(request, html, response)

def add_status(request):
    form = Status_Form(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        response['status'] = request.POST['status']
        status = Status(status=response['status'])
        status.save()
        return HttpResponseRedirect('/status/')
    else:
        return HttpResponseRedirect('/status/')

def delete_status(request, pk):
    status = Status.objects.filter(pk=pk).first()
    if status != None:
        status.delete()
        pass
    return HttpResponseRedirect('/status/')