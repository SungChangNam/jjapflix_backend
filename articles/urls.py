from django.urls import path
from articles import views

urlpatterns = [
    path('', views.ArticlesView.as_view(), name ='articles_view' ),
    path('<int:movie_id>/', views.ArticlesDetailView.as_view(), name = 'articles_detail_view'),
    path('<int:movie_id>/like/', views.ArticlesMovieLikeView.as_view(), name = 'movie_like_view'),
    path('<int:movie_id>/comment/', views.ArticlesCommentView.as_view(), name = 'articles_comment_view'),
    path('<int:movie_id>/comment/<int:comment_id>/like/', views.ArticlesCommentLikeView.as_view(), name = 'articles_comment_like_view'),
    path('<int:movie_id>/comment/<int:comment_id>/', views.ArticlesCommentDetailView.as_view(), name = 'articles_comment_detail_view'),
    path('search/', views.ArticlesSearchView.as_view(), name = 'articles_search_view'),
]
