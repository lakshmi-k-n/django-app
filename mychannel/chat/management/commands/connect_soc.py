from django.core.management.base import BaseCommand
import json
import requests
from websocket import create_connection
import time
import re
from urllib.parse import urlparse,parse_qs
from chat.models import Video

def initialize():
  url="https://slack.com/api/rtm.connect"
  payload={"token":"xoxb-378217444134-377486375763-PctG9vIUJJ6w8BQVlVgmCuoT"}
  r=requests.post(url,payload)
  res=json.loads(r.text)
  print(res)
  url1=res['url']
  ws = create_connection(url1)
  return ws

def get_id(url):
    u_pars = urlparse(url)
    quer_v = parse_qs(u_pars.query).get('v')
    if quer_v:
        return quer_v[0]
    pth = u_pars.path.split('/')
    if pth:
        return pth[-1]

def add_item(link):
  ytid=get_id(link)
  id_list = Video.objects.order_by('vote')
  ids={ q.yt_id for q in id_list }
  if ytid not in ids:
    row=Video(url=link,yt_id=ytid)
    row.save()
    print("\nItem added to database")
  else:
    print("\nitem not added to database - item already exist!")


def parse_yt(ws):
  result =  ws.recv()
  print(result)
  yt=r"^<((https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+)>$"
  while True:
    result =  ws.recv()
    result=json.loads(result)
    if result["type"]=="message" and "hidden" not in result:
      match = re.search(yt, result['text'])
      if match:
        print("match")
        link=match.group(1)
        add_item(link)
    #print(result)
    time.sleep(1)
  ws.close()


class Command(BaseCommand):
  def handle(self,**options):
    session=initialize()
    parse_yt(session)
    

