
from ninja import NinjaAPI, Router
from ninja.security import django_auth
from django.http import HttpResponseForbidden
from users.models import CustomUser
from django.http import HttpResponseForbidden, response
from http import HTTPStatus
from decouple import config 

from apis.v1.auth import router as auth_router
from apis.v1.messaging.chatgroups import router as chatgroups_router
from apis.v1.messaging.custom_emoticons import router as custom_emoticons_router
from apis.v1.messaging.group_messages import router as group_messages_router
from apis.v1.messaging.messages import router as messages_router
from apis.v1.notifications import router as notifications_router
from apis.v1.messaging.polls import router as polls_router
from apis.v1.profiles import router as profiles_router
from apis.v1.reviews import router as reviews_router
from apis.v1.users import router as users_router
from apis.v1.os import router as os_router

# from plugins.email_token import sendUserEmail
from django.utils import timezone
from ninja.security import HttpBearer


class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        meta = request.META
        # HTTP_USER_AGENT = meta.get('HTTP_USER_AGENT')
        user =  CustomUser.objects.all().filter(token=token)
        if user.exists():
            foundUser = user.get()
        #     # on production check
        #     recipent_list =  f"{foundUser.email}" if config('ENVIRONMENT') == "production" else "anointedngeorge@gmail.com"
            
        #     sendUserEmail(
        #         recipient_list=recipent_list,
        #         subject=f'Login Notification <{foundUser.email}>',
        #         context={
        #                 'email': foundUser.email,
        #                 'message_date':timezone.now(),
        #                 "agent":str(HTTP_USER_AGENT),
        #             },
        #             template='login_template.html'
        #     )

            return foundUser.token
            # return True
    def on_auth_fail(self, response):
        return HttpResponseForbidden("Failed to authenticate! or maybe you requested for a password change.")
    

authenticator =  GlobalAuth() if config('ENVIRONMENT') == 'production' else None
api = NinjaAPI(
    auth=None,
    # auth=authenticator,
    title="Spotipy",
    description="This is an API with dynamic OpenAPI info section",
)

# let this be the first one.
api.add_router("/auth/", auth_router)
# -----------------------------------------------------
api.add_router("/chatgroups/", chatgroups_router)
api.add_router("/custom_emoticons/", custom_emoticons_router)
api.add_router("/group_messages/", group_messages_router)
api.add_router("/messages/", messages_router)
api.add_router("/notifications/", notifications_router)
api.add_router("/polls/", polls_router)
api.add_router("/profiles/", profiles_router)
api.add_router("/reviews/", reviews_router)
api.add_router("/users/", users_router)




if config("ENVIRONMENT") == "development":
    api.add_router("/os/", os_router)
