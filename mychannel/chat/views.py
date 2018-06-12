from django.shortcuts import render
from chat.models import Video
from django.http import HttpResponse

def list(request):
    latest_url_list = Video.objects.order_by('vote')
    output = ', '.join([q.url+' '+str(q.vote) for q in latest_url_list])
    return HttpResponse(output)

def index(request):
    url_list = Video.objects.all()
    newlist = sorted(url_list, key=lambda x: x.vote, reverse=True)
    k=[x.yt_id for x in newlist] 
    first=str(k[0])
    last=",".join(k[1:])
    context = {'url_list': url_list,'newlist': newlist,'first':first,'last':last}
    return render(request, 'chat/index.html', context)


