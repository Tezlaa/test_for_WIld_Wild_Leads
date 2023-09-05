from random import choice, randint

from apps.application.models import Employee, Order


class Producer:
    def create_order(self):
        self.employee = self._get_random_employee()
        self.count_tasks = self._get_count_tasks()
        self.task_id = randint(100000, 999999)
        
        self._create_order()
        
    def _create_order(self) -> None:
        name = f'Test order №{self.count_tasks + 1}'
        desctiption = f'ID: {self.task_id}'
        
        Order.objects.create(
            task_id=self.task_id,
            name=name,
            desctiption=desctiption,
            employee=self.employee
        )
    
    def _get_count_tasks(self) -> int:
        return Order.objects.count()
    
    def _get_random_employee(self) -> Employee:
        employees = Employee.objects.all()
        random_employee = choice(employees)
        
        return random_employee
        