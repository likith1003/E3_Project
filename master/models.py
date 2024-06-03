from django.db import models

# Create your models here.
item_choices = (
    ('Veg','Veg'),
    ('Non-Veg','Non-Veg'),
    ('Egg','Egg')
)

class Item(models.Model):
    item_id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=50)
    item_price = models.IntegerField()
    item_desc = models.CharField(max_length=50)
    item_type = models.CharField(choices=item_choices, max_length=50)
    item_photo = models.ImageField()

    def __str__(self):
        return self.item_name