from rest_framework import serializers
from api.models import Category, Photo, Comment
from auth_.models import MainUser


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    img = serializers.ImageField()

    def create(self, validated_data):
        category = Category.objects.create(name=validated_data.get('name'), img=validated_data.get('img'))
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.img = validated_data.get('img', instance.img)
        instance.save()
        return instance


class CategorySerializer2(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'img')


class PhotoSerializer(serializers.ModelSerializer):
    # category_id = serializers.IntegerField(write_only=True)
    # user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Photo
        fields = ('id', 'name', 'description', 'price', 'user', 'category', 'img')


class CategoryWithPhotosSerializer(serializers.ModelSerializer):
    # vacancies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # vacancies = serializers.StringRelatedField(many=True, read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'photos')


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta(object):
        model = MainUser
        fields = ('id', 'email', 'first_name', 'last_name',
                  'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class CommentSerializer(serializers.ModelSerializer):
    photo_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'username', 'text', 'date', 'photo_id')
