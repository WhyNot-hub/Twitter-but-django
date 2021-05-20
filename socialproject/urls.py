from django.urls import include, path
from django.conf.urls import include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from . import settings

urlpatterns = [
    path('', include('backend.urls')),
    path('', include('frontend.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [path('api-auth/', include('rest_framework.urls')),]

