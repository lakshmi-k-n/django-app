from django.shortcuts import render,render_to_response
from chat.models import Video
from django.http import HttpResponse,HttpResponseRedirect
from .forms import MyForm

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = MyForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            
            k=form.cleaned_data['choice_field']
            vid=Video.objects.get(yt_id=k)
            vid.vote+=1
            vid.save()
            print(k)       
            
     
            return HttpResponseRedirect('/chat/contact/') # Redirect after POST
    else:
        form = MyForm() # An unbound form
        
    return render(request,'chat/contact.html',{'form':form})

def index(request):
    url_list = Video.objects.all()
    newlist = sorted(url_list, key=lambda x: x.vote, reverse=True)
    k=[x.yt_id for x in newlist] 
    first=str(k[0])
    last=",".join(k[1:])
    context = {'url_list': url_list,'newlist': newlist,'first':first,'last':last}
    return render(request, 'chat/index.html', context)


