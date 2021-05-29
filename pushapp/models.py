
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    age = IntegerRangeField(min_value=1)

    def __str__(self):
        return str(self.user)



class PushUps(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    numOfPushUps = IntegerRangeField(min_value=1)
    date = models.DateTimeField('date')

    class Meta:
        unique_together = ['date', 'user']


