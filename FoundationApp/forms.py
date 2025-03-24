from django import forms

from FoundationApp.models import ImageModel, EventModel


class ImageModelForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'

class EventModelForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ['image']