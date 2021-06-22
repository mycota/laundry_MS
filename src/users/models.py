from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class EmployeeInfo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE) # defaulf=1 means
	role = models.CharField(max_length=30, blank=True)
	phone = models.CharField(null=True, max_length=10, blank=True, unique=True)
	address = models.TextField(max_length=225, blank=True)
	gender = models.CharField(max_length=6, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	marrig_Status = models.CharField(max_length=10, blank=True)
	department = models.CharField(max_length=20, blank=True)
	salary = models.FloatField(null=True, blank=True)
	employment_Date = models.DateField(null=True, blank=True)
	image = models.ImageField(upload_to='emply_pics')

	def __str__(self):
		return f"{self.user.username}'s Info"

	def save(self, **kwargs):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 200 or img.width > 200:
			output = (200,200)
			img.thumbnail(output)
			img.save(self.image.path)


class Logs(models.Model):
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) # defaulf=1 means
	ip_addr = models.CharField(max_length=70)
	event_type = models.CharField(max_length=20)
	event = models.TextField(max_length=2000)
	event_time = models.DateTimeField(auto_now_add=True)

