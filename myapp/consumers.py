import json
import time,subprocess
from channels.generic.websocket import WebsocketConsumer
from django.conf import settings

class myappConsumer(WebsocketConsumer):
 def connect(self):
  self.accept()


  self.send(text_data=json.dumps({
   'type':'connection_established',
   'message':'Connected',
   
  }

  ))

 def receive(self,text_data):
   text_data_json = json.loads(text_data)
   message = text_data_json['message']
   
   cmd= 'powershell -command '+message
   message=''
   for i in range(2):
     p=subprocess.run(cmd,capture_output=True,text=True,shell=True)
     message += p.stdout
     time.sleep(2)
     print('Output:',message)
    

     self.send(text_data=json.dumps({
      'type':'chat',
      'message':message,
     }))