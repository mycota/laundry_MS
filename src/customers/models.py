from django.db import models
from django.contrib.auth.models import User


class Customers(models.Model):
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) # defaulf=1 means
	cust_name = models.CharField(max_length=70)
	cust_phone = models.CharField(max_length=10, unique=True)
	cust_email = models.CharField(max_length=100, unique=True)
	cust_address = models.TextField(max_length=225)	
	cust_gender = models.CharField(max_length=6)
	balance = models.FloatField(null=True, blank=True)
	update = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f"{self.cust_name} - {self.cust_phone}"






	
		