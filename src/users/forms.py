from django import forms
from datetimepicker.widgets import DateTimePicker
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import EmployeeInfo


class InputDate(forms.DateInput):
	input_type = 'date'

# for admin to create new user
class AddUserForm	(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=70)
	
	# is_staff = forms.BooleanField() #'is_staff',
	# is_active = forms.BooleanField(required=False) 
	# is_superuser = forms.BooleanField(required=False)

	class Meta:
		model = User
		fields = ['first_name','last_name','email', 'username', 'password1', 'password2']
# for user profile update and admin to update a user info
class UpdateUser(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','email']
# for user profile update and adding new info after the user is created
class UpdateEmployeeInfo(forms.ModelForm):
	# users = User.objects.get(pk=user_id)
	# def gtUsers(users):
	# 	for usr in users:
	# 		return usr
	# usr = ((gtUsers(users),gtUsers(users)),)
	roles = (('Front Desk', 'Front Desk'),('Supervisor', 'Supervisor'),('Manager', 'Manager'),('Admin', 'Admin'),)
	gend = (('Male', 'Male'), ('Famale', 'Famale'), )
	mstu = (('Single', 'Single'), ('Married', 'Married'), )
	dept = (('Sales', 'Sales'),('Accouts', 'Accouts'),('IT', 'IT'), )

	# user = forms.ChoiceField(choices=usr)
	role = forms.ChoiceField(choices=roles)
	phone = forms.CharField(max_length=10)
	address = forms.CharField(widget=forms.Textarea,max_length=225)
	gender = forms.ChoiceField(choices=gend)
	birth_date = forms.DateField(widget=InputDate)
	marrig_Status = forms.ChoiceField(choices=mstu)
	department = forms.ChoiceField(choices=dept)
	# salary = forms.FloatField()
	employment_Date = forms.DateField(widget=InputDate)
	image = forms.ImageField(required=False)

	
	class Meta:
		model = EmployeeInfo
		fields = ['role', 'phone', 'address', 'gender', 'birth_date', 'marrig_Status', 'department', 'employment_Date', 'image']

	def check_age(self, *args, **kwargs):
		instance = self.instance
		birth_date = self.cleaned_data.get("birth_date")
		today = date.today()
		age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

		if age <= 17:
			raise forms.ValidationError("Sorry you cannot employed a person with age lower than 18 years.")
		if age >= 80:
			raise forms.ValidationError("Sorry you cannot employed a person with age more than 80 years")
		return birth_date

# for the admin to update a user info
class UpdateEmployeeInfoByAdmin(forms.ModelForm):
	# users = User.objects.get(pk=user_id)
	# def gtUsers(users):
	# 	for usr in users:
	# 		return usr
	# usr = ((gtUsers(users),gtUsers(users)),)
	roles = (('Front Desk', 'Front Desk'),('Supervisor', 'Supervisor'),('Manager', 'Manager'),('Admin', 'Admin'),)
	gend = (('Male', 'Male'), ('Famale', 'Famale'), )
	mstu = (('Single', 'Single'), ('Married', 'Married'), )
	dept = (('Sales', 'Sales'),('Accouts', 'Accouts'),('IT', 'IT'), )

	# user = forms.ChoiceField(choices=usr)
	role = forms.ChoiceField(choices=roles)
	phone = forms.CharField(max_length=10)
	address = forms.CharField(widget=forms.Textarea,max_length=225)
	gender = forms.ChoiceField(choices=gend)
	birth_date = forms.DateField(widget=InputDate)
	marrig_Status = forms.ChoiceField(choices=mstu)
	department = forms.ChoiceField(choices=dept)
	# salary = forms.FloatField()
	employment_Date = forms.DateField(widget=InputDate)
	image = forms.ImageField(required=False)

	
	class Meta:
		model = EmployeeInfo
		fields = ['role', 'phone', 'address', 'gender', 'birth_date', 'marrig_Status', 'department', 'employment_Date', 'image']

  # employment_Date = forms.DateField(
  #       widget=forms.DateInput(format='%m/%d/%Y'),
  #       input_formats=('%m/%d/%Y', )
  #       )
