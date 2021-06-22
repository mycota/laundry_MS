from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import EmployeeInfo
# from .forms import AddEmployeeInfo

@receiver(post_save, sender=User)
def create_employeeinfo(sender, instance, created, **kwargs):
	if created:
		EmployeeInfo.objects.create(user=instance)


@receiver(post_save, sender=User)
def add_employeeinfo(sender, instance, **kwargs):
	instance.employeeinfo.save()
	