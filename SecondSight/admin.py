from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from . models import *


class NewspostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Newspost
        fields = [
            'title',
            'image',
            'group_id',
            'text',
            'manage',
        ]


class NewspostAdmin(admin.ModelAdmin):
    form = NewspostAdminForm


class CoverBannerAdminForm(forms.ModelForm):
    tag_line = forms.CharField(widget=CKEditorWidget())
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = CoverBanner
        fields = [
            'title',
            'image',
            'tag_line',
            'description',
        ]


class CoverBannerAdmin(admin.ModelAdmin):
    form = CoverBannerAdminForm


class StickyAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

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


class StickyAdmin(admin.ModelAdmin):
    form = StickyAdminForm



class UserAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = User
        fields = [
            'name',
            'image',
            'description',
        ]


class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm


# Register your models here.
admin.site.register(Newspost, NewspostAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Chapter)
admin.site.register(Comic)
admin.site.register(Image)
admin.site.register(Sticky, StickyAdmin)
admin.site.register(CoverBanner, CoverBannerAdmin)