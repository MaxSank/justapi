from django.db import models


class Record(models.Model):
    name = models.CharField('Name', max_length=250)
    time = models.DateTimeField('Time')
    number = models.FloatField('Number')
    text = models.TextField('Text', max_length=500)
    list = models.TextField('List', max_length=500)

    def __str__(self):
        return self.name
