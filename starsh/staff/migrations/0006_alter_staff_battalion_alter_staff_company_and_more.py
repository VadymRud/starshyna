# Generated by Django 4.1.5 on 2023-02-08 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_battalion_company_platoon_squad_staff_battalion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='battalion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.battalion', verbose_name='Battalion'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.company', verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='platoon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.platoon', verbose_name='Взвод'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='squad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.squad', verbose_name='Squad'),
        ),
    ]