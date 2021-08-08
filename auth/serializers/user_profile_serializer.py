from rest_framework import serializers

from auth.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    profile_picture = serializers.SerializerMethodField('get_profile_picture')
    
    class Meta:
        model = UserProfile
        fields = '__all__'
    
    def get_profile_picture(self, profile):
        return profile.profile_picture.url
