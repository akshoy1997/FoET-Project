from django.conf.urls import include
from django.conf.urls import url
from rest_framework import routers

from blackboard.api.users import UsersViewSet

"""
If unset the basename will be automatically generated based on the queryset attribute of the viewset, 
if it has one. Note that if the viewset does not include a queryset 
attribute then you must set basename when registering the viewset.
"""
router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
