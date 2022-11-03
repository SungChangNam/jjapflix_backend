from django.db import models
from users.models import User

# Create your models here.
class Movie(models.Model):

    movie_id = models.CharField(max_length =50)
    image = models.URLField()
    title = models.CharField(max_length =50)
    release_year = models.DecimalField(max_digits=8, decimal_places=0)
    rating = models.CharField(max_length =50)
    duration = models.CharField(max_length =50)
    description = models.TextField()
    movie_like = models.ManyToManyField(User, related_name="like_movie",blank=True)
    category = models.CharField(max_length=20, null =True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    comment_like = models.ManyToManyField(User, related_name="like_comment",blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,blank=True, related_name="movie_comment")
    rating = models.CharField(max_length=10, blank=True)
    
    def __str__(self):
        return str(self.content)

