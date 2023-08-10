from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def home_view(request):
    context={}
    if not request.user.is_authenticated:
        return HttpResponseRedirect('accounts/login/')
    else:
        user = request.user
        hello = 'Hello '
        context = {
        'user': user,
        'hello' : hello,
        }
        return render(request, 'main/home.html', context)