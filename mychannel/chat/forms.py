from django import forms
from .models import Video
#form file

#extract ( you tube id, you tube link ) pairs 
def get_choice():
    obj=Video.objects.all()
    tup=tuple()
    finaltup=tuple()
    for k in obj:
        tup=(k.yt_id,k.url+" --> Votes:"+str(k.vote))
        #generate tuple of tuples contaning the pairs
        finaltup=finaltup+(tup,)
    return finaltup

#get updated forms with changes made until that point,generating a simple radio list of links
class MyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['choice_field']= forms.ChoiceField(choices=get_choice(),widget=forms.RadioSelect())

