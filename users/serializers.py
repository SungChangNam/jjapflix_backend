from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


VALID_EMAIL_LIST = ["naver.com", "gmail.com", "daum.net"]



class UserProfileSerializer(serializers.ModelSerializer):  # 프로필 조회
    class Meta:
        model = User
        fields="__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
    def validate(self, data):
        if data.get("email", "").split('@')[-1] not in VALID_EMAIL_LIST:
            raise serializers.ValidationError(
                detail={"error": "naver, gmail, daum 이메일 주소만 사용 가능합니다."}
            )
        return data    
    
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password) # 패스워드 해싱
        user.save()
        return user


    def update(self, instance, validated_data): # 비밀번호 수정 
        instance.password = validated_data.get('password', instance.password)
        instance.set_password('password') # 패스워드 해싱
        instance.save()
        return instance
       
        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):   # jwt payload 커스텀
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email

        return token
    
class UserUpdateSerializer(serializers.ModelSerializer):  # 프로필 조회
    class Meta:
        model = User
        fields=("nickname", "password")
        
    def update(self, instance, validated_data): # 비밀번호 수정 
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                continue
            setattr(instance, key, value)
            
        instance.save()
        
        return instance