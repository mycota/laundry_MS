from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
import time
from orders.models import Orders
from .models import Customers
from .forms import AddCustomerForm, UpdateCustomerForm
from laundry.views import logs


def add_customer(request):
	if request.method == 'POST':
		cust_form = AddCustomerForm(request.POST)
		if cust_form.is_valid():
			cust_form.save()
			cust_phone = cust_form.cleaned_data.get('cust_phone')
			print('before')
			custid = get_object_or_404(Customers, cust_phone=cust_phone)
			name = custid.cust_name
			custid = custid.id
			tranid = "%s-%d" % (custid, time.time())

			messages.success(request, f"You've added a new customer, place order now...")
			logs(request, 'Normal', 'Added new customer '+name)
			return redirect('place_order', custid=custid)
	else:
		cust_form = AddCustomerForm()
		context = {'cust_form': cust_form, 'title': 'Add Customer'}
		logs(request, 'Normal', 'Adding new customer')

	return render(request, 'customers/add_customer.html', context) # as register.html

def update_customer(request, custid):
	custObj = get_object_or_404(Customers, id=custid)
	if request.method == 'POST':
		cust_form = UpdateCustomerForm(request.POST, instance=custObj)
		if cust_form.is_valid():
			cust_form.save()
			cust_name = custObj.cust_name
			messages.success(request, f"You've updated {cust_name} info ...")
			logs(request, 'Normal', 'Updated a customer '+cust_name)
			return redirect('view_customers')

	else:
		cust_form = UpdateCustomerForm(instance=custObj)
		context = {'cust_form': cust_form, 'title':'Update customer info'}
		usertype = request.user.employeeinfo.role
		if usertype == 'Admin' or usertype == 'Manager':
			logs(request, 'Normal', 'Updating a customer record')
			return render(request, 'customers/update_customer_adm.html', context)
		else:
			logs(request, 'Normal', 'Updating a customer record')
			return render(request, 'customers/update_customer.html', context)
			


def view_customers(request):
	cust = Customers.objects.all()
	# results = Members.objects.raw('SELECT * FROM myapp_members GROUP BY designation')

	orders = Orders.objects.raw('SELECT DISTINCT id FROM orders_orders GROUP BY customer_id')
	usertype = request.user.employeeinfo.role
	active = request.user.is_active
	ordering = ['-timestamp']
	paginate_by = 2
	context = {'cust': cust, 'orders': orders, 'title': 'All customers', 'usertype': usertype, 'active': active}
	if usertype == 'Manager' or usertype == 'Admin':
		logs(request, 'Normal', 'View all customer records')
		return render(request, 'customers/view_customers_adm.html', context)
	else:
		logs(request, 'Normal', 'View all customer records')
		return render(request, 'customers/view_customers.html', context)

	