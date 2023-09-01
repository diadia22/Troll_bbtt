from django.db import models

# Create your models here.



#Unnamed: 0,puuid,championId,championLevel,championPoints
class Mastery(models.Model):
    id = models.AutoField(primary_key=True)
    puuid = models.CharField(max_length=78)
    championId = models.IntegerField()
    championLevel = models.IntegerField()
    championPoints = models.IntegerField()

