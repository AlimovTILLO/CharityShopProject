# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from models import Comments


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']
        widgets = {
            'comments_text': forms.Textarea(attrs={'cols': 120, 'rows': 5})
        }


#class ItemPostForm(ModelForm):
#    class Meta:
#        model = Item
#        fields = ('item_title', 'item_image', 'item_category', 'item_description', 'item_price', 'item_foundation',
#                  'item_charity')
