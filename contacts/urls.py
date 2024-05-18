from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AddressViewSet,
    ContactViewSet,
    EmailViewSet,
    PhoneViewSet,
    SocialMediaViewSet,
)

router = DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'phones', PhoneViewSet)
router.register(r'emails', EmailViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'socialmedia', SocialMediaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'contacts/<int:pk>/profile_image/',
        ContactViewSet.as_view({'get': 'profile_image'}),
    ),
]
