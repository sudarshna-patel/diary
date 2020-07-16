from django.db import models

# Create your models here.
class Entry(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return "Entry #{}".format(self.id)