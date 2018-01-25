# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:32:26 2018

@author: kreamas
"""

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text')