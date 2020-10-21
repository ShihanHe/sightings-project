from django.db import models

class Squirrel(models.Model):
    Latitude = models.FloatField( )

    Longitude = models.FloatField( )

    Unique_Squirrel_ID = models.CharField(
        max_length=100,
        unique=True,
    )

    Shift = models.CharField(
        max_length=100,
    )

    Date = models.DateField(
        max_length=100,
        blank=True,
    )

    Age = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    Primary_Fur_Color = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    Location = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    Specific_Location = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )       

    Running = models.BooleanField(blank=True)     

    Chasing = models.BooleanField(blank=True)  
    
    Climbing = models.BooleanField(blank=True)  

    Eating = models.BooleanField(blank=True)

    Foraging = models.BooleanField(blank=True)

    Other_Activitites = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    Kuks = models.BooleanField(blank=True)

    Quaas = models.BooleanField(blank=True)

    Moans = models.BooleanField(blank=True)

    Tail_flags = models.BooleanField(blank=True)

    Tail_twitches = models.BooleanField(blank=True)

    Approaches = models.BooleanField(blank=True)

    Indifferent = models.BooleanField(blank=True)

    Runs_from = models.BooleanField(blank=True)
    
    def __str__(self):
        return self.Unique_Squirrel_ID
