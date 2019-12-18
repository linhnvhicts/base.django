"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from graphene_django.views import GraphQLView
import sys

admin.site.site_header = os.environ.get('ADMIN_SITE_HEADER') or 'Django administration'

urlpatterns = [
    path('api', include('api.urls')),
    path('admin', admin.site.urls),
    path('graphql', GraphQLView.as_view(graphiql=True)),
]

if settings.DEBUG or 'test' in sys.argv:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns