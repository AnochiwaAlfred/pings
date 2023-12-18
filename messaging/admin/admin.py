from django.contrib import admin
from messaging.models import *

# Register your models here.


@admin.register(ChatGroup)
class ChatGroupAdmin(admin.ModelAdmin):
    list_display = CHAT_GROUP_LIST_DISPLAY

    class Meta:
        verbose_name_plural = 'Chat Groups'

@admin.register(CustomEmoticon)
class CustomEmoticonAdmin(admin.ModelAdmin):
    list_display = CUSTOM_EMOTICON_LIST_DISPLAY

    class Meta:
        verbose_name_plural = 'Custom Emoticons'

@admin.register(GroupMessage)
class GroupMessageAdmin(admin.ModelAdmin):
    list_display = GROUP_MESSAGE_LIST_DISPLAY

    class Meta:
        verbose_name_plural = 'Group Messages'

@admin.register(MessageReaction)
class MessageReactionAdmin(admin.ModelAdmin):
    list_display = MESSAGE_REACTION_LIST_DISPLAY

    class Meta:
        verbose_name_plural = 'Message Reactions'

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = MESSAGE_LIST_DISPLAY

    class Meta:
        verbose_name_plural = 'Messages'

@admin.register(PollVote)
class PollVoteAdmin(admin.ModelAdmin):
    list_display = POLL_VOTE_LIST_DISPLAY

    class Meta:
        verbose_name_plural = 'PollVotes'

@admin.register(PollOption)
class PollOptionAdmin(admin.ModelAdmin):
    list_display = POLL_OPTION_LIST_DISPLAY

    class Meta:
        verbose_name_plural = 'PollOptions'

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = POLL_LIST_DISPLAY

    class Meta:
        verbose_name_plural = 'Polls'


