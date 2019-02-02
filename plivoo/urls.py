"""plivoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from contact import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'contacts', views.ContactViewSet)
router.register(r'phone-numbers', views.PhoneViewSet)


urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/rest-auth/', include('rest_auth.urls')),
    url(r'^api/v1/', include('rest_framework.urls', namespace='rest_framework'))
]