# Generated by Django 4.0.4 on 2022-07-26 07:10

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_khayer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='madadjo',
            name='creating_date',
            field=django_jalali.db.models.jDateField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]