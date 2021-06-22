from django import forms
from datetimepicker.widgets import DateTimePicker
from django.contrib.auth.models import User
from .models import Machines




class InputDate(forms.DateInput):
	input_type = 'date'

class UpdateMachines(forms.ModelForm):
	date_bought = forms.DateField(widget=InputDate)

	class Meta:
		model = Machines
		fields = ['machine_name','model','manufacturer', 'price','date_bought','image']

		# date_bought = forms.DateField(
  #       widget=forms.DateInput(format='%m/%d/%Y'),
  #       input_formats=('%m/%d/%Y', )
  #       )