from django.contrib import admin

from apps.application.models import Order, Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'probation', 'position')


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'name', 'desctiption', 'employee')