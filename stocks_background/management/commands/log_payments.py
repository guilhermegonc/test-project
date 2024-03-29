from datetime import datetime, date

from dateutil.relativedelta import *
from django.core.management.base import BaseCommand, CommandError

from expenses_management.expensesHelper import create_expense
from expenses_management.recurringHelper import get_recurring
from app.userHelper import get_all_users
from app.models import Users

import sys

class Command(BaseCommand):
    help = 'Update Recommendations'

    def handle(self, *args, **options):
        self.log_payments()
        return


    def log_payments(self):
        if datetime.today().day == 1:
            date = datetime.today().strftime('%Y-%m-01')
            users = get_all_users()
            to_register = [get_recurring(u.id, [True]) for u in users]
            [self.register_payment(ur['data'], date) for ur in to_register]
        return


    def register_payment(self, recurring, date):
        return [self.write_payload(r, date) for r in recurring]


    def write_payload(self, recurring, date):
        payload = {'user': Users.objects.get(id=recurring['user_id']), 'name': recurring['name'], 'type': recurring['type'], 
            'date': date, 'value': recurring['value'], 'recurring': True}        
        return create_expense(payload)
