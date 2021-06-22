from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Machines(models.Model):
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) # defaulf=1 means
	machine_name = models.CharField(max_length=30, blank=True)
	model = models.CharField(max_length=70, blank=True)
	manufacturer = models.CharField(max_length=70, blank=True)
	price = models.FloatField(null=True)
	date_bought = models.DateField(null=True, blank=True)
	image = models.ImageField(upload_to='wmachines')
	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f"{self.manufacturer}.{self.model} washing machine"

	def save(self, **kwargs):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 200 or img.width > 200:
			output = (200,200)
			img.thumbnail(output)
			img.save(self.image.path)