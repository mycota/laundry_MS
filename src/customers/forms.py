from django import forms
from django.contrib.auth.models import User
from .models import Customers


class AddCustomerForm(forms.ModelForm):
	gend = (('Male', 'Male'), ('Famale', 'Famale'),)

	cust_name = forms.CharField(max_length=70)
	cust_phone = forms.CharField(max_length=10)
	cust_email = forms.CharField(max_length=100)
	cust_address = forms.CharField(widget=forms.Textarea,max_length=225)	
	cust_gender = forms.ChoiceField(choices=gend)
	# balance = forms.FloatField()

	class Meta:
		model = Customers
		fields = ['cust_name', 'cust_phone', 'cust_email', 'cust_address', 'cust_gender']


class UpdateCustomerForm(forms.ModelForm):
	gend = (('Male', 'Male'), ('Famale', 'Famale'),)

	cust_name = forms.CharField(max_length=70)
	cust_phone = forms.CharField(max_length=10)
	cust_email = forms.CharField(max_length=100)
	cust_address = forms.CharField(widget=forms.Textarea,max_length=225)	
	cust_gender = forms.ChoiceField(choices=gend)
	# balance = forms.FloatField()

	class Meta:
		model = Customers
		fields = ['cust_name', 'cust_phone', 'cust_email', 'cust_address', 'cust_gender']