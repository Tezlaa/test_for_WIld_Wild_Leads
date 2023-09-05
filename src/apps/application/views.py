from typing import Any, Dict

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.application.services.consumer import (
    get_orders, delete_task, send_message_to_telegram
)


class TablePage(LoginRequiredMixin, TemplateView):
    """
    Creating a table with user tasks.
    """
    
    template_name = 'application/index.html'
    login_url = reverse_lazy('login')
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tasks'] = get_orders(employee=self.request.user)
        
        return context


class DeleteTask(View):
    """
    Delete task by his primary key and sending a message to the telegram group.
    """
    
    success_url = reverse_lazy('application:main-page')
    
    def post(self, request, task_id: int):
        success_url = self.get_success_url()
        employee = self.request.user
        
        message_data = delete_task(task_id=task_id)
        send_message_to_telegram(message_data=message_data, employee=employee)
        
        return HttpResponseRedirect(success_url)
    
    def get_success_url(self) -> str:
        return self.success_url