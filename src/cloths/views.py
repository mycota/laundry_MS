from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Cloths
from orders.models import OrderDetails
from .forms import ClothForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from laundry.views import logs
from datetime import date


# Create your views here.

def add_cloths(request):
	usertype = request.user.employeeinfo.role
	active = request.user.is_active

	if ((usertype == 'Manager' or usertype == 'Admin') and active == True):
		# print('Am here', usertype, active)
		cloth_form = ClothForm()
		context = {'cloth_form': cloth_form, 'title': 'Add Cloth'}
		if request.method == 'POST':
			cloth_form = ClothForm(request.POST)
			if cloth_form.is_valid():
					cloth_form.save()
					cloth_name = cloth_form.cleaned_data.get('cloth_name')
					messages.success(request, f"You've added {cloth_name}.....")
					logs(request, 'Normal', 'Added new cloth ...'+cloth_name)
					return redirect('view_cloths')
		else:
			logs(request, 'Normal', 'Adding a new cloth....')
			return render(request, 'cloths/add_cloths.html', context) # as register.html

			
			# print('What is going on here ......')
	else:
		# print('Sorry you Dont have access here ..')
		logs(request, 'Violation', 'Tried to access the add new cloth page')
		messages.warning(request, f"Sorry you dont have access to that page ..")
		return redirect('denied')

def update_cloths(request, clothid):
	usertype = request.user.employeeinfo.role
	active = request.user.is_active
	obj = get_object_or_404(Cloths, id=clothid)
	form_cloth = ClothForm(instance=obj)
	if ((usertype == 'Manager' or usertype == 'Admin') and active == True):
		if request.method == 'POST':
			form_cloth = ClothForm(request.POST, instance=obj)
			if form_cloth.is_valid():
				form_cloth.save()
				cloth_name = form_cloth.cleaned_data.get('cloth_name')
				messages.success(request, f"You've updated cloth ....")
				logs(request, 'Normal', 'Updated a cloth '+cloth_name)
				return redirect('view_cloths')

				# Machines.objects.filter(id=macid).update(user=request.user, mac_name=mac_name, model=mac_model,
			 	# 	manufactural=manu, price=price, date_bought=date, image=mimage)
				# insert.save()
				# Orders.objects.filter(transid=trans).update(order_status='Collected')
		else:
			logs(request, 'Normal', 'Updating a cloth')
			return render(request, 'cloths/update_cloth.html', {'title': 'Update Cloth', 'form_cloth': form_cloth})

	else:
		logs(request, 'Violation', 'Tried to access update cloth page')
		messages.warning(request, f"Sorry you dont have access to that page ..")
		return redirect('denied')

def cloth_details(request, clothid):
	usertype = request.user.employeeinfo.role
	active = request.user.is_active

	if ((usertype == 'Manager' or usertype == 'Admin') and active == True):
		cloth = get_object_or_404(Cloths, id=clothid)
		cloth_name = cloth.cloth_name
		allcloths = OrderDetails.objects.all()
		lastdate = OrderDetails.objects.filter(cloth_name=cloth_name).last()
		total = 0
		count = 0
		for clth in allcloths:
			if clth.cloth_name == cloth_name:
			  	total += clth.sub_total
			  	count += 1
		cloth_form = ClothForm(instance=cloth)
		if lastdate is None:
			context = {'cloth_form': cloth_form, 'title': 'Add Cloth', 'count': count, 'total': total, 'lastdate': 'None'}
		else:
			context = {'cloth_form': cloth_form, 'title': 'Add Cloth', 'count': count, 'total': total, 'lastdate': lastdate.timestamp}

		if request.method == 'POST':
			cloth_form = ClothForm(request.POST)
			if cloth_form.is_valid():
				cloth_form.save()
				cloth_name = cloth_form.cleaned_data.get('cloth_name')
				messages.success(request, f"You've added {cloth_name}.....")
				logs(request, 'Normal', 'Updating a cloth')

				return redirect('view_cloths')
		else:
			logs(request, 'Normal', 'view cloth detail')
			return render(request, 'cloths/cloth_details.html', context) # as register.html
	else:
		logs(request, 'Violation', 'Tried to access the cloth detail page')
		messages.warning(request, f"Sorry you dont have access to that page ..")
		return redirect('denied')


def view_cloths(request):
	cloths = Cloths.objects.all()
	usertype = request.user.employeeinfo.role
	active = request.user.is_active
	ordering = ['-timestamp']
	paginate_by = 2
	context = {'cloths': cloths, 'title': 'All cloths'}
	if usertype == 'Manager' or usertype == 'Admin':
		logs(request, 'Normal', 'View all cloths')
		return render(request, 'cloths/view_cloths.html', context)
	else:
		logs(request, 'Normal', 'View all cloths')
		return render(request, 'cloths/view_cloths.html', context)

@login_required
def remove_cloth(request, clothid):
	cloths = Cloths.objects.all()
	Cloths.objects.filter(id=clothid).delete()

	usertype = request.user.employeeinfo.role
	active = request.user.is_active
	ordering = ['-timestamp']
	paginate_by = 2
	context = {'cloths': cloths, 'title': 'All cloths'}
	if usertype == 'Manager' or usertype == 'Admin':
		logs(request, 'Normal', 'View all cloths after deleting a cloth')
		messages.success(request, f"Cloth deleted ...")
		return render(request, 'cloths/view_cloths.html', context)
	else:
		logs(request, 'Normal', 'View all cloths after deleting a cloth')
		messages.success(request, f"Cloth deleted ...")
		return render(request, 'cloths/view_cloths.html', context)