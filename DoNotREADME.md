
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
- [ ] POST /api/token  <font color="cornflowerblue">**# Obtain JWT token for authentication**</font>
- [ ] POST /api/token/refresh  <font color="cornflowerblue">**# Refresh JWT token**</font>

### Users Endpoints
- [x] GET /api/users  <font color="cornflowerblue">**# List all users**</font>
- [x] GET /api/users/{user_id}  <font color="cornflowerblue">**# Retrieve user details**</font>
- [x] POST /api/users  <font color="cornflowerblue">**# Register a new user**</font>
- [x] PATCH /api/users/{user_id}  <font color="cornflowerblue">**# Update user details**</font>
- [x] DELETE /api/users/{user_id}  <font color="cornflowerblue">**# Delete user account**</font>

### Messaging Endpoints
- [x] GET /api/messages  <font color="cornflowerblue">**# List all messages**</font>
- [x] GET /api/{user_id}/sent_messages  <font color="cornflowerblue">**# List all user sent messages**</font>
- [x] GET /api/{user_id}/received_messages  <font color="cornflowerblue">**# List all user received messages**</font>
- [x] GET /api/{user_id}/messages  <font color="cornflowerblue">**# List all user messages, sent or received**</font>
- [x] GET /api/{user1_id}/{user2_id}/messages  <font color="cornflowerblue">**# List all messages between two users**</font>
- [x] GET /api/{sender_id}/{receiver_id}/messages_sent  <font color="cornflowerblue">**# List all messages from sender to receiver**</font>
- [x] GET /api/messages/{message_id}  <font color="cornflowerblue">**# Retrieve a specific message**</font>
- [x] POST /api/messages  <font color="cornflowerblue">**# Send a new message**</font>
- [ ] PATCH /api/messages/{message_id}  <font color="cornflowerblue">**# Update a message**</font>
- [x] DELETE /api/messages/{message_id}  <font color="cornflowerblue">**# Delete a message**</font>
---
- [x] GET /api/groups  <font color="cornflowerblue">**# List all groups**</font>
- [x] GET /api/groups/{group_id}  <font color="cornflowerblue">**# Retrieve group details**</font>
- [x] POST /api/groups  <font color="cornflowerblue">**# Create a new group**</font>
- [x] PATCH /api/groups/{group_id}  <font color="cornflowerblue">**# Update group details**</font>
- [x] DELETE /api/groups/{group_id}  <font color="cornflowerblue">**# Delete a group**</font>
---
- [x] GET /api/group-messages  <font color="cornflowerblue">**# List all group messages**</font>
- [x] GET /api/{group_id}/group-messages  <font color="cornflowerblue">**# List all group messages in a particular group**</font>
- [x] GET /api/{group_id}/{sender_id}/group-messages  <font color="cornflowerblue">**# List all group messages in a particular group from a </font>particular user**
- [x] GET /api/group-messages/{message_id}  <font color="cornflowerblue">**# Retrieve a specific group message**</font>
- [x] POST /api/group-messages  <font color="cornflowerblue">**# Send a new group message**</font>
- [ ] PATCH /api/group-messages/{message_id}  <font color="cornflowerblue">**# Update a group message**</font>
- [x] DELETE /api/group-messages/{message_id}  <font color="cornflowerblue">**# Delete a group message**</font>
---
- [x] GET /api/polls  <font color="cornflowerblue">**# List all polls**</font>
- [x] GET /api/polls/{poll_id}  <font color="cornflowerblue">**# Retrieve poll details**</font>
- [x] POST /api/polls/create  <font color="cornflowerblue">**# Create a new poll**</font>
- [ ] PATCH /api/polls/{poll_id}  <font color="cornflowerblue">**# Update poll details**</font>
- [x] POST /api/poll-options/create  <font color="cornflowerblue">**# Add poll options to a poll / Create Poll option**</font>
- [x] DELETE /api/polls/{poll_id}  <font color="cornflowerblue">**# Delete a poll**</font>
---
- [x] GET /api/poll-options/list  <font color="cornflowerblue">**# List all poll options**</font>
- [x] GET /api/poll-options/{poll_option_id}  <font color="cornflowerblue">**# Retrieve specific poll option details**</font>
- [x] GET /api/poll-options/{poll_id}  <font color="cornflowerblue">**# List poll options for a poll**</font>
- [x] DELETE /api/poll-options/{poll_option_id}/delete  <font color="cornflowerblue">**# Delete poll options / Remove from a poll**</font>
---
- [x] GET /api/poll-votes/list  <font color="cornflowerblue">**# Retrieve poll votes list**</font>
- [x] GET /api/poll-votes/{poll_vote_id}  <font color="cornflowerblue">**# Retrieve specific poll vote details**</font>
- [x] GET /api/poll-votes/{poll_id}  <font color="cornflowerblue">**# Retrieve poll votes list for a particular poll**</font>
- [x] GET /api/poll-votes/{poll_option_id}  <font color="cornflowerblue">**# Retrieve all poll votes for a particular poll option**</font>
- [x] POST /api/poll-votes/create   <font color="cornflowerblue">**# Vote in a poll / Create a poll vote**</font>
- [x] DELETE /api/poll-votes/{poll_vote_id}/delete  <font color="cornflowerblue">**# Delete poll vote / Remove from a poll**</font>
---
- [x] GET /api/custom-emoticons  <font color="cornflowerblue">**# List all custom emoticons**</font>
- [x] GET /api/custom-emoticons/{emoticon_id}  <font color="cornflowerblue">**# Retrieve a specific custom emoticon**</font>
- [x] POST /api/custom-emoticons  <font color="cornflowerblue">**# Create a new custom emoticon**</font>
- [ ] PATCH /api/custom-emoticons/{emoticon_id}  <font color="cornflowerblue">**# Update a custom emoticon**</font>
- [x] DELETE /api/custom-emoticons/{emoticon_id}  <font color="cornflowerblue">**# Delete a custom emoticon**</font>
---
- [x] GET /api/message-reactions  <font color="cornflowerblue">**# List all message reactions**</font>
- [x] GET /api/message-reactions/{reaction_id}  <font color="cornflowerblue">**# Retrieve a specific message reaction**</font>
- [x] POST /api/message-reactions  <font color="cornflowerblue">**# Create a new message reaction**</font>
- [ ] PATCH /api/message-reactions/{reaction_id}  <font color="cornflowerblue">**# Update a message reaction**</font>
- [x] DELETE /api/message-reactions/{reaction_id}  <font color="cornflowerblue">**# Delete a message reaction**</font>

### Notifications Endpoints
- [x] GET /api/devices  <font color="cornflowerblue">**# List all devices**</font>
- [x] GET /api/{user_id}/devices  <font color="cornflowerblue">**# List all devices for user**</font>
- [x] GET /api/devices/{device_id}  <font color="cornflowerblue">**# Retrieve device details**</font>
- [x] POST /api/devices  <font color="cornflowerblue">**# Register a new device**</font>
- [ ] PATCH /api/devices/{device_id}  <font color="cornflowerblue">**# Update device details**</font>
- [x] DELETE /api/devices/{device_id}  <font color="cornflowerblue">**# Unregister a device**</font>
---
- [x] GET /api/notifications  <font color="cornflowerblue">**# List all notifications**</font>
- [x] GET /api/notifications/{notification_id}  <font color="cornflowerblue">**# Retrieve a specific notification**</font>
- [x] GET /api/notifications/{user_id}/notifications  <font color="cornflowerblue">**# List a specific user's notifications**</font>
- [x] PATCH /api/notifications/{notification_id}/mark-as-read  <font color="cornflowerblue">**# Mark notification as read**</font>
- [x] DELETE /api/notifications/{notification_id}  <font color="cornflowerblue">**# Delete a notification**</font>

### Profiles Endpoints
- [ ] GET /api/user-profiles  <font color="cornflowerblue">**# List all user profiles**</font>
- [ ] GET /api/user-profiles/{user_id}  <font color="cornflowerblue">**# Retrieve user profile details**</font>
- [ ] PATCH /api/user-profiles/{user_id}  <font color="cornflowerblue">**# Update user profile details**</font>
---
- [x] GET /api/friendships  <font color="cornflowerblue">**# List all friendships**</font>
- [x] GET /api/friendships/{friendship_id}  <font color="cornflowerblue">**# Retrieve friendship details**</font>
- [x] GET /api/friendships/{user_id}/friends  <font color="cornflowerblue">**# List all of a users friends**</font>
- [x] POST /api/friendships  <font color="cornflowerblue">**# Send a friend request**</font>
- [x] PATCH /api/friendships/{friendship_id}/accept  <font color="cornflowerblue">**# Accept a friend request**</font>
- [x] DELETE /api/friendships/{friendship_id}  <font color="cornflowerblue">**# Cancel or unfriend**</font>
---
- [ ] GET /api/user-settings  <font color="cornflowerblue">**# Retrieve user settings**</font>
- [ ] PATCH /api/user-settings  <font color="cornflowerblue">**# Update user settings**</font>

### Reviews Endpoints
- [ ] POST /api/user-blocks  <font color="cornflowerblue">**# Block a user**</font>
- [ ] DELETE /api/user-blocks/{block_id}  <font color="cornflowerblue">**# Unblock a user**</font>
---
- [ ] POST /api/reports  <font color="cornflowerblue">**# Report inappropriate content**</font>
- [ ] GET /api/reports  <font color="cornflowerblue">**# List all reports**</font>
- [ ] GET /api/reports/{report_id}  <font color="cornflowerblue">**# Retrieve a specific report**</font>
- [ ] PATCH /api/reports/{report_id}  <font color="cornflowerblue">**# Mark report as resolved**</font>
- [ ] DELETE /api/reports/{report_id}  <font color="cornflowerblue">**# Delete a report**</font>








