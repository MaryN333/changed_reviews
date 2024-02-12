# Generated by Django 3.2.20 on 2024-02-10 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_remove_restaurant_reviews_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='type',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='type',
            field=models.ManyToManyField(to='restaurant.Type'),
        ),
    ]
