
## Features (sketch)

### FE Modules
- Chat
- Contact List
- Notifications
- Settings
- Voice Call
- Video Call
- Add People
- Invite People to Chat
- Login
- Register


### User Authentication:
- User registration with phone number
- User login with OTP
- Password reset functionality (if needed)

### Real-time Chat:
- Send text messages in real-time
- Support for multimedia messages (images, videos, files)
- Group chat functionality
- Notification of new messages in real-time

### Database Operations:
- Store user information (username, phone number)
- Store chat messages with metadata (sender, receiver, timestamp)
- Consider data models for group chats if needed

### Twilio Integration:
- Integration for sending OTP via SMS
- Verification of OTP for user login

### API Endpoints with Django-Ninja:
- User registration and login endpoints
- Endpoints for sending and receiving messages
- Additional endpoints for managing user profiles and settings

### WebSocket Implementation:
- Set up WebSocket consumers for real-time chat
- Handle WebSocket connections for sending and receiving messages

### Push Notifications:
- Implement push notifications for new messages
- Notify users even when the app is not actively open

### Security:
- Implement secure communication (HTTPS)
- Protect against common web vulnerabilities

### User Interface:
- Web interface for chat application
- Responsive design for different screen sizes

### Development and Testing:
- Unit tests for critical functionalities
- Integration tests for API endpoints
- End-to-end testing for the entire chat flow

### Scalability:
- Design the application to handle a larger user base
- Optimize database queries and operations




## More Features

### Users App
- CustomUser model for extended user details

### Messaging App
- Message model for one-to-one user messages
- ChatGroup model for group conversations
- GroupMessage model for messages within a group
- Poll model for creating polls
- PollVote model for voting in polls
- CustomEmoticon model for user-specific emoticons
- MessageReaction model for reactions to messages

### Notifications App
- Device model for storing user devices
- Notification model for user notifications
- Announcement (Removed)

### Profiles App
- UserProfile model for additional user profile information
- Friendship model for managing user friendships
- UserStatus model for tracking user online status
- UserSettings model for user-specific settings

### Reviews App
- UserBlock model for blocking users
- UserActivity (Removed)
- UserReputation (Removed)
- Report model for reporting inappropriate content

### Locations App
- UserLocation model for tracking user locations

### Extras (Additional Features)
- Polls and Surveys
- Emojis and Reactions
- User Blocking
- User Activity Log
- User Settings
- Report/Flagging System
- Location Sharing
- Integration with External Services (Removed)
- User Tags or Labels
- Custom Emoticons or Stickers
- Polls and Surveys
- User Reputation (Removed)
- Announcements or Broadcast Messages (Removed)


 ![Alt text](conar-cross-woodland-spring-cc.jpg)


## Apps and Models

### users:
- CustomUser

### messaging:
- Message
- Group
- GroupMessage
- Poll
- PollVote
- CustomEmoticon
- MessageReaction

### notifications:
- Device
- Notification

### profiles:
- UserProfile
- Friendship
- UserStatus
- UserSettings


### reviews:
- UserBlock
- Report




![Alt text](conar-cross-woodland-autumn-cc.jpg)




```
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    # Additional fields for multimedia messages if needed
    image = models.ImageField(upload_to='message_images/', null=True, blank=True)
    video = models.FileField(upload_to='message_videos/', null=True, blank=True)
    file = models.FileField(upload_to='message_files/', null=True, blank=True)

class ChatGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    members = models.ManyToManyField(User, related_name='groups')

class GroupMessage(models.Model):
    group = models.ForeignKey(Group, related_name='group_messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sent_group_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # Additional fields for multimedia messages if needed

class Device(models.Model):
    user = models.ForeignKey(User, related_name='devices', on_delete=models.CASCADE)
    device_token = models.CharField(max_length=255)
    # Additional fields as needed

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    # Additional fields as needed

class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    # Additional fields as needed

class Friendship(models.Model):
    user = models.ForeignKey(User, related_name='friendships', on_delete=models.CASCADE)
    friend = models.ForeignKey(User, on_delete=models.CASCADE)
    # Additional fields as needed

class UserStatus(models.Model):
    user = models.OneToOneField(User, related_name='status', on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
    last_online = models.DateTimeField(null=True, blank=True)
    # Additional fields as needed

class UserLocation(models.Model):
    user = models.OneToOneField(User, related_name='location', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    # Additional fields as needed

class MessageReaction(models.Model):
    message = models.ForeignKey(Message, related_name='reactions', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='message_reactions', on_delete=models.CASCADE)
    emoji = models.CharField(max_length=255)
    # Additional fields as needed

class UserBlock(models.Model):
    user = models.ForeignKey(User, related_name='blocked_users', on_delete=models.CASCADE)
    blocked_user = models.ForeignKey(User, related_name='blocked_by_users', on_delete=models.CASCADE)
    # Additional fields as needed

class UserActivity(models.Model):
    user = models.ForeignKey(User, related_name='activity_logs', on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Additional fields as needed

class UserSettings(models.Model):
    user = models.OneToOneField(User, related_name='settings', on_delete=models.CASCADE)
    theme = models.CharField(max_length=255, choices=[('light', 'Light'), ('dark', 'Dark')], default='light')
    notification_preferences = models.JSONField(default=dict)
    # Additional fields as needed

class Report(models.Model):
    user = models.ForeignKey(User, related_name='reports', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    reason = models.TextField()
    is_resolved = models.BooleanField(default=False)
    # Additional fields as needed

class Poll(models.Model):
    question = models.CharField(max_length=255)
    options = models.JSONField()
    creator = models.ForeignKey(User, related_name='created_polls', on_delete=models.CASCADE)
    # Additional fields as needed

class PollVote(models.Model):
    user = models.ForeignKey(User, related_name='poll_votes', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, related_name='votes', on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=255)
    # Additional fields as needed

class UserReputation(models.Model):
    user = models.OneToOneField(User, related_name='reputation', on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    # Additional fields as needed

class Announcement(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(User, related_name='sent_announcements', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Additional fields as needed

class UserTag(models.Model):
    user = models.ForeignKey(User, related_name='tags', on_delete=models.CASCADE)
    tag = models.CharField(max_length=255)
    # Additional fields as needed

class CustomEmoticon(models.Model):
    user = models.ForeignKey(User, related_name='custom_emoticons', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='custom_emoticons/')
    shortcut = models.CharField(max_length=50, unique=True)
    # Additional fields as needed

class ExternalServiceToken(models.Model):
    user = models.ForeignKey(User, related_name='service_tokens', on_delete=models.CASCADE)
    service_name = models.CharField(max_length=255)
    token = models.TextField()
    # Additional fields as needed

```


![Alt text](conar-cross-woodland-winter-cc.jpg)

## Endpoints

### Authentication Endpoints
- POST /api/token/  # Obtain JWT token for authentication
- POST /api/token/refresh/  # Refresh JWT token

### Users Endpoints
- GET /api/users/  # List all users
- GET /api/users/{user_id}/  # Retrieve user details
- POST /api/users/  # Register a new user
- PATCH /api/users/{user_id}/  # Update user details
- DELETE /api/users/{user_id}/  # Delete user account

### Messaging Endpoints
- GET /api/messages/  # List all messages
- GET /api/messages/{message_id}/  # Retrieve a specific message
- POST /api/messages/  # Send a new message
- PATCH /api/messages/{message_id}/  # Update a message
- DELETE /api/messages/{message_id}/  # Delete a message
---
- GET /api/groups/  # List all groups
- GET /api/groups/{group_id}/  # Retrieve group details
- POST /api/groups/  # Create a new group
- PATCH /api/groups/{group_id}/  # Update group details
- DELETE /api/groups/{group_id}/  # Delete a group
---
- GET /api/group-messages/  # List all group messages
- GET /api/group-messages/{message_id}/  # Retrieve a specific group message
- POST /api/group-messages/  # Send a new group message
- PATCH /api/group-messages/{message_id}/  # Update a group message
- DELETE /api/group-messages/{message_id}/  # Delete a group message
---
- GET /api/polls/  # List all polls
- GET /api/polls/{poll_id}/  # Retrieve poll details
- POST /api/polls/  # Create a new poll
- PATCH /api/polls/{poll_id}/  # Update poll details
- DELETE /api/polls/{poll_id}/  # Delete a poll
---
- POST /api/poll-votes/  # Vote in a poll
---
- GET /api/custom-emoticons/  # List all custom emoticons
- GET /api/custom-emoticons/{emoticon_id}/  # Retrieve a specific custom emoticon
- POST /api/custom-emoticons/  # Create a new custom emoticon
- PATCH /api/custom-emoticons/{emoticon_id}/  # Update a custom emoticon
- DELETE /api/custom-emoticons/{emoticon_id}/  # Delete a custom emoticon
---
- GET /api/message-reactions/  # List all message reactions
- GET /api/message-reactions/{reaction_id}/  # Retrieve a specific message reaction
- POST /api/message-reactions/  # Create a new message reaction
- PATCH /api/message-reactions/{reaction_id}/  # Update a message reaction
- DELETE /api/message-reactions/{reaction_id}/  # Delete a message reaction

### Notifications Endpoints
- GET /api/devices/  # List all devices
- GET /api/devices/{device_id}/  # Retrieve device details
- POST /api/devices/  # Register a new device
- PATCH /api/devices/{device_id}/  # Update device details
- DELETE /api/devices/{device_id}/  # Unregister a device
---
- GET /api/notifications/  # List all notifications
- GET /api/notifications/{notification_id}/  # Retrieve a specific notification
- PATCH /api/notifications/{notification_id}/  # Mark notification as read
- DELETE /api/notifications/{notification_id}/  # Delete a notification

### Profiles Endpoints
- GET /api/user-profiles/  # List all user profiles
- GET /api/user-profiles/{user_id}/  # Retrieve user profile details
- PATCH /api/user-profiles/{user_id}/  # Update user profile details
---
- GET /api/friendships/  # List all friendships
- GET /api/friendships/{friendship_id}/  # Retrieve friendship details
- POST /api/friendships/  # Send a friend request
- PATCH /api/friendships/{friendship_id}/  # Accept or reject a friend request
- DELETE /api/friendships/{friendship_id}/  # Cancel or unfriend
---
- GET /api/user-statuses/  # List all user statuses
- GET /api/user-statuses/{user_id}/  # Retrieve user status
- PATCH /api/user-statuses/{user_id}/  # Update user status
---
- GET /api/user-settings/  # Retrieve user settings
- PATCH /api/user-settings/  # Update user settings

### Reviews Endpoints
- POST /api/user-blocks/  # Block a user
- DELETE /api/user-blocks/{block_id}/  # Unblock a user
---
- POST /api/reports/  # Report inappropriate content
- GET /api/reports/  # List all reports
- GET /api/reports/{report_id}/  # Retrieve a specific report
- PATCH /api/reports/{report_id}/  # Mark report as resolved
- DELETE /api/reports/{report_id}/  # Delete a report
















pip install --upgrade pillow cloudinary cryptography crispy-bootstrap5 django-cors-headers django-countries django-crispy-forms django-ninja django-otp google-auth google-auth-oauthlib gunicorn PyJWT pyotp python-decouple requests social-auth-app-django social-auth-core twilio whitenoise django-unfold django-jazzmin