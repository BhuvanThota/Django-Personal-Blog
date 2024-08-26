from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "username": "Your Name",
            "user_email": "Email",
        }

    rating = forms.IntegerField(min_value=1, max_value=5)


