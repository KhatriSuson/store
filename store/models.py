from django.db import models



# Create your models here

class product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    
    description = models.CharField(max_length=200)
    images = models.ImageField(upload_to='images/product')



class catagory(models.Model):
    name = models.CharField(max_length=50)




class customer(models.Model):
    email = models.CharField(max_length=50)
    password = models.IntegerField(default=0)
    

  

    
  



