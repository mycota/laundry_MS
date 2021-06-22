from django.shortcuts import render, redirect
from django.contrib import messages
from laundry.views import logs

# from django.http import HttpResponse
from users.models import EmployeeInfo
from customers.models import Customers
from orders.models import Orders
from cloths.models import Cloths
from machines.models import Machines
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib.auth.decorators import login_required

@login_required
def admindashboard(request): # as homet
	usertype = request.user.employeeinfo.role
	active = request.user.is_active

	if ((usertype == 'Manager' or usertype == 'Admin') and active == True):
		cust = Customers.objects.values('id').annotate(dcount=Count('id'))
		cust_c = 0
		for c in cust:
			cust_c += 1
		ready = Orders.objects.filter(order_status='Ready')
		ready_c = 0
		for r in ready:
			ready_c += 1

		pend = Orders.objects.filter(order_status='Pendding')
		pend_c = 0
		for p in pend:
			pend_c += 1

		usrs = User.objects.all()
		usr_c = 0
		for p in usrs:
			usr_c += 1

		mac = Machines.objects.all()
		mac_c = 0
		for p in mac:
			mac_c += 1

		cloth = Cloths.objects.all()
		cloth_c = 0
		for p in cloth:
			cloth_c += 1
		logs(request,'Normal','view admin dashboard')
		context = {'title': 'Admin Dashboard', 'usr_c': usr_c, 'cust_c': cust_c, 'mac_c': mac_c, 'cloth_c': cloth_c}
		return render(request, 'adm/admdash.html', context)
	else:
		# print('Sorry you Dont have access here ..')
		logs(request,'Violation','Tried to access the admin dashboard !!!!')
		messages.warning(request, f"Sorry you dont have access to that page ..")
		return redirect('denied')
