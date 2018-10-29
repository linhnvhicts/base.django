from django.conf.urls import url, include
from .views import LogEntryViewSet, UserViewSet
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'log-entry', LogEntryViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]