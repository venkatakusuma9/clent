from django.db import models

# Create your models here.
class Member(models.Model):
    name=models.CharField(max_length=250)
    num=models.IntegerField()
    marks=models.IntegerField(null=True)
    def __str__(self):
        return f"{self.name}-{self.num}"
