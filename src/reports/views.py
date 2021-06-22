from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
import time
from customers.models import Customers
from cloths.models import Cloths
from orders.models import Orders, OrderDetails
from laundry.views import logs

@login_required
def allorders(request):
	usertype = request.user.employeeinfo.role
	orders = Orders.objects.all()
	total = 0
	for x in orders:
		total += float(x.total)
	if usertype == 'Admin' or usertype =='Manager':
		return render(request, 'reports/allorders_adm.html', {'orders': orders, 'title': 'All orders',
		'usertype': usertype, 'total': total})
	else:
		return render(request, 'reports/allorders.html', {'orders': orders, 'title': 'All orders',
		'usertype': usertype, 'total': total})


@login_required # for customer history
def all_ordersby(request, custid):
	usertype = request.user.employeeinfo.role
	orders = Orders.objects.filter(customer=custid)
	customers = get_object_or_404(Customers, id=custid)

	total = 0
	for x in orders:
		total += float(x.total)
	if usertype == 'Admin' or usertype =='Manager':
		return render(request, 'reports/all_ordersby_adm.html', {'orders': orders, 'customers': customers,'title': 'All orders by customer',
		'usertype': usertype, 'total': total})
	else:
		return render(request, 'reports/all_ordersby.html', {'orders': orders, 'customers': customers,'title': 'All orders by customer',
		'usertype': usertype, 'total': total})

def month_report(request):
	usertype = request.user.employeeinfo.role
	active = request.user.is_active
	users = User.objects.all()

	if ((usertype == 'Manager' or usertype == 'Admin') and active == True):
		if request.method == "POST" :
			frdate = request.POST['frdate']
			todate = request.POST['todate']
			order_type = request.POST['order_type']
			user = request.POST['user']

			if order_type == 'All' and user == 'All':
				orders = Orders.objects.filter(order_date__range=(frdate,todate)) #.order_by('order_date')
				total=0
				for x in orders:
					total += x.total

				header = 'Report from '+frdate+' to '+todate+ ' for all users and type'
				context = {'title': 'Monthly report', 'users': users, 'orders': orders, 'header': header, 'total':total}
				return render(request, 'reports/month_report.html', context)

			if order_type != 'All' and user != 'All':
				orders = Orders.objects.filter(order_status=order_type, user=user, order_date__range=(frdate,todate)) #.order_by('order_date')
				total=0
				for x in orders:
					total += x.total

				header = 'Report from '+frdate+' to '+todate+ ' for '+order_type
				context = {'title': 'Monthly report', 'users': users, 'orders': orders, 'header': header, 'total':total}
				return render(request, 'reports/month_report.html', context)

			if order_type == 'All' and user != 'All':
				orders = Orders.objects.filter(user=user, order_date__range=(frdate,todate)) #.order_by('order_date')
				total=0
				for x in orders:
					total += x.total

				header = 'Report from '+frdate+' to '+todate
				context = {'title': 'Monthly report', 'users': users, 'orders': orders, 'header': header, 'total':total}
				return render(request, 'reports/month_report.html', context)


			if order_type != 'All' and user == 'All':
				orders = Orders.objects.filter(order_status=order_type, order_date__range=(frdate,todate)) #.order_by('order_date')
				total=0
				for x in orders:
					total += x.total

				header = 'Report from '+frdate+' to '+todate+ ' for '+order_type
				context = {'title': 'Monthly report', 'users': users, 'orders': orders, 'header': header, 'total':total}
				return render(request, 'reports/month_report.html', context)
			else:
				header = 'No result found'
				context = {'title': 'Monthly report', 'users': users, 'orders': orders, 'header': header, 'total':total}
				return render(request, 'reports/month_report.html', context)

		else:
			context = {'title': 'Monthly report', 'users': users}
			return render(request, 'reports/month_report.html', context)

	else:
		if request.method == "POST" :
			frdate = request.POST['frdate']
			todate = request.POST['todate']
			order_type = request.POST['order_type']

			if order_type != 'All':
				orders = Orders.objects.filter(user=request.user,order_status=order_type, order_date__range=(frdate,todate)) #.order_by('order_date')
				total=0
				for x in orders:
					total += x.total

				header = 'Report from '+frdate+' to '+todate+ ' for '+order_type
				context = {'title': 'Monthly report', 'users': users, 'orders': orders, 'header': header, 'total':total}
				return render(request, 'reports/month_report_fd.html', context)
			else:
				orders = Orders.objects.filter(user=request.user,order_date__range=(frdate,todate)) #.order_by('order_date')
				total=0
				for x in orders:
					total += x.total

				header = 'Report from '+frdate+' to '+todate
				context = {'title': 'Monthly report', 'users': users, 'orders': orders, 'header': header, 'total':total}
				return render(request, 'reports/month_report_fd.html', context)

		else:
			context = {'title': 'Monthly report'}
			return render(request, 'reports/month_report_fd.html', context)
		