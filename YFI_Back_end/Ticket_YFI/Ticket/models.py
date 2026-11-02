from django.db import models

# Create your models here.

class TicketData(models.Model):
    customer_name=models.CharField(max_length=100)
    issue_description=models.TextField()

    def __str__(self):
        return f"name={self.customer_name} ,issue_description={self.issue_description}"
