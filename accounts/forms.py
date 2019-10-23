from django.forms import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model  # 현재 활성화(active)된 user model을 return하는 함수


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model() #accounts.USER
        fields = ['email', 'first_name', 'last_name', ]



# 커스터마이징한 유저모델을 인식하지 못해서 직접 get_user_model 함수로
# 유저 모델정보를 넣어줌
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields