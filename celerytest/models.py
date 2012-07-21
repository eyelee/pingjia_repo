from django.db import models

class Counter(models.Model):
    seq = models.BigIntegerField()
    #date =models.DateTimeField('date inserted')
   
    def __unicode__(self):
        return self.seq