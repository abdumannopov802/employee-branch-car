from django.db import models

class AutoBranch(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    branch = models.ForeignKey(AutoBranch, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Automobile(models.Model):
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    branch = models.ForeignKey(AutoBranch, on_delete=models.CASCADE)

    def __str__(self):
        return self.model