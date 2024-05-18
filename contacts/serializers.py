from rest_framework import serializers
from .models import Contact, Phone, Email, Address, SocialMedia

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True, read_only=True)
    emails = EmailSerializer(many=True, read_only=True)
    addresses = AddressSerializer(many=True, read_only=True)
    social_media = SocialMediaSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'