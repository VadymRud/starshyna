import django_tables2 as tables
from .models import ServiseID


class ServiseIDTable(tables.Table):
    class Meta:
        model = ServiseID
        template_name = "django_tables2/bootstrap5.html"
        fields = ("name", "sename", "third_name")
