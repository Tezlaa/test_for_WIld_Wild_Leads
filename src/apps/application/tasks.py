from celery import shared_task

from apps.application.services.producer import Producer


@shared_task()
def create_order_task() -> None:
    Producer().create_order()