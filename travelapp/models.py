from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='pics/')  
    desc = models.TextField()

    def __str__(self):
        return self.name
    
class TeamMember(models.Model):
    tname = models.CharField(max_length=255)
    timg = models.ImageField(upload_to='pics/')  
    tdesc = models.TextField()
    tdesig = models.CharField(max_length=50)

    def __str__(self):
        return self.tname

