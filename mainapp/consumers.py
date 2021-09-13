from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):
        
    def connect(self):  # data from backend to frontend
        self.room_name = 'test_consumer'
        self.room_group_name = 'test_consumer_group'
        async_to_sync(self.channel_layer.group_add)(
            self.room_name, self.room_group_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status': 'connected from django channels'}))
    
    
    def receive(self, text_data):  # data from frontend to backend
        print(text_data)
        self.send(text_data=json.dumps({'status': 'we got you.'}))
    
    
    def disconnect(self, *args, **kwargs):
        print('disconnected')