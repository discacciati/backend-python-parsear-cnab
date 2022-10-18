import uuid
from django.core.validators import MaxLengthValidator
from django.db import models

class Operations(models.Model): 
    id = models.UUIDField(default=uuid.uuid5, primary_key=True)
    type = models.IntegerField(choices=Types.choices)
    date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    card_number = models.CharField(max_length=12)
    hour = models.TimeField()
    store_owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)
    
    def __str__(self):
        return f'{self.id} - {self.date}-{self.hour} - {self.type} {self.store_name} - {round(self.value / 100)}'