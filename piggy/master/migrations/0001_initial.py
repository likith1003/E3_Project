# Generated by Django 4.2.13 on 2024-06-01 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.IntegerField()),
                ('item_desc', models.CharField(max_length=50)),
                ('item_type', models.CharField(choices=[('Veg', 'Veg'), ('Non-Veg', 'Non-Veg'), ('Egg', 'Egg')], max_length=50)),
                ('item_photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
