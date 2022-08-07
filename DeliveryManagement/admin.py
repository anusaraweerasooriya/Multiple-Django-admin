from django.contrib import admin


class DeliveryAdmin(admin.AdminSite):
    site_header = 'Delivery Admin Area'


delivery_admin = DeliveryAdmin(name='delivery_admin')
