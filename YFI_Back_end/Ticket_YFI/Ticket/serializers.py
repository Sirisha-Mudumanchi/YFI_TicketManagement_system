from rest_framework import serializers

from .models import TicketData

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=TicketData
        fields=["id","customer_name","issue_description","pripority"]