from django import forms
from django.forms import ModelForm
from dashboardbuku.models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["review"]
        # widgets = {
        #     "review":forms.Textarea()
        # }