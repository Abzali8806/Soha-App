from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form__txt__input', 'id': 'title_input', 'placeholder':'Title'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'class':'form__txt__input', 'id': 'author_input', 'placeholder':'Author'}))
    category = forms.CharField(widget=forms.TextInput(attrs={'class':'form__txt__input', 'id': 'category_input', 'placeholder':'Category'}))
    class Meta:
        model = Article
        fields = ['title', 'category', 'author', 'body']
        # widgets={
        #     'title': forms.CharField(attrs={'class':'form__txt__input', 'id': 'title_input'}),
        #     'author': forms.CharField(attrs={'class':'form__txt__input', 'id': 'author_input'}),
        #     'category': forms.CharField(attrs={'class':'form__txt__input', 'id': 'category_input'}),
        #     'body': forms.RichTextField(attrs={'class':'rich_editor', 'id': 'sbox_pub_input'})
        # }