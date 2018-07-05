from django import forms
from .models import Lunch

class LunchForm(forms.ModelForm):
    class Meta:
        model = Lunch
        exclude = ['team']
        widgets = {'yelp_id' : forms.HiddenInput()}

    def save(self, *args, **kwargs):
        """
        This method saves changes to the linked user model.
        """
        self.instance.team = kwargs.pop('team')
        return super(LunchForm, self).save(*args, **kwargs)