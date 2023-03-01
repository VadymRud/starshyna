# Generated by Django 4.1.5 on 2023-02-28 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soldier', '0010_alter_award_options_alter_battlewound_options_and_more'),
        ('staff', '0006_alter_staff_battalion_alter_staff_company_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zvannya',
            fields=[
                ('zv_id', models.AutoField(primary_key=True, serialize=False)),
                ('zv_name', models.TextField()),
                ('zv_short_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'zvannya_name',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Adresa',
        ),
        migrations.DeleteModel(
            name='Kontrakt',
        ),
        migrations.DeleteModel(
            name='Nakaz',
        ),
        migrations.DeleteModel(
            name='NakazNomer',
        ),
        migrations.DeleteModel(
            name='NakazPlace',
        ),
        migrations.DeleteModel(
            name='Name',
        ),
        migrations.DeleteModel(
            name='OsvitaName',
        ),
        migrations.DeleteModel(
            name='Peremish',
        ),
        migrations.DeleteModel(
            name='Phones',
        ),
        migrations.DeleteModel(
            name='PidrozdilId',
        ),
        migrations.DeleteModel(
            name='PidrozdilName',
        ),
        migrations.DeleteModel(
            name='PosadaName',
        ),
        migrations.DeleteModel(
            name='Priznach',
        ),
        migrations.DeleteModel(
            name='PriznachOld',
        ),
        migrations.DeleteModel(
            name='PriznachOld2',
        ),
        migrations.DeleteModel(
            name='Ridny',
        ),
        migrations.DeleteModel(
            name='RidnyName',
        ),
        migrations.DeleteModel(
            name='Shtatka',
        ),
        migrations.DeleteModel(
            name='ShtatkaOld',
        ),
        migrations.DeleteModel(
            name='ShtatkaOld2',
        ),
        migrations.DeleteModel(
            name='SimStanName',
        ),
        migrations.DeleteModel(
            name='StatsName',
        ),
        migrations.DeleteModel(
            name='StatusName',
        ),
        migrations.DeleteModel(
            name='Table32',
        ),
        migrations.DeleteModel(
            name='Table35',
        ),
        migrations.DeleteModel(
            name='Temp',
        ),
        migrations.DeleteModel(
            name='Tmp',
        ),
        migrations.DeleteModel(
            name='Vysluga',
        ),
        migrations.DeleteModel(
            name='VyslugaNormy',
        ),
        migrations.DeleteModel(
            name='VyslugaZv',
        ),
        migrations.DeleteModel(
            name='Zbroya',
        ),
        migrations.DeleteModel(
            name='ZbroyaAll',
        ),
        migrations.DeleteModel(
            name='ZbroyaName',
        ),
        migrations.DeleteModel(
            name='ZbroyaSklad',
        ),
        migrations.DeleteModel(
            name='ZbrStatusName',
        ),
        migrations.DeleteModel(
            name='ZvannyaId',
        ),
        migrations.DeleteModel(
            name='ZvannyaName',
        ),
        migrations.DeleteModel(
            name='ZvGrupaName',
        ),
        migrations.DeleteModel(
            name='ZvilnComent',
        ),
        migrations.AlterModelOptions(
            name='battalion',
            options={'verbose_name': 'Батальйон', 'verbose_name_plural': 'Батальйони'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Рота', 'verbose_name_plural': 'Роти'},
        ),
        migrations.AlterModelOptions(
            name='squad',
            options={'verbose_name': 'Взвод', 'verbose_name_plural': 'Взвода'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'Штатка', 'verbose_name_plural': 'Штатка'},
        ),
        migrations.AlterField(
            model_name='battalion',
            name='name',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Імʼя'),
        ),
        migrations.AlterField(
            model_name='battalion',
            name='short_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Імʼя'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Імʼя'),
        ),
        migrations.AlterField(
            model_name='company',
            name='short_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Імʼя'),
        ),
        migrations.AlterField(
            model_name='platoon',
            name='name',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Імʼя'),
        ),
        migrations.AlterField(
            model_name='platoon',
            name='short_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Імʼя'),
        ),
        migrations.AlterField(
            model_name='squad',
            name='name',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Імʼя'),
        ),
        migrations.AlterField(
            model_name='squad',
            name='short_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Імʼя'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='battalion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.battalion', verbose_name='Батальйон'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.company', verbose_name='Рота'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='ocoba',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='soldier.serviseid', verbose_name='Військовослужбовець'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='poz',
            field=models.CharField(blank=True, max_length=512, verbose_name='Позивний'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='salary',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True, verbose_name='Заробітна плата'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='shpk',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='staff.shpk', verbose_name='ШПК'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='squad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.squad', verbose_name='Взвод'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='tariff_category',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True, verbose_name='Тарифна сітка'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='vacant',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Вакантна'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='vos',
            field=models.CharField(max_length=512, verbose_name='ВОС'),
        ),
    ]