from django.db import models
import uuid
from django.contrib.auth.models import User
from customers.models import Customers



class Orders(models.Model):
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
	customer = models.ForeignKey(Customers, default=1, null=True, on_delete=models.SET_NULL)
	order_date = models.DateTimeField(auto_now_add=True)
	return_date = models.DateField(auto_now_add=False, blank=True, null=True)
	order_status = models.CharField(max_length=15)
	total_item = models.IntegerField()
	total = models.FloatField()
	transid = models.CharField(max_length=100, unique=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.customer}"


class OrderDetails(models.Model):
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
	transid = models.CharField(max_length=100, null=True)
	cloth_name = models.CharField(max_length=50)
	quantity = models.IntegerField()
	unit_price = models.FloatField()
	sub_total = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f"{self.transid}"

