from django.db import models
from django.contrib.auth.models import User

class TotalValue(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'totalvalue', null= True)
    total = models.IntegerField(default=0)

    def __str__(self):
        return str(self.total)

class Income(models.Model):
    relation = models.ForeignKey(TotalValue, on_delete= models.CASCADE, null= True)
    name = models.CharField(max_length=200)
    amount = models.IntegerField()
    def __str__(self):
        return f'{self.name} - {self.amount}'

class Expenses(models.Model):
    relation = models.ForeignKey(TotalValue, on_delete = models.CASCADE, null= True)
    name = models.CharField(max_length= 200)
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.amount}'