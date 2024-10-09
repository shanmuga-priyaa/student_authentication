from django.db import models

class course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.FloatField(max_length=100)
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    