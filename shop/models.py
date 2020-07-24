from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50,blank=True)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField(blank=True)
    #available = models.BooleanField(default=True)
    pub_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='shop/images', blank=True)

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    query = models.TextField(max_length=500, default="")


    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=90)
    instructions = models.TextField(max_length=5000,default=True)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")



class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.TextField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."