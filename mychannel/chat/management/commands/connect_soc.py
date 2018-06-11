from django.core.management.base import BaseCommand
import json
import requests
from websocket import create_connection
import time
import re
from chat.models import Votes

def initialize():
  url="https://slack.com/api/rtm.connect"
  payload={"token":"xoxb-378217444134-377486375763-PctG9vIUJJ6w8BQVlVgmCuoT"}
  r=requests.post(url,payload)
  res=json.loads(r.text)
  print(res)
  url1=res['url']
  ws = create_connection(url1)
  return ws


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
        row=Votes(url=match.group(1))
        row.save()
        print("Item added to database")
    print(result)
    time.sleep(1)
  ws.close()


class Command(BaseCommand):
  def handle(self,**options):
    session=initialize()
    parse_yt(session)
    

