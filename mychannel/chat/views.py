from django.shortcuts import render
from chat.models import Video
from django.http import HttpResponse



def list(request):
    latest_url_list = Video.objects.order_by('vote')
    output = ', '.join([q.url+' '+str(q.vote) for q in latest_url_list])
    return HttpResponse(output)
