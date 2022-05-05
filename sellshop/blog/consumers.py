from datetime import datetime
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Blog, Comment


class ChatConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None
        self.room_group_name = None
        self.room = None
        self.user = None
        self.user_inbox = None

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['slug']
        self.room_group_name = f'chat_{self.room_name}'
        self.room = Blog.objects.get(slug=self.room_name)
        self.user = self.scope['user']
        self.user_inbox = f'inbox_{self.user.username}'

        # connection has to be accepted
        self.accept()

        # join the room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )
        if self.user.is_authenticated and self.user not in self.room.online_users.all():
            # send the join event to the room
            self.room.online_users.add(self.user)
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'user_join',
                    'users': [user.username for user in self.room.online_users.all()],
                }
            )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

        if self.user.is_authenticated and self.user in self.room.online_users.all():
            # send the leave event to the room
            self.room.online_users.remove(self.user)
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'user_leave',
                    'users': [user.username for user in self.room.online_users.all()],
                }
            )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        description = text_data_json.get('description')
        action = text_data_json.get('action')
        id = text_data_json.get('id')

        # create a new main comment
        if action == 'main_comment':
            created_comment = Comment.objects.create(
                user=self.user, blog=self.room, description=description, is_main=True)
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'main_comment',
                    'user': self.user.username,
                    'description': description,
                    'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'image': self.user.image.url,
                    'id': created_comment.id,
                }
            )
        elif description and description.startswith('/del '):
            print('delete comment')
            comment_id = description.split(' ')[1]
            comment = Comment.objects.get(id=comment_id)
            if comment.user == self.user:
                comment.is_deleted = True
                comment.save()
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'delete_comment',
                        'id': comment_id,
                    }
                )
        elif action == 'edit_comment' and id:
            comment = Comment.objects.get(id=id)
            if comment.user == self.user:
                comment.description = description
                comment.is_edited = True
                comment.save()
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'edit_comment',
                        'id': id,
                        'description': description,
                    }
                )
        elif action == 'user_typing':
            self.room.typing_users.add(self.user)
            users = [user.username for user in self.room.typing_users.all()]
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'user_typing',
                    'users': users,
                }
            )
        elif action == 'user_not_typing':
            self.room.typing_users.remove(self.user)
            users = [user.username for user in self.room.typing_users.all()]
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'user_not_typing',
                    'users': users,
                }
            )

    def main_comment(self, event):
        self.send(text_data=json.dumps(event))

    def delete_comment(self, event):
        self.send(text_data=json.dumps(event))

    def edit_comment(self, event):
        self.send(text_data=json.dumps(event))

    def user_typing(self, event):
        self.send(text_data=json.dumps(event))

    def user_not_typing(self, event):
        self.send(text_data=json.dumps(event))

    def user_join(self, event):
        self.send(text_data=json.dumps(event))

    def user_leave(self, event):
        self.send(text_data=json.dumps(event))
