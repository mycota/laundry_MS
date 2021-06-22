from django.db import models
from django.contrib.auth.models import User
from customers.models import Customers
from orders.models import Orders

# Create your models here.

class Payments(models.Model):
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
	customer = models.ForeignKey(Customers, default=1, null=True, on_delete=models.SET_NULL)
	order_id = models.ForeignKey(Orders, default=1, null=True, on_delete=models.SET_NULL)
	payment_id = models.CharField(max_length=100, unique=True)
	transactid = models.CharField(max_length=20, unique=True)
	amount = models.FloatField()
	pay_mthd = models.CharField(max_length=5, null=True)
	trans_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f"{self.customer.cust_name}'s Payments"

