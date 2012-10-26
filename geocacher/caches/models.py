from django.db import models
from django.contrib.auth.models import User
from geopy import distance
from django.forms import ModelForm


SIZE_CHOICES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
)

class Cache(models.Model):
    created_by =   models.ForeignKey(User, related_name='created_caches')
    title =        models.CharField(max_length = 100)
    lat =          models.FloatField()
    lon =          models.FloatField()
    description =  models.TextField(null=True, blank=True)
    size =         models.CharField(max_length=6, choices=SIZE_CHOICES)


class Log(models.Model):
    cache =   models.ForeignKey(Cache, related_name='logs')
    time =    models.DateTimeField(auto_now_add=True)
    found =   models.BooleanField()
    message = models.TextField(null=True, blank=True)
    user =    models.ForeignKey(User, related_name='logs')


# ------------------------------ FORMS --------------------------------- #    

class CacheForm(ModelForm):
    class Meta:
        model = Cache
        exclude = ('created_by',)

class LogForm(ModelForm):
    class Meta:
        model = Log
        exclude = ('user',)

