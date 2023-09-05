from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_migrate
from django.contrib.auth.models import AbstractUser

from apps.application.services.utils import create_employees


class Employee(AbstractUser):
    """
    Castomize Django user. Added porbation time and his position.
    """
    probation = models.BooleanField(default=False)
    position = models.CharField(verbose_name='Position', max_length=164, blank=True, null=True)


class Order(models.Model):
    """
    Model with all the orders.
    """
    
    task_id = models.PositiveIntegerField(verbose_name='Task ID', unique=True)
    name = models.CharField(max_length=164, verbose_name='Order name')
    desctiption = models.TextField(verbose_name='Desctiption')
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE, verbose_name='Empoloyee')
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    
    def __str__(self):
        return f'ID: {self.task_id} Name: {self.name}'


@receiver(post_migrate)
def initial_employees(sender, **kwargs) -> None:
    """
    Initialization of employees if there`re less than 3.
    """
    employee_count = Employee.objects.count()
    if employee_count < 3:
        create_employees(Employee, employee_count)
    