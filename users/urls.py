from django.urls import path, re_path, include
from users import views
from dj_rest_auth.registration.views import VerifyEmailView

urlpatterns = [

    path('signup/', views.UserView.as_view(), name='user_view'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('<int:user_id>/', views.ProfileView.as_view(), name='profilw_view'),
    


]

