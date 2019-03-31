import django_tables2 as tables
from .models import UserQuotes

class QuoteTable(tables.Table):
    class Meta:
        model = UserQuotes
        template_name = 'django_tables2/bootstrap.html'