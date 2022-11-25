# Generated by Django 4.1.3 on 2022-11-22 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='collect_date',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='data',
            name='min_lh',
            field=models.FloatField(default=''),
        ),
        migrations.AlterField(
            model_name='data',
            name='min_ppm',
            field=models.FloatField(default=''),
        ),
        migrations.AlterField(
            model_name='data',
            name='min_wh',
            field=models.FloatField(default=''),
        ),
        migrations.AlterField(
            model_name='data',
            name='total_l',
            field=models.FloatField(default=''),
        ),
        migrations.AlterField(
            model_name='data',
            name='total_wh',
            field=models.FloatField(default=''),
        ),
    ]