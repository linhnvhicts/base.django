from django.conf.urls import url, include
from .views import LogEntryViewSet
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'log-entry', LogEntryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]