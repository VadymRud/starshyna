# Generated by Django 4.1.5 on 2023-03-03 10:06

from django.db import migrations, models
import django_jsonform.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gunwarehouse', '0014_invoice_good_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_weapon', models.CharField(choices=[(1, 'Pistol'), (2, 'Rifle'), (3, 'Machinegun'), (4, 'Grenade launcher'), (5, 'Sniper rifle'), (5, 'Large-caliber weapon')], default='1', max_length=50, verbose_name='Type Weapon')),
                ('calibre', models.CharField(max_length=50, verbose_name='Calibre')),
                ('serial_number', models.CharField(max_length=256, verbose_name='Serial number')),
                ('issued', models.PositiveSmallIntegerField(choices=[(1, 'Not issued'), (2, 'Issued'), (3, 'Miss')], default=1, verbose_name='Issued')),
                ('additional', django_jsonform.models.fields.JSONField()),
            ],
        ),
        migrations.AlterField(
            model_name='invoice',
            name='good_class',
            field=models.CharField(choices=[('1', 'Боєприпас'), ('2', 'Gun'), ('3', 'Devises')], default='2', max_length=50, verbose_name='Good class'),
        ),
    ]
