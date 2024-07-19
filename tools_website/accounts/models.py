from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class tools(models.Model):
    price = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to="images/")
    description = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} {self.description} {self.price}"
        
        
        
class contactus(models.Model):
    Username = models.CharField(max_length=255)
    Email = models.CharField(max_length=150)
    Your_trc20_wallet_address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.Username} {self.Email} {self.Your_trc20_wallet_address}"



class nameofuser(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True)
    def __str__(self):
        return f'{self.users}{self.amount}'


        
class Meta:
    ordering = ["created"]
    indexes = [models.Index(fields=["created"]),]


    
    
    
    
