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

        # send the user list to the newly joined user
        self.send(json.dumps({
            'type': 'user_list',
        }))

        if self.user.is_authenticated:
            # create a user inbox for private messages
            async_to_sync(self.channel_layer.group_add)(
                self.user_inbox,
                self.channel_name,
            )

            # send the join event to the room
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'user_join',
                    'user': self.user.username,
                }
            )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

        # if self.user.is_authenticated:
        #     # delete the user inbox for private messages
        #     async_to_sync(self.channel_layer.group_add)(
        #         self.user_inbox,
        #         self.channel_name,
        #     )

        #     # send the leave event to the room
        #     async_to_sync(self.channel_layer.group_send)(
        #         self.room_group_name,
        #         {
        #             'type': 'user_leave',
        #             'user': self.user.username,
        #         }
        #     )
        #     self.room.online.remove(self.user)

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        action_type = text_data_json.get('type', None)

        if action_type == 'edit_comment':
            comment_id = text_data_json['comment_id']
            comment = Comment.objects.get(id=comment_id)
            comment.description = message
            updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            comment.save()
            async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'edit_comment',
                        'id': comment_id,
                        'message': message,
                        'updated_at': updated_at,
                    }
                )
            return

        if not self.user.is_authenticated:
            return self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'You must be logged in to send messages.',
            }))
        if message.startswith('/pm '):
            split = message.split(' ', 2)
            target = split[1]
            target_msg = split[2]

            # send private message to the target
            async_to_sync(self.channel_layer.group_send)(
                f'inbox_{target}',
                {
                    'type': 'private_message',
                    'user': self.user.username,
                    'message': target_msg,
                }
            )
            # send private message delivered to the user
            self.send(json.dumps({
                'type': 'private_message_delivered',
                'target': target,
                'message': target_msg,
            }))
            return 
        
        # delete comment 
        if message.startswith('/del '):
            split = message.split(' ', 1)
            deleted_comment_id = split[1]
            deleted_comment = Comment.objects.get(id=deleted_comment_id)
            if deleted_comment.user == self.user:
                deleted_comment.delete()
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'comment_deleted',
                        'id': deleted_comment_id,
                    }
                )
                return
            else:
                return self.send(text_data=json.dumps({
                    'type': 'error',
                    'message': 'You are not the author of this comment.',
                }))

        # send chat message event to the room
        created_comment = Comment.objects.create(user=self.user, blog=self.room, description=message)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'user': self.user.username,
                'message': message,
                'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'image': self.user.image.url,
                'id': created_comment.id,
            }
        )

    def chat_message(self, event):
        self.send(text_data=json.dumps(event))

    def edit_comment(self, event):
        self.send(text_data=json.dumps(event))

    def comment_deleted(self, event):
        self.send(text_data=json.dumps(event))

    def user_join(self, event):
        self.send(text_data=json.dumps(event))

    def user_leave(self, event):
        self.send(text_data=json.dumps(event))

    def private_message(self, event):
        self.send(text_data=json.dumps(event))

    def private_message_delivered(self, event):
        self.send(text_data=json.dumps(event))