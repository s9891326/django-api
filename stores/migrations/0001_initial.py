# Generated by Django 3.2.2 on 2021-09-01 14:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('store_type', models.CharField(choices=[('Japan', '日式料理'), ('Western', '西式料理'), ('Taiwan', '台式料理')], max_length=7)),
                ('phone_number', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '0912-345-678'", regex='^\\d{4}\\-\\d{3}\\-\\d{3}$')])),
                ('notes', models.TextField(blank=True, default='')),
                ('local', models.CharField(max_length=30)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='stores.store')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(1, '一顆星'), (2, '二顆星'), (3, '三顆星'), (4, '四顆星'), (5, '五顆星')], default=3)),
                ('notes', models.TextField(blank=True, default='')),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_items', to='stores.store')),
            ],
        ),
    ]
