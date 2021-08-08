from rest_framework import serializers

from auth.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    profile_picture = serializers.SerializerMethodField('get_profile_picture')
    
    class Meta:
        model = UserProfile
        fields = ['user_id', 'bio', 'profile_picture', 'youtube', 'instagram', 'twitter']
        read_only_fields = ['user_id']
    
    def get_profile_picture(self, profile):
        return profile.profile_picture.url
