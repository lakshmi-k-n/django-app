from django.shortcuts import render
from appbot.test_connect import *
# Create your views here.


def appb(request):
    session=initialize()
    return render(request, 'appbot/appb.html', {
            'sock': session,
             })
  
  

