from django.utils import timezone
from rest_framework import serializers

from auth_.models import MainUser, Profile

def is_adult_or_old(value):
    age = timezone.now().year - value.year
    if age <= 16 and age <= 63:
        raise serializers.ValidationError('You are not in 16 to 63')


class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = MainUser
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'role')
        extra_kwargs = {'password': {'write_only': True}}


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('email', 'password')


class BaseProfileSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(validators=[is_adult_or_old, ])
    user_id = serializers.IntegerField(write_only=True)

    class Meta(object):
        model = Profile
        fields = '__all__'
        abstract = True


class ProfileSerializer(BaseProfileSerializer):

    class Meta(object):
        model = Profile
        fields = ('id', 'short_bio', 'birth_date', 'user')


class ProfileDetailSerializer(BaseProfileSerializer):

    class Meta(object):
        model = Profile
        fields = ('id', 'short_bio', 'birth_date', 'user', )


class ProfileUpdateSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(validators=[is_adult_or_old])

    class Meta(object):
        model = Profile
        fields = ['short_bio', 'birth_date', 'avatar']
