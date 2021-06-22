from django.db import models
from django.contrib.auth.models import User

class Cloths(models.Model):
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) # defaulf=1 means
	cloth_name = models.CharField(max_length=50)
	wash_price = models.FloatField()
	category = models.CharField(max_length=30)
	date_add = models.DateTimeField(auto_now_add=True)
	# add_date = models.DateField(null=True, blank=True)


	def __str__(self):
		return f"{self.cloth_name}"

