from django import forms
from .models import Article, Comment

# form은 데이터를 받아 검증 후 저장한다!



class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        
        fields = '__all__'


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment

        fields = ['content']