from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# class Employee(models.Model):
# 	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) # defaulf=1 means
# 	empFName = models.CharField(max_length=50)
# 	empLName = models.CharField(max_length=70)
# 	empPhone = models.CharField(max_length=10)
# 	empEmail = models.EmailField()
# 	empAddress = models.TextField(max_length=50)
# 	empGender = models.CharField(max_length=6)
# 	empBod = models.DateField(null=True)
# 	empMarrigStatus = models.CharField(max_length=10)
# 	empDept = models.CharField(max_length=20)
# 	empSalary = models.FloatField()
# 	empDateEmpl = models.DateField(null=True)
# 	EmpTimestamp = models.DateTimeField(auto_now_add=True)

# 	def __str__(self):
# 		return self.empFName


# emply_1 = Employee(user=user, empFName='Mohammed', empLName='Adamu', empPhone='9537764955', empEmail='adamuips@gmail.com', empAddress='Box 1372 Sunyani', empGender='Male', empBod='1998-02-12', empMarrigStatus='Single', empDept='IT', empSalary=12900, empDateEmpl='2011-08-12')
# emply_2 = Employee(user=user, empFName='Pery', empLName='Tei', empPhone='0246757454', empEmail='pery@gmail.com', empAddress='Box 121 Mim', empGender='Male', empBod='1985-06-30', empMarrigStatus='Married', empDept='Accounts', empSalary=10500, empDateEmpl='2012-12-02')