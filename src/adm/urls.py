# from django.contrib import admin
from django.urls import path
from . import views
from users import views as userac_views
from cloths import views as cloths_views
from machines import views as mac_views



urlpatterns = [
    path('', views.admindashboard, name='admin-dashboard'), # as home
    path('emplyview/', userac_views.employee_view, name='emply-view'),
    path('add_user/', userac_views.add_user, name='add_user'), # django admin page
    path("add_emp_info/<int:usr>/", userac_views.add_emp_info, name='add_emp_info'), # django admin page
    path("user_info_update/<int:usr>/", userac_views.user_info_update, name='user_info_update'), # django admin page
    path("user_details/<int:usr>/", userac_views.user_details, name='user_details'), # django admin page
    path("add_cloths/", cloths_views.add_cloths, name='add_cloths'), # django admin page
    path("update_cloths/<int:clothid>/", cloths_views.update_cloths, name='update_cloths'), # django admin page
    path("view_cloths/", cloths_views.view_cloths, name='view_cloths'), # django admin page
    path("cloth_details/<int:clothid>/", cloths_views.cloth_details, name='cloth_details'), # django admin page
    path("add_mac/", mac_views.add_machine, name='add_mac'), # django admin page
    path("view_mac/", mac_views.view_machines, name='view_mac'), # django admin page
    path("update_mac/<int:macid>/", mac_views.update_machine, name='update_mac'), # django admin page
    path("mac_details/<int:macid>/", mac_views.mac_details, name='mac_details'), # django admin page
    path("remove_cloth/<int:clothid>/", cloths_views.remove_cloth, name='remove_cloth'),


    
]
