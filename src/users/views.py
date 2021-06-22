from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
from django.db.models import Count
from .models import EmployeeInfo
from .forms import (AddUserForm, UpdateEmployeeInfo,
 					UpdateUser, UpdateEmployeeInfoByAdmin
 )

@property
def empdatepast(self):
	return date.today() > self.date


@login_required
def add_user(request):
	usertype = request.user.employeeinfo.role
	active = request.user.is_active

	if ((usertype == 'Manager' or usertype == 'Admin') and active == True):
		# print('Am here', usertype, active)
		usr_form = AddUserForm()
		context = {'usr_form': usr_form, 'title': 'Add User'}
		if request.method == 'POST':
			usr_form = AddUserForm(request.POST)
			if usr_form.is_valid():
				usr_form.save()
				username = usr_form.cleaned_data.get('username')
				usrid = get_object_or_404(User, username=username)
				usrid = usrid.id
				messages.success(request, f"You've created account for {username}...")
				return redirect('add_emp_info', usr=usrid)
		else:
			
			print('What is going on here ......')
		return render(request, 'users/add_user.html', context) # as register.html
	else:
		# print('Sorry you Dont have access here ..')
		messages.warning(request, f"Sorry you dont have access to that page ..")
		return redirect('denied')

@login_required
def add_emp_info(request, usr):
	usertype = request.user.employeeinfo.role
	active = request.user.is_active

	if ((usertype == 'Manager' or usertype == 'Admin') and active == True):
		obj2 = get_object_or_404(EmployeeInfo, user=usr)
		if request.method == 'POST':
			info_form = UpdateEmployeeInfo(request.POST, request.FILES, instance=obj2)
			if info_form.is_valid():

				birthdate = info_form.cleaned_data.get("birth_date")
				empldate = info_form.cleaned_data.get("employment_Date")

				today = date.today()

				age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

				if age <= 17:
					# print("Sorry you cannot employed a person with age lower than 18 years")
					messages.warning(request, f"Sorry you cannot employed a person with age lower than 18 years.")
					return redirect('add_emp_info', usr=usr)
					
				elif age >=80:
					# print("Sorry you cannot employed a person with age lower than 18 years in India")
					messages.warning(request, f"Sorry you cannot employed a person with age more than 80 years")
					return redirect('add_emp_info', usr=usr)

				elif date.today() < empldate:
					# print("See this -------------", date.today())
					messages.warning(request, f"Sorry employment date cannot be more than today's date")
					return redirect('add_emp_info', usr=usr)	
				
				else:
					info_form.save()
					username = get_object_or_404(User, id=usr)
					username = username.username
					messages.success(request, f"You've added info for {username}...")
					return redirect('emply-view')
		else:
			info_form = UpdateEmployeeInfo(instance=obj2)
			context = {'info_form': info_form, 'title': 'Add User Info'}

		return render(request, 'users/add_emp_info.html', context) # as register.html
	else:
		# print('Sorry you Dont have access here2 ..')
		messages.warning(request, f"Sorry you dont have access to that page ..")
		return redirect('denied')

@login_required
def employee_view(request):
	usertype = request.user.employeeinfo.role
	active = request.user.is_active
	if ((usertype == 'Manager' or usertype == 'Admin') and active == True):
		count = User.objects.annotate(Count('id'))
		allusers = User.objects.all().order_by('date_joined')
		# print(allusers)
		context = {'empmodel': allusers, 'title':'All users', 'count':count}
		return render(request, 'users/emply_view.html', context)
	else:
		# print('Sorry you Dont have access here3 ..')
		messages.warning(request, f"Sorry you dont have access to that page ..")
		return redirect('denied')

@login_required #user info update by admin 
def user_info_update(request, usr):
	usertype = request.user.employeeinfo.role
	active = request.user.is_active
	if ((usertype == 'Manager' or usertype == 'Admin') and active == True):
		obj1 = get_object_or_404(User, id=usr)
		obj2 = get_object_or_404(EmployeeInfo, user=usr)
		if request.method == 'POST':
			usr_form = UpdateUser(request.POST, instance=obj1)
			info_form = UpdateEmployeeInfoByAdmin(request.POST, request.FILES, instance=obj2)
			if usr_form.is_valid() and info_form.is_valid():

				birthdate = info_form.cleaned_data.get("birth_date")
				empldate = info_form.cleaned_data.get("employment_Date")

				today = date.today()

				age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

				if age <= 17:
					# print("Sorry you cannot employed a person with age lower than 18 years")
					messages.warning(request, f"Sorry date of birth is lower than 18 years.")
					return redirect('add_emp_info', usr=usr)
					
				elif age >=80:
					# print("Sorry you cannot employed a person with age lower than 18 years in India")
					messages.warning(request, f"Sorry date of birth is more than 80 years")
					return redirect('add_emp_info', usr=usr)

				elif date.today() < empldate:
					# print("See this -------------", date.today())
					messages.warning(request, f"Sorry employment date cannot be more than today's date")
					return redirect('add_emp_info', usr=usr)
				else:	
					usr_form.save()
					info_form.save() #00mohamed
					username = obj1.username
					messages.success(request, f"You've added info for {username}...")
					return redirect('emply-view')
		else:
			usr_form = UpdateUser(instance=obj1)
			info_form = UpdateEmployeeInfoByAdmin(instance=obj2)
			context = {'usr_form': usr_form, 'info_form': info_form, 'title': 'Update Info', 'obj1': obj1, 'obj2': obj2}

		return render(request, 'users/user_info_update.html', context) # as register.html
	else:
		# print('Sorry you Dont have access here4 ..')
		messages.warning(request, f"Sorry you dont have access to that page ..")
		return redirect('denied')

@login_required # profile upate by a login user
def user_profile(request):
	usertype = request.user.employeeinfo.role
	active = request.user.is_active

	if request.method == 'POST':
		usr_form = UpdateUser(request.POST, instance=request.user)
		info_form = UpdateEmployeeInfo(request.POST, request.FILES, instance=request.user.employeeinfo)
		if usr_form.is_valid() and info_form.is_valid():

			birthdate = info_form.cleaned_data.get("birth_date")
			empldate = info_form.cleaned_data.get("employment_Date")

			today = date.today()

			age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

			if age <= 17:
				# print("Sorry you cannot employed a person with age lower than 18 years")
				messages.warning(request, f"Sorry date of birth is lower than 18 years.")
				return redirect('uprofile')
				
			elif age >=80:
				# print("Sorry you cannot employed a person with age lower than 18 years in India")
				messages.warning(request, f"Sorry date of birth is more than 80 years")
				return redirect('uprofile')

			elif date.today() < empldate:
				# print("See this -------------", date.today())
				messages.warning(request, f"Sorry employment date cannot be more than today's date")
				return redirect('uprofile')
			else:	
				usr_form.save()
				info_form.save() #00mohamed
				# last_name = usr_form.cleaned_data.get('first_name')
				messages.success(request, f"You've updated your info...")
				return redirect('uprofile')
	else:
		usr_form = UpdateUser(instance=request.user)
		info_form = UpdateEmployeeInfo(instance=request.user.employeeinfo)
		context = {'usr_form': usr_form, 'info_form': info_form, 'title': 'Update Profile'}
		if ((usertype == 'Manager' or usertype == 'Admin') and active == True):
			return render(request, 'users/uprofile.html', context)
		else:
			return render(request, 'users/uprofile_fdesk.html', context)


def user_details(request,usr):
	usertype = request.user.employeeinfo.role
	active = request.user.is_active
	if ((usertype == 'Manager' or usertype == 'Admin') and active == True):
		obj1 = get_object_or_404(User, id=usr)
		obj2 = get_object_or_404(EmployeeInfo, user=usr)
		
		context = {'title': 'User Details', 'obj1': obj1, 'obj2': obj2}

		return render(request, 'users/user_details.html', context)

	else:
		# print('Sorry you Dont have access here5 ..')
		messages.warning(request, f"Sorry you dont have access to that page ..")
		return redirect('denied')

