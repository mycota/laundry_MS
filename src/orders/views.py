from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
import time
from customers.models import Customers
from cloths.models import Cloths
from .models import Orders, OrderDetails
from django.core.mail import send_mail
from laundry.views import logs


# from .forms import AddOrderDetailForm


@login_required
def place_order(request, custid):
	cloths = Cloths.objects.all()

	if request.method == 'POST':

		tranid = request.POST["transid"]
		qty = request.POST["qty"]
		clothid = request.POST["item"]
		cloth_details = get_object_or_404(Cloths, id=clothid)
		cloth_name = cloth_details.cloth_name
		cloth_price = cloth_details.wash_price
		price = cloth_price * float(qty)
		order_detail = OrderDetails(user=request.user, transid=tranid, cloth_name=cloth_name,
			quantity=qty, unit_price=cloth_price, sub_total=price)
		order_detail.save()
		total = 0
		items = OrderDetails.objects.filter(transid=tranid)
		for x in items:
			total += float(x.sub_total)

		context = {'title': 'Add Cloths', 'custid': custid, 'tranid': tranid, 'items': items, 'cloths': cloths, 'total': total}
		logs(request, 'Normal', 'Adding cloths to cart '+cloth_name)
		return render(request, 'orders/place_order.html', context) # as register.html


		# return render(request, 'orders/place_order.html', context) # as register.html
	
	else:
		tranid = "%s-%d" % (custid, time.time())
		items = OrderDetails.objects.filter(transid=tranid)

		total = 0
		for x in items:
			total += float(x.sub_total)
		context = {'title': 'Add Cloths', 'custid': custid, 'tranid': tranid, 'cloths': cloths, 'total': total}
		logs(request, 'Normal', 'Adding cloths to cart for customer')
	return render(request, 'orders/place_order.html', context) # as register.html

@login_required
def pendding(request):
	orders = Orders.objects.filter(order_status='Pending')
	usertype = request.user.employeeinfo.role
	if usertype == 'Admin' or usertype == 'Manager':
		logs(request, 'Normal', 'View all pending orders')
		return render(request, 'orders/pendding_orders_adm.html', {'orders': orders, 'title': 'Pending orders'})
	else:
		logs(request, 'Normal', 'View all pending orders')
		return render(request, 'orders/pendding_orders.html', {'orders': orders, 'title': 'Pending orders'})

@login_required
def pend_collect(request):
	orders = Orders.objects.filter(order_status='Ready')
	usertype = request.user.employeeinfo.role
	if usertype == 'Admin' or usertype == 'Manager':
		logs(request, 'Normal', 'View all pending orders')
		return render(request, 'orders/ready_orders_adm.html', {'orders': orders, 'title': 'Pending for collection'})
	else:
		logs(request, 'Normal', 'View all pending orders')
		return render(request, 'orders/ready_orders.html', {'orders': orders, 'title': 'Pending for collection'})


@login_required
def view_order(request, trans):
	ordr = Orders.objects.filter(transid=trans).first()
	items = OrderDetails.objects.filter(transid=trans)
	total = 0
	for x in items:
		total += float(x.sub_total)

	custid = trans.split('-')
	custid = custid[0]
	customers = Customers.objects.filter(id=custid).first()

	usertype = request.user.employeeinfo.role
	context = {'customers': customers, 'transid': trans,
		 'total': total, 'title': 'Payment a reciept', 'items': items, 'ordr': ordr}

	if usertype == 'Admin' or usertype == 'Manager':
		logs(request, 'Normal', 'View order reciept')
		return render(request, 'payments/reciept_adm.html', context)
	else:
		logs(request, 'Normal', 'View order reciept '+trans)
		return render(request, 'payments/reciept.html', context)


@login_required
def ready(request, trans):
	Orders.objects.filter(transid=trans).update(order_status='Ready')
	orders = Orders.objects.filter(order_status='Pending')
	cut = trans.split('-')
	custid = cut[0]
	customers = get_object_or_404(Customers, id=custid)
	customer = customers.cust_name
	customer_name = customers.cust_name
	cust_mail = customers.cust_email

	# send email to customer
	body = 'Hello '+customer_name+','+'\n'
	body += 'Thank you for using our service, your cloths are ready for pickup,'+'\n' 
	body += 'kindly collect them from 8:30am to 5:30 on Mondays to Saturdays'+'\n'
	body += 'your transaction id is '+trans+'\n'
	send_mail('Adamu Laundry Services', body, 'adamumh@gmail.com', [cust_mail], fail_silently=False)

	usertype = request.user.employeeinfo.role
	if usertype == 'Admin' or usertype == 'Manager':
		logs(request, 'Normal', 'Change pending order to ready '+trans)
		return render(request, 'orders/pendding_orders_adm.html', {'orders': orders, 'title': 'Pending'})
	else:
		logs(request, 'Normal', 'Change pending order to ready '+trans)
		return render(request, 'orders/pendding_orders.html', {'orders': orders, 'title': 'Pending'})

@login_required
def collect(request, trans):
	Orders.objects.filter(transid=trans).update(order_status='Collected')
	orders = Orders.objects.filter(order_status='Ready')
	usertype = request.user.employeeinfo.role

	cut = trans.split('-')
	custid = cut[0]
	customers = get_object_or_404(Customers, id=custid)
	customer = customers.cust_name
	customer_name = customers.cust_name
	cust_mail = customers.cust_email

	# send email to customer
	body = 'Hello '+customer_name+','+'\n'
	body += 'Thank you for using our service, we hope you were serve well,'+'\n' 
	body += 'see you soon, We work from 8:30am to 5:30 on Mondays to Saturdays'+'\n'
	body += 'your transaction id is '+trans+'\n'
	send_mail('Adamu Laundry Services', body, 'adamumh@gmail.com', [cust_mail], fail_silently=False)

	if usertype == 'Admin' or usertype == 'Manager':
		logs(request, 'Normal', 'Customer collected item '+trans)
		return render(request, 'orders/ready_orders_adm.html', {'orders': orders, 'title': 'Pending for collection'})
	else:
		logs(request, 'Normal', 'Customer collected item '+trans)
		return render(request, 'orders/ready_orders.html', {'orders': orders, 'title': 'Pending for collection'})



@login_required
def remove_item(request, ordid):
	cloths = Cloths.objects.all()
	cust_trans = get_object_or_404(OrderDetails, id=ordid)
	tranid = cust_trans.transid
	custid = tranid.split('-')
	custid = custid[0]

	OrderDetails.objects.filter(id=ordid).delete()

	items = OrderDetails.objects.filter(transid=tranid)
	total = 0
	for x in items:
		total += float(x.sub_total)
	logs(request, 'Normal', 'Removing item from cart ')
	context = {'title': 'Add Cloths', 'custid': custid, 'tranid': tranid, 'items': items, 'cloths': cloths, 'total': total}
	return render(request, 'orders/place_order.html', context) # as register.html


















