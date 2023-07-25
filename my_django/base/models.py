from django.db import models

# Create your models here.
class Person(models.Model):
    '''first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)'''

    SHIRT_SIZE=[
        ("S","Small"),
        ("M","Medium"),
        ("L","Large"),
    ]
    name = models.CharField(max_length=60,default="somethin")
    shirt_size = models.CharField(max_length=1,choices=SHIRT_SIZE,default="NA")
    def __str__(self) :
        return self.name
    
    def identifier(self):
        import datetime

        if self.shirt_size =="L":
            return self.name
        else:
            return "Not large"
        
    @property
    def full_size(self):
        return f"Name is {self.name} "
    


    

class Musician(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    instrument=models.CharField(max_length=30)

class Albums(models.Model):
    artist =models.ForeignKey(Musician, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    release_date=models.DateField()
    num_stars=models.IntegerField()

class Runner(models.Model):
    MedalType=models.TextChoices("MedalType","Gold Silver Bronze")
    name=models.CharField(max_length=60)
    medal=models.CharField(blank=True,choices=MedalType.choices,max_length=10,default="none")

class Fruit(models.Model):
    name=models.CharField(max_length=30,primary_key=True)

    def __str__(self) :
        return self.name
