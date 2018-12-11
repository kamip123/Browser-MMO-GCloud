from rest_framework import serializers
from .models import Alliance, Forum, SubForum, Topic, PostForum
from mainPage.serializers import UserSerializer


class AllianceSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Alliance
        fields = ('name', 'creator', 'vice_creator', 'alliance_logo', 'alliance_bio', 'members')


class PostForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostForum
        fields = ('author', 'text', 'created_date')


class TopicSerializer(serializers.ModelSerializer):
    posts = PostForumSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ('title', 'posts')


class SubForumSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = SubForum
        fields = ('title', 'topics')


class ForumSerializer(serializers.ModelSerializer):
    sub_forums = SubForumSerializer(many=True, read_only=True)

    class Meta:
        model = Forum
        fields = ('sub_forums', 'owner')
