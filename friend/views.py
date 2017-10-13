from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Add_Form
from .models import Friend

# Create your views here.
response = {}

def index(request):
	friend = Friend.objects.all()
	response['friend'] = friend
	html = 'add_friend.html'
	response['add_form'] = Add_Form
	response["author"] = "Azmie"
	return render(request, html, response)

def add_friend(request):
	form = Add_Form(request.POST or None)
	if(request.method == 'POST' and form.is_valid()):
		response['name'] = request.POST['name']
		response['url'] = request.POST['url']
		friend = Friend(name=response['name'], url=response['url'])
		friend.save()
		return HttpResponseRedirect('/friend/')
	else:
		return HttpResponseRedirect('/friend/')

def url_is_valid(url):
    try:
        thepage = urlopen(url)
    except URLError as e:
        return False
    else:
        return True
