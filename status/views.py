from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Update_Bar
from .models import Update_Form #di models namanya update

response = {}
def index(request):
    status = Update_Form.objects.all()
    response['status'] = status
    html = 'update_status/update_status.html'
    response['update_form'] = Update_Bar
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
