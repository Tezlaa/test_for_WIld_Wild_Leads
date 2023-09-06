import requests
from datetime import datetime

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from django.conf import settings

from apps.application.models import Order


def get_orders(employee) -> QuerySet[Order]:
    return Order.objects.filter(employee=employee)


def delete_task(task_pk: int) -> dict:
    instance = get_object_or_404(Order, pk=task_pk)
    result = {
        'pk': instance.pk,
        'task_id': instance.task_id,
        'name': instance.name
    }
    
    instance.delete()
    
    return result
    

def send_message_to_telegram(message_data: dict, employee) -> None:
    pk = message_data.get('pk')
    task_id = message_data.get('task_id')
    name = message_data.get('name')
    employee_info = f'{employee.first_name} - {employee.position}'
    time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    
    message = (f'Задача №{pk}-{task_id} під назвою: ***{name}*** \n'
               f'була опрацьована ***{employee_info}*** об ***{time}*** 🟢')
    
    requests.get(url=f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage",
                 data={"chat_id": settings.TELEGRAM_CHAT_ID,
                       "text": message,
                       "parse_mode": "MARKDOWN", })