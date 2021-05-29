from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from .models import Person, PushUps

class DateInput(forms.DateInput):
    input_type = 'date'

class pushUpForm(forms.ModelForm):
    numOfPushUps = forms.IntegerField(label='Number of pushups:', min_value=1)
    class Meta:
        model = PushUps
        fields = '__all__'
        widgets = {
            'date': DateInput(),
            'user': forms.HiddenInput()
        }

        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "You can't add more pushups the same day",
            }
        }