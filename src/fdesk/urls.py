# from django.contrib import admin
from django.urls import path
from . import views
from orders import views as order_views
from payments import views as pay_views

urlpatterns = [
    path('', views.fdesk_dashboard, name='fdesk-dashboard'), # as home
    path("place_order/<int:custid>/", order_views.place_order, name='place_order'),
    # path("place_order/<int:custid>/", order_views.place_order, name='place_order'),
    path("add_cash_payment/<str:trans>", pay_views.add_cash_payment, name='add_cash_payment'),
    path("add_card_payment/<str:trans>/", pay_views.add_card_payment, name='add_card_payment'),
    path("remove_item/<int:ordid>/", order_views.remove_item, name='remove_item'),
    path("reciept/", pay_views.reciept, name='reciept'),
    path("pend_collect/", order_views.pend_collect, name='pend_collect'),
    path("pendding_order/", order_views.pendding, name='pendding_order'),
    path("view_order/<str:trans>/", order_views.view_order, name='view_order'),
    path("ready/<str:trans>/", order_views.ready, name='ready'),
    path("collect/<str:trans>/", order_views.collect, name='collect'),

]
