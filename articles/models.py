from django.db import models
from users.models import User
from django.conf import settings

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "category"
    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, default='')
    
    def __str__(self):
        return self.name


class Movie(models.Model):

    movie_id = models.CharField(max_length =50)
    image = models.URLField() # poster_url
    original_title = models.CharField(max_length =50) # 영문 제목
    title = models.CharField(max_length =50) # 한글 제목
    release_year = models.CharField(max_length =50) # release_date
    rating = models.CharField(max_length =50) # rank
    description = models.TextField() # overview
    movie_like = models.ManyToManyField(User, related_name="like_movie",blank=True)
    category = models.ManyToManyField(Category,symmetrical=False,related_name='movies')
    
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    comment_like = models.ManyToManyField(User, related_name="like_comment",blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,blank=True, related_name="movie_comment")
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    
    def __str__(self):
        return str(self.content)

