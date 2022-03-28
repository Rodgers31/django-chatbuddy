from django.db import models

# Create your models here.

class Room(models.Model):
 #host = 
 #topic = 
  name = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)
  #participants = models

 # Auto_now takes a nsapshot evertime we save this instance, while auto_now_add only does it on the initial will never change event if you change multiple times
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.name