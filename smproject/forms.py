from django import forms
from .models import Post, New, Parallax, Comment, Client, Portfolio, Newsgrid, Workgrid


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'details']
        labels = {
            'name': 'name',
            'details': 'details',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.TextInput(attrs={'class': 'form-control'}),
        }


class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ['news_user', 'news_image', 'news_category', 'news_topic', 'news_details', 'news_created_at']
        labels = {
            'news_user': 'news_user',
            'news_image': 'news_image',
            'news_category': 'news_category',
            'news_topic': 'news_topic',
            'news_details': 'news_details',
            'news_created_at': 'news_created_at'
        }

        widgets = {
            'news_user': forms.TextInput(attrs={'class': 'form-control'}),
            'news_category': forms.TextInput(attrs={'class': 'form-control'}),
            'news_topic': forms.TextInput(attrs={'class': 'form-control'}),
            'news_details': forms.TextInput(attrs={'class': 'form-control'}),

        }

class NewsgridForm(forms.ModelForm):
    class Meta:
        model = Newsgrid
        fields = ['ngrid_user', 'ngrid_image', 'category', 'ngrid_created_at', 'ngrid_description']
        labels = {
            'ngrid_user': 'ngrid_news_user',
            'ngrid_image': 'ngrid_image',
            'category': 'category',
            'ngrid_description': 'ngrid_description',
            'ngrid_created_at': 'ngrid_created_at'
        }

        widgets = {
            'ngrid_user': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'ngrid_description': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ParallaxForm(forms.ModelForm):
    class Meta:
        model = Parallax
        fields = ['work_image', 'desc_work']
        labels = {
            'work_image': 'work_image',
            'desc_work': 'desc_work' 
        }

        widgets = {
            'desc_work': forms.TextInput(attrs={'class': 'form-control'}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'commentator', 'commentator_position']
        labels = {
            'comment': 'comment',
            'commentator': 'commentator',
            'commentator_position': 'commentator_position' 
        }

        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
            'commentator': forms.TextInput(attrs={'class': 'form-control'}),
            'commentator_position': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_image']
        labels = {
            'client': 'client', 
        }


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['news_image', 'title', 'description']
        labels = {
            'news_image': 'news_image',
            'title': 'title',
            'description': 'description' 
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),

        }

class WorkgridForm(forms.ModelForm):
    class Meta:
        model = Workgrid
        fields = ['ngrid_image', 'category', 'ngrid_description']
        labels = {
            'ngrid_image': 'ngrid_image',
            'category': 'category',
            'ngrid_description': 'news_description',
        }

        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'ngrid_description': forms.TextInput(attrs={'class': 'form-control'}),

        }