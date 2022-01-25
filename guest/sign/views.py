from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == "admin" and password == "admin123":
            response = HttpResponseRedirect("/event_manage/")
            response.set_cookie('user', username, 3600)
            return response
        return render(request, 'index.html', {"error": "username or password error!"})


def event_manage(request):
    username = request.COOKIES.get('user', '')
    return render(request, 'event_manage.html', {'user':username})
# Create your views here.
