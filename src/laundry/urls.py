from django.contrib import admin
from django.contrib.auth import views as authac_views
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import denied, switch_user
from users import views as userac_views
from customers import views as cust_views
from orders import views as order_views
from adm import views as adv
from reports import views as report_view

urlpatterns = [
    path('', authac_views.LoginView.as_view(template_name='users/login.html'), name='login_page'), # login page for everyone which is also the default page to load
    path('logout', authac_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), # login page for everyone which is also the default page to load
    path('password-reset', 
        authac_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'), # login page for everyone which is also the default page to load
   path('password-reset/done/', 
        authac_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),
   path('password-reset-confirm/<uidb64>/<token>/', 
        authac_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
   path('password-reset-complete/',
         authac_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('adm/', include('adm.urls')), # takes you to the adm app section i.e if you are admin
    path('fdesk/', include('fdesk.urls')),
    path('uprofile/', userac_views.user_profile, name='uprofile'), # django admin page
    path("denied", denied, name='denied'), # denied user access
    path('decide', switch_user, name='decide'), # switch user base on role

    path('add_customer', cust_views.add_customer, name='add_customer'),
    path('update_customer/<int:custid>/', cust_views.update_customer, name='update_customer'),
    path('view_customers', cust_views.view_customers, name='view_customers'),
    path('allorders', report_view.allorders, name='allorders'),
    path('all_ordersby/<int:custid>/', report_view.all_ordersby, name='all_ordersby'),
    path('month_report/', report_view.month_report, name='month_report'),

    path('admin/', admin.site.urls), # django admin page

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
