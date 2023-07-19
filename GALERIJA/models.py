from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now



class Gallery(models.Model):
    title=models.CharField(max_length=255)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    dateTime=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.author) +  " Painting Title: " + self.title
    
    def get_absolute_url(self):
        return reverse('paintingslist')
    
    

    


