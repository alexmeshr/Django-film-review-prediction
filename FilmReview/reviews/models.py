from django.db import models
from django.forms import ModelForm
from django import forms


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    sentiment = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['sentiment', 'date_of_creation', 'rating']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "What's your name?"}),
            'description': forms.Textarea(attrs={'placeholder': "Your review here...", 'cols': 200, 'rows': 5}),
        }
