from rest_framework.serializers import (
    ModelSerializer, 
    HyperlinkedIdentityField, 
    SerializerMethodField,
)

from accounts.api.serializers import UserDetailSerializer
from comments.api.serializers import CommentSerializer
from comments.models import Comment

from posts.models import Post

post_detail_url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='pk'
    )

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish'
        ]

class PostListSerializer(ModelSerializer):
    url = post_detail_url
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Post
        fields = [
            'pk',
            'url',
            'user',
            'title',
            'content'
        ]
    

class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    user = UserDetailSerializer(read_only=True)
    image = SerializerMethodField()
    markdown = SerializerMethodField()
    comments = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'pk',
            'url',
            'user',
            'title',
            'slug',
            'content',
            'markdown',
            'publish',
            'image',
            'comments'
        ]

    def get_markdown(self, obj):
        return obj.get_markdown()

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def get_comments(self, obj):
        content_type = obj.get_content_type
        object_id = obj.id
        comment_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(comment_qs, many=True).data
        return comments