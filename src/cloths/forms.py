from django import forms
from django.contrib.auth.models import User
from .models import Cloths

# class InputDate(forms.DateInput):
# 	input_type = 'date'


class ClothForm(forms.ModelForm):
	cat = (('Men', 'Men'), ('Famale', 'Famale'), ('Kids', 'Kids'),)

	category = forms.ChoiceField(choices=cat)
	# add_date = forms.DateField(widget=InputDate)


	class Meta:
		model = Cloths
		fields = ['cloth_name', 'wash_price', 'category']


		
		# # print('from validations: ',title) # go ahead 
		# qs = BlogPost.objects.filter(title__iexact = title) # case insentitive # to see if there is any values of that
		# if instance is not None:
		# 	qs = qs.exclude(pk=instance.pk) # same as id=instance.id
		# if qs.exists():
		# 	raise forms.ValidationError("This title has already been use, please use a different one")
