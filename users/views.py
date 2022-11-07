from django.shortcuts import render, redirect
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from users import serializers
from json import JSONDecodeError
from django.http import JsonResponse
from users.models import User
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from users.serializers import UserProfileSerializer, UserUpdateSerializer
import os
import requests
from allauth.socialaccount.models import SocialAccount
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
BASE_URL = 'http://127.0.0.1:8000/'
KAKAO_CALLBACK_URI = BASE_URL + 'users/kakao/callback/'
class UserView(APIView):
     
    def delete(self, request): # 회원탈퇴
        if request.user.is_authenticated:
            request.user.delete()
            return Response("탈퇴되었습니다!", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)


class ProfileView(APIView):  # 회원정보 조회
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserProfileSerializer(user)  
        return Response(serializer.data)
    
    def put(self, request, user_id): # 회원정보 수정
        user = User.objects.get(id=user_id)
        serializer = UserUpdateSerializer(user, data=request.data, partial=True, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class ConfirmEmailView(APIView): # 이메일 인증
    
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)
        # A React Router Route will handle the failure scenario
        return HttpResponseRedirect('/') # 인증성공

    def get_object(self, queryset=None):
        key = self.kwargs['key']
        email_confirmation = EmailConfirmationHMAC.from_key(key)
        if not email_confirmation:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                email_confirmation = queryset.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:
                # A React Router Route will handle the failure scenario
                return HttpResponseRedirect('/') # 인증실패
        return email_confirmation

    def get_queryset(self):
        qs = EmailConfirmation.objects.all_valid()
        qs = qs.select_related("email_address__user")
        return qs

def kakao_login(request):
    client_id = os.environ.get("SOCIAL_AUTH_KAKAO_CLIENT_ID")
    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={KAKAO_CALLBACK_URI}&response_type=code&scope=account_email")


def kakao_callback(request):
    client_id = os.environ.get("SOCIAL_AUTH_KAKAO_CLIENT_ID")
    code = request.GET.get("code")

    # code로 access token 요청
    token_request = requests.get(f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={KAKAO_CALLBACK_URI}&code={code}")
    token_response_json = token_request.json()

    # 에러 발생 시 중단
    error = token_response_json.get("error", None)
    if error is not None:
        raise JSONDecodeError(error)

    access_token = token_response_json.get("access_token")
    profile_request = requests.post(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    profile_json = profile_request.json()

    kakao_account = profile_json.get("kakao_account")
    email = kakao_account.get("email", None) # 이메일!

    # 이메일 없으면 오류 => 카카오톡 최신 버전에서는 이메일 없이 가입 가능해서 추후 수정해야함
    if email is None:
        return JsonResponse({'err_msg': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)
    
#     email_req_json = email_req.json()
#     email = email_req_json.get('email')
    

# try:   # 전달받은 이메일로 등록된 유저가 있는지 탐색
#     user = User.objects.get(email=email)

#     # FK로 연결되어 있는 socialaccount 테이블에서 해당 이메일의 유저가 있는지 확인
#     social_user = SocialAccount.objects.get(user=user)

#         # 있는데 구글계정이 아니어도 에러
#     if social_user.provider != 'google':
#         return JsonResponse({'err_msg': 'no matching social type'}, status=status.HTTP_400_BAD_REQUEST)

#         # 이미 Google로 제대로 가입된 유저 => 로그인 & 해당 우저의 jwt 발급
#         data = {'access_token': access_token, 'code': code}
#         accept = requests.post(f"{BASE_URL}api/user/google/login/finish/", data=data)
#         accept_status = accept.status_code

#         # 뭔가 중간에 문제가 생기면 에러
#         if accept_status != 200:
#             return JsonResponse({'err_msg': 'failed to signin'}, status=accept_status)

#         accept_json = accept.json()
#         accept_json.pop('user', None)
#         return JsonResponse(accept_json)

# except User.DoesNotExist:
#             # 전달받은 이메일로 기존에 가입된 유저가 아예 없으면 => 새로 회원가입 & 해당 유저의 jwt 발급
#             data = {'access_token': access_token, 'code': code}
#             accept = requests.post(f"{BASE_URL}api/user/google/login/finish/", data=data)
#             accept_status = accept.status_code

#             # 뭔가 중간에 문제가 생기면 에러
#             if accept_status != 200:
#                 return JsonResponse({'err_msg': 'failed to signup'}, status=accept_status)

#             accept_json = accept.json()
#             accept_json.pop('user', None)
#             return JsonResponse(accept_json)
            
#         except SocialAccount.DoesNotExist:
#             # User는 있는데 SocialAccount가 없을 때 (=일반회원으로 가입된 이메일일때)
#             return JsonResponse({'err_msg': 'email exists but not social user'}, status=status.HTTP_400_BAD_REQUEST)

class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    callback_url = KAKAO_CALLBACK_URI
    client_class = OAuth2Client