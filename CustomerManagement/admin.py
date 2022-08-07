from django.contrib import admin


class CustomerAdmin(admin.AdminSite):
    site_header = 'Customer Admin Area'


customer_admin = CustomerAdmin(name='customer_admin')
