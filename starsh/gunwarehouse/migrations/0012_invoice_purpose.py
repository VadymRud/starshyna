# Generated by Django 4.1.5 on 2023-02-20 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gunwarehouse', '0011_gunwarehouse_invoice_gun_warehouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='purpose',
            field=models.CharField(choices=[('1', 'Arrived'), ('2', 'Out')], default='2', max_length=50, verbose_name='Purpose'),
        ),
    ]
