from django.db import models

class Subscription(models.Model):
    user = models.CharField(max_length=255, blank=False) 
    plan = models.CharField(max_length=50, blank=True)
    price = models.IntegerField()
    status = models.CharField(max_length=50, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    payment_id = models.CharField(max_length=110, blank=True)
    payment_status = models.CharField(max_length=100, blank=False)
    auto_renewal = models.DateTimeField()
    time_created = models.TimeField()
    date_created = models.DateField()