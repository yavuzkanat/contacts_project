from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Contact, Phone, Email, Address, SocialMedia
from .serializers import ContactSerializer, PhoneSerializer, EmailSerializer, AddressSerializer, SocialMediaSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @action(detail=True, methods=['get'])
    def profile_image(self, request, pk=None):
        contact = self.get_object()
        contact.get_social_media_image()
        if contact.img_url:
            return Response({'image_url': contact.img_url}, status=status.HTTP_200_OK)
        return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
