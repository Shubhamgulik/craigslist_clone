from django.db import models

# Create your models here.

class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.search)

    class Meta:
        verbose_name_plural = 'Searches'

#end here
#anaconda-client==1.7.2
#anaconda-navigator==1.9.12
#anaconda-project==0.8.3