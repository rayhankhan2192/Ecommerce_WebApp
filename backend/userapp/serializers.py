from rest_framework import serializers
from .models import User, UserAddress

from rest_framework import serializers
from .models import User, UserAddress

class UserRegistrationSerializer(serializers.ModelSerializer):
    city = serializers.CharField(required=False, allow_blank=True)
    post_code = serializers.CharField(required=False, allow_blank=True)
    country = serializers.CharField(required=False, allow_blank=True)
    home = serializers.CharField(required=False, allow_blank=True)
    
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'phone',
            'password',
            'password2',
            'city', 
            'post_code', 
            'country', 
            'home'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        # Remove password2 from validated_data
        validated_data.pop('password2')
        
        # Extract address fields from validated_data
        address_data = {
            'city': validated_data.pop('city', ''),
            'post_code': validated_data.pop('post_code', ''),
            'country': validated_data.pop('country', ''),
            'home': validated_data.pop('home', '')
        }
        
        # Create user instance
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        
        # Create address for the user if any address data was provided
        UserAddress.objects.create(user=user, **address_data)
        
        return user
