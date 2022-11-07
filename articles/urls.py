from django.urls import path
from articles import views

urlpatterns = [
    path('', views.ArticlesView.as_view(), name ='articles_view' ), #영화 전체 리스트(노우석님)
    path('category/<int:category_id>/', views.ArticlesCategoryView.as_view(), name= 'category_view'), # 영화 카테고리 분류
    path('<int:movie_id>/', views.ArticlesDetailView.as_view(), name = 'articles_detail_view'), #영화 상세 보기(양기철님)
    path('<int:movie_id>/like/', views.ArticlesMovieLikeView.as_view(), name = 'movie_like_view'), #영화 좋아요(성창남님)
    path('<int:movie_id>/comment/', views.ArticlesCommentView.as_view(), name = 'articles_comment_view'), #영화 리뷰(작성)(노우석님)
    path('<int:movie_id>/comment/<int:comment_id>/like/', views.ArticlesCommentLikeView.as_view(), name = 'articles_comment_like_view'), #영화리뷰좋아요(성창남님)
    path('<int:movie_id>/comment/<int:comment_id>/', views.ArticlesCommentDetailView.as_view(), name = 'articles_comment_detail_view'),  #영화 리뷰(수정,삭제)(노우석님)
    path('search/', views.ArticlesSearchView.as_view(), name = 'articles_search_view'), #검색(양기철님)
]
