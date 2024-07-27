from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class tools(models.Model):
    price = models.IntegerField(null=True)
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to="images/")
    description = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} {self.description} {self.price}"
        
        
        
class contactus(models.Model):
    Username = models.CharField(max_length=255)
    Amount_Transfered = models.CharField(max_length=255, null=True)
    Your_trc20_wallet_address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.Username}{self.Your_trc20_wallet_address}"


class order_emails(models.Model):
    Email = models.EmailField(null=True, max_length=200)
    
    def __str__(self):
        return f'{self.Email}'

      
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_detals = models.IntegerField(default=0)
    msg = models.TextField(max_length=500, default='Hello!! welcome, Place order and get your tool delivered to email')
    def __str__(self):
        return f'{self.user.username} {self.msg}'    


     




        


    
    
    
    
