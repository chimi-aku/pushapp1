from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.core.exceptions import ValidationError
from .models import Person, PushUps

from django.db.models import Deferrable, UniqueConstraint

class DateInput(forms.DateInput):
    input_type = 'date'

class pushUpForm(forms.ModelForm):
    numOfPushUps = forms.IntegerField(label='Number of pushups:', min_value=1)
    class Meta:
        model = PushUps
        #exclude = ['user']
        fields = '__all__'
        widgets = {
            'date': DateInput(),
            'user': forms.HiddenInput()
        }

    # def clean(self):
    #
    #     try:
    #         super(forms.ModelForm, self).clean()
    #     except forms.ValidationError:
    #         raise forms.ValidationError("You can't add more pushups the same day")

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     print( '#####################################', self.user)
    #     cleaned_data = self.cleaned_data
    #     if PushUps.objects.filter(date=cleaned_data['date'],
    #                                    user=self.user).exists():
    #         raise ValidationError(
    #                 'Solution with this Name already exists for this problem')
    #
    #     # Always return cleaned_data
    #     return cleaned_data

# ValidationError wyjątek do wyłapania