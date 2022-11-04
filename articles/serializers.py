from rest_framework import serializers

from articles.models import Movie,Comment
from users.models import User

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    comment_like_count= serializers.SerializerMethodField()


    def get_comment_like_count(self, obj):
        return obj.comment_like.count()

    def get_user(self, obj):
        return obj.user.nickname

    class Meta:
        model = Comment
        fields=('user', 'content','created_at', 'comment_like_count', 'rating',)




class ArticleSerializer(serializers.ModelSerializer):


    class Meta:
        model = Movie
        fields='__all__'


class MovieLikeUserNickname(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname',]


class ArticleListSerializer(serializers.ModelSerializer):

    movie_like_count= serializers.SerializerMethodField()


    def get_movie_like_count(self, obj):
        return obj.movie_like.count()

    class Meta:
        model = Movie
        fields='__all__'


    
    


class MovieCommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = Comment
        fields='__all__'


class ArticleDetailSerializer(serializers.ModelSerializer):
    movie_comment = CommentSerializer(many=True)

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Movie
        fields='__all__'

