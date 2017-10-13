from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Update_Bar
from .models import Update_Form 

name = 'Hadlina Rahmadinni'

response = {}
def index(request):
    author = 'kelompok 4'
    response['author'] = author
    status = Update_Form.objects.all().order_by('-created_date')
    response['status'] = status
    html = 'update_status/update_status.html'
    response['update_form'] = Update_Bar
    response['profile_name'] = name
    return render(request, html, response)

def add_status(request):
    form = Update_Bar(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        response['description'] = request.POST['description']
        status = Update_Form(description=response['description'])
        status.save()
        return HttpResponseRedirect('/status/')
    else:
        return HttpResponseRedirect('/status/')

def delete_status(request, pk):
    status = Update_Form.objects.filter(pk=pk).first()
    if status != None:
        status.delete()
        pass
    return HttpResponseRedirect('/status/')