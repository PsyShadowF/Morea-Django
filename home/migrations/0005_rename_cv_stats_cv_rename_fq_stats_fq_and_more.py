# Generated by Django 4.1.3 on 2022-12-13 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_motes_type_stats'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stats',
            old_name='CV',
            new_name='cv',
        ),
        migrations.RenameField(
            model_name='stats',
            old_name='FQ',
            new_name='fq',
        ),
        migrations.RenameField(
            model_name='stats',
            old_name='Max',
            new_name='max',
        ),
        migrations.RenameField(
            model_name='stats',
            old_name='Mean',
            new_name='mean',
        ),
        migrations.RenameField(
            model_name='stats',
            old_name='Median',
            new_name='median',
        ),
        migrations.RenameField(
            model_name='stats',
            old_name='Min',
            new_name='min',
        ),
        migrations.RenameField(
            model_name='stats',
            old_name='STD',
            new_name='std',
        ),
        migrations.RenameField(
            model_name='stats',
            old_name='TQ',
            new_name='tq',
        ),
    ]