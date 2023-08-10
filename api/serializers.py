from rest_framework import serializers
from profiles.models import Profile
from posts.models import Post
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','user','bio','email','country','avatar','friends','slug','updated','created','objects']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['content', 'image', 'liked', 'updated', 'created', 'author']

