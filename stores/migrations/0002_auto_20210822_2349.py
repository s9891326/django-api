# Generated by Django 3.2.5 on 2021-08-22 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='store',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]