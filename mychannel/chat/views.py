from django.shortcuts import render
from chat.models import Votes

from django.http import HttpResponse



def list(request):
    latest_url_list = Votes.objects.order_by('vote')
    output = ', '.join([q.url for q in latest_url_list])
    return HttpResponse(output)
