#coding: utf-8
from django import forms
from .models import Atl, Tour, Group

class AtlForm(forms.ModelForm):
    tour = forms.ModelChoiceField(required=True, widget=forms.Select(attrs={
        'class': 'form-control'
    }), queryset=Tour.objects.filter(is_published=True), label=u'Турнир')
    group = forms.ModelMultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple(), queryset=Group.objects.filter(is_published=True), label=u'Группа')
    dancer1 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': u'введите № книжки'
    }), required=True, label=u'Партнер 1')
    dancer2 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': u'введите № книжки'
    }), required=True, label=u'Партнер 2')
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': u'Почта'
    }), required=True, label=u'Почта')

    class Meta:
        model = Atl
        fields = ('tour', 'group', 'dancer1', 'dancer2', 'email',  )