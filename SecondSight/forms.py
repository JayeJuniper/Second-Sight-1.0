from django import forms
from django.utils import timezone


from .models import *

class NewsForm(forms.ModelForm):
    class Meta:
        model = Newspost
        fields = [
            'title',
            'image',
            'group_id',
            'text',
            'manage',
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'image',
            'description',
        ]


class StickyForm(forms.ModelForm):
    class Meta:
        model = Sticky
        fields = [
            'name',
            'image',
            'description',
            'status',
            'date',
            'manage',
        ]


class ComicForm(forms.ModelForm):
    class Meta:
        model = Comic
        fields = [
            'title',
            'image',
            'chapter',
            'page_number',
            'group_id',
            'description',
            'transcript',
        ]


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = [
            'title',
            'image',
            'description',
            'manage',
        ]