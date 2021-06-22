from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from customers.models import Customers
from cloths.models import Cloths
from orders.models import Orders, OrderDetails
from payments.models import Payments
from laundry.views import logs


@login_required
def fdesk_dashboard(request):
	usertype = request.user.employeeinfo.role
	active = request.user.is_active

	if ((usertype == 'Front Desk' or usertype == 'Supervisor') and active == True):
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
		logs(request, 'Normal', 'View front desk dashboard')
		context = {'title': 'Front Desk Dashboard','cust': cust_c, 'ready_c': ready_c, 'pend_c': pend_c}
		# results = Members.objects.raw('SELECT * FROM myapp_members GROUP BY designation')
		return render(request, 'fdesk/fdeskdash.html', context)

	else:
		logs(request, 'Violation', 'Tried to access the front desk dashboard')
		messages.warning(request, f"Sorry you dont have access to that page ..")
		return redirect('denied')
