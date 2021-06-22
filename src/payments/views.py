from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
import time
from customers.models import Customers
from cloths.models import Cloths
from .models import Payments
from orders.models import Orders, OrderDetails
from django.core.mail import send_mail
from laundry.views import logs




@login_required
def add_cash_payment(request, trans):
	cut = trans.split('-')
	custid = cut[0]
	customers = get_object_or_404(Customers, id=custid)
	customer = customers.cust_name
	customer_name = customers.cust_name
	cust_mail = customers.cust_email
	total = 0
	count = 0
	items = OrderDetails.objects.filter(transid=trans)
	for x in items:
		total += float(x.sub_total)
		count += 1

	if request.method == 'POST':
		due = request.POST['date']
		customer = Customers(id=custid)
		orders = Orders(user=request.user, customer= customer, return_date=due, order_status='Pending', total_item=count,
			total=total, transid=trans)
		orders.save()
		ordid = get_object_or_404(Orders, transid=trans)
		ordr = Orders.objects.filter(transid=trans).first()
		ordid = ordr.id
		order = Orders(id=ordid)
		payments = Payments(user=request.user, customer= customer, order_id=order, payment_id=trans,
			transactid=trans, amount=total, pay_mthd='Cash')
		payments.save()

		# send email to customer
		body = 'Hello '+customer_name+','+'\n'
		body += 'Thank you for using our service, your cloths would be ready by '+due+'\n'
		body += 'your transaction id is '+trans+'\n'
		send_mail('Adamu Laundry Services', body, 'adamumh@gmail.com', [cust_mail], fail_silently=False)
		messages.success(request, f"Print out reciept to customer ....")
		context = {'customers': customers, 'transid': trans,
		 'total': total, 'title': 'Cash Payment', 'items': items, 'ordr': ordr}
		logs(request, 'Normal', 'Completed a payment using a add cash payment method for order '+trans)
		return render(request, 'payments/reciept.html', context)

	else:
		logs(request, 'Normal', 'Adding cash using add cash method for order '+trans)
		context = {'customer': customer, 'customers': customers, 'transid': trans,
		 'total': total, 'title': 'Cash Payment', 'items': items}
		messages.success(request, f"Complete cash payment process ...")
		return render(request, 'payments/cash_payment.html', context)
		

@login_required
def add_card_payment(request, trans):
	cut = trans.split('-')
	custid = cut[0]
	customers = get_object_or_404(Customers, id=custid)
	customer = customers.cust_name
	customer_name = customers.cust_name
	cust_mail = customers.cust_email
	total = 0
	count = 0
	items = OrderDetails.objects.filter(transid=trans)
	for x in items:
		total += float(x.sub_total)
		count += 1

	if request.method == 'POST':
		payid = request.POST['payid']
		due = request.POST['date']
		customer = Customers(id=custid)
		orders = Orders(user=request.user, customer= customer, return_date=due, order_status='Pending', total_item=count,
			total=total, transid=trans)
		orders.save()
		ordid = get_object_or_404(Orders, transid=trans)
		ordr = Orders.objects.filter(transid=trans).first()
		ordid = ordr.id
		order = Orders(id=ordid)
		payments = Payments(user=request.user, customer= customer, order_id=order, payment_id=payid,
			transactid=trans, amount=total, pay_mthd='Card')
		payments.save()

		body = 'Hello '+customer_name+','+'\n'
		body += 'Thank you for using our service, your cloths would be ready by '+due+'\n'
		body += 'your transaction id is '+trans+'\n'
		send_mail('Adamu Laundry Services', body, 'adamumh@gmail.com', [cust_mail], fail_silently=False)

		messages.success(request, f"Print out reciept to customer ....")
		context = {'customers': customers, 'transid': trans,
		 'total': total, 'title': 'Cash Payment', 'items': items, 'ordr': ordr}
		logs(request, 'Normal', 'Completed a payment using a add card payment method for order '+trans)
		return render(request, 'payments/reciept.html', context)

	else:
		logs(request, 'Normal', 'Adding cash using add card method for order '+trans)
		context = {'customer': customer, 'customers': customers, 'transid': trans, 'total': total, 'title': 'Cash Payment', 'items': items}
		messages.success(request, f"Complete card payment process on POS device...")
		return render(request, 'payments/card_payment.html', context)


def reciept(request):
		logs(request, 'Normal', 'View reciept')
		return render(request, 'payments/reciept.html')



