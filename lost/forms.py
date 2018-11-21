from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'type_of_object', 'description', 'location_found', 'pickup_details', 'posted_at', 'status', 'image',  ]
