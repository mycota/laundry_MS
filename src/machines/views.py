from django.shortcuts import render, redirect, get_object_or_404
from .models import Machines
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UpdateMachines
from laundry.views import logs


def add_machine(request):
	usertype = request.user.employeeinfo.role
	active = request.user.is_active

	if ((usertype == 'Manager' or usertype == 'Admin') and active == True):
		if request.method == 'POST':
			mac_name = request.POST['mac_name']
			mac_model = request.POST['mac_model']
			manu = request.POST['manu']
			price = request.POST['price']
			date = request.POST['date']
			mimage = request.FILES['mimage']

			insert = Machines(user=request.user, mac_name=mac_name, model=mac_model,
			 manufactural=manu, price=price, date_bought=date, image=mimage)
			insert.save()
			logs(request, 'Normal', 'Added a new washing machine '+mac_name)
			messages.success(request, f"You've added new machine ....")
			return redirect('view_mac')
			
		else:
			logs(request, 'Normal', 'Adding a new washing machine ')
			return render(request, 'machines/add_machine.html', {'title': 'Add Washing Machine'})

	else:
		logs(request, 'Violation', 'Tried to access add new washing machine')
		messages.warning(request, f"Sorry you dont have access to that page ..")
		return redirect('denied')

def view_machines(request):
	mac = Machines.objects.all()
	context = {'title': 'Wash Machines', 'mac': mac}
	logs(request, 'Normal', 'View all washing machines record.')
	return render(request, 'machines/view_wmachines.html', context)


def update_machine(request, macid):
	usertype = request.user.employeeinfo.role
	active = request.user.is_active
	obj = get_object_or_404(Machines, id=macid)
	form_mac = UpdateMachines(instance=obj)
	if ((usertype == 'Manager' or usertype == 'Admin') and active == True):
		if request.method == 'POST':
			form_mac = UpdateMachines(request.POST, request.FILES, instance=obj)
			if form_mac.is_valid():
				form_mac.save()
				messages.success(request, f"You've updated machine ....")
				logs(request, 'Normal', 'Updating a washing machine ')
				return redirect('view_mac')
		else:
			logs(request, 'Normal', 'Updating washing machine')
			return render(request, 'machines/update_mac.html', {'title': 'Update Washing Machine', 'form_mac': form_mac})

	else:
		logs(request, 'Violation', 'Tried to access update washing machine page')
		messages.warning(request, f"Sorry you dont have access to that page ..")
		return redirect('denied')


def mac_details(request, macid):
	usertype = request.user.employeeinfo.role
	active = request.user.is_active
	if ((usertype == 'Manager' or usertype == 'Admin') and active == True):
		obj = get_object_or_404(Machines, id=macid)
		
		context = {'title': 'Machine Details', 'obj': obj}
		logs(request, 'Normal', 'View a washing machine detail page ')
		return render(request, 'machines/view_mac_details.html', context)

	else:
		# print('Sorry you Dont have access here5 ..')
		logs(request, 'Violation', 'Tried to access all washing machine page')
		messages.warning(request, f"Sorry you dont have access to that page ..")
		return redirect('denied')