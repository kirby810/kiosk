from django.db import models


# Customer 모델
class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    phone_num = models.CharField(max_length=15, unique=True)
    point = models.IntegerField(default=0)




# Menu 모델
class Menu(models.Model):
    menu_name = models.CharField(max_length=255)
    menu_price = models.IntegerField()
    menu_category = models.CharField(max_length=50)

    def __str__(self):
        return self.menu_name


# Order 모델
class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)

   
