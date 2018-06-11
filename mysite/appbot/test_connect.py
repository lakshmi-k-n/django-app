import json
import requests
from websocket import create_connection
import time
import re
def initialize():
  url="https://slack.com/api/rtm.connect"
  payload={"token":"xoxb-378217444134-377486375763-PctG9vIUJJ6w8BQVlVgmCuoT"}
  r=requests.post(url,payload)
  res=json.loads(r.text)
  url1=res['url']
  ws = create_connection(url1)
  boturl="https://slack.com/api/bots.info"
  r=requests.post(boturl,payload)
  res=json.loads(r.text)
  print(res)
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
        print(match.group(1))
    print(result)
    time.sleep(1)
  ws.close()


def main():
  session=initialize()
  parse_yt(session)


if __name__=="__main__":
  main()


