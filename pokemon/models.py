from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(verbose_name=u'Nombre del pokemon', max_length=250)

    class Meta:
        unique_together = ('name',)
        ordering = ('id',)