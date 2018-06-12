from django.conf.urls import url

from . import views
app_name = 'polls'
urlpatterns = [
    url('jukebox/', views.index, name='index'),
    url('contact/', views.contact, name='contact'),
]
