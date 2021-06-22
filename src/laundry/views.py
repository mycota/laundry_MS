import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from machines.models import Machines
from customers.models import Customers
from cloths.models import Cloths
from users.models import Logs
from orders.models import Orders, OrderDetails
from django.db.models import Count


def ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    # print('My ip: ',ip)
    return ip

def logs(request, event_type, event):
	ipp = ip(request)
	user = User(id=request.user.id)
	add_log = Logs(user=user, ip_addr=ipp, event_type=event_type, event=event)
	add_log.save()

# decide where aeach user shld go
@login_required
def switch_user(request):
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
		logs(request,'Nomal','login')
		context = {'title': 'Admin Dashboard', 'usr_c': usr_c, 'cust_c': cust_c, 'mac_c': mac_c, 'cloth_c': cloth_c}
		return render(request, 'adm/admdash.html', context)
	
	elif ((usertype == 'Supervisor' or usertype == 'Front Desk') and active == True):
		print(os.environ.get('EMAIL_USER'))
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
		logs(request,'Nomal','login')

		context = {'title': 'Front Desk Dashboard','cust': cust_c, 'ready_c': ready_c, 'pend_c': pend_c}
		# print(os.environ.get('EMAIL_USER'))
		print('Sorry you Dont have access here ..')
		return render(request, 'fdesk/fdeskdash.html', context)

			# print('Sorry you Dont have access here ..')
	else:
		return redirect('denied')


		
def denied(request):
	return render(request, "denied.html")






# the default page to load once you open this app
# def login_page(request):
# 	return render(request, "login.html")
