
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.static import serve
from apis.api import api as api
# from apis.v1.clientAuth import google_authenticate


VERSION = "v1"

urlpatterns = [
    # ADMIN DASH
    
    path('admin/', admin.site.urls),
    # path('', include('admin_datta.urls')),
    # path('', include('admin_corporate.urls')),
    # path('', include('admin_argon.urls')),
    # path('', include('admin_soft.urls')),
    
    # API URLS
    path(f"api/{VERSION}/", api.urls),
    
    # MEDIA URLS
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    # re_path(r'^auth/', include('social_django.urls', namespace='social')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = urlpatterns + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
