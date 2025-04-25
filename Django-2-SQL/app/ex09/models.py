from django.db import models

# Create your models here.
class Planets(models.Model):
    name=models.CharField(max_length=64, unique=True, null=False)
    climate=models.CharField(max_length=64, blank=True, null=True)
    diameter=models.IntegerField(null=True, blank=True)
    orbital_period=models.IntegerField(null=True, blank=True)
    population=models.BigIntegerField(null=True, blank=True)
    rotation_period=models.IntegerField(null=True, blank=True)
    surface_water=models.FloatField(null=True, blank=True)
    terrain=models.CharField(max_length=64, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class People(models.Model):
    name=models.CharField(max_length=64, null=False)
    birth_year=models.CharField(max_length=32, blank=True, null=True)
    gender=models.CharField(max_length=32, blank=True, null=True)
    eye_color=models.CharField(max_length=32, blank=True, null=True)
    hair_color=models.CharField(max_length=32, blank=True, null=True)
    height=models.IntegerField(null=True, blank=True)
    mass=models.FloatField(null=True, blank=True)
    homeworld = models.ForeignKey(
        Planets,
        to_field='name',
        db_column='homeworld',
        on_delete=models.SET_NULL,
        related_name='residents',
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        