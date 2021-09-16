# Generated by Django 3.2.2 on 2021-09-15 13:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='store',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='store',
            name='store_type',
        ),
        migrations.AddField(
            model_name='comment',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='評價內容'),
        ),
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='菜單內容物說明'),
        ),
        migrations.AddField(
            model_name='menu',
            name='picture',
            field=models.ImageField(blank=True, upload_to='menus', verbose_name='菜單圖片'),
        ),
        migrations.AddField(
            model_name='menu',
            name='type',
            field=models.CharField(choices=[('Recommend_product', '推薦商品'), ('Popular_select', '人氣精選'), ('Meal', '套餐'), ('Rice', '飯類'), ('Noodles', '麵類'), ('Side_dishes', '小菜類')], default='Recommend_product', max_length=50, verbose_name='菜單類型'),
        ),
        migrations.AddField(
            model_name='store',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='簡介'),
        ),
        migrations.AddField(
            model_name='store',
            name='picture',
            field=models.ImageField(default='', upload_to='stores', verbose_name='店家圖片'),
        ),
        migrations.AddField(
            model_name='store',
            name='type',
            field=models.CharField(choices=[('Japan', '日式料理'), ('Western', '西式料理'), ('Taiwan', '台式料理')], default='Taiwan', max_length=10, verbose_name='店家類型'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='評價者'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='score',
            field=models.IntegerField(choices=[(1, '一顆星'), (2, '二顆星'), (3, '三顆星'), (4, '四顆星'), (5, '五顆星')], default=3, verbose_name='評價分數'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=20, verbose_name='菜單名稱'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.IntegerField(verbose_name='菜單價格'),
        ),
        migrations.AlterField(
            model_name='store',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='創建時間'),
        ),
        migrations.AlterField(
            model_name='store',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='創建者'),
        ),
        migrations.AlterField(
            model_name='store',
            name='local',
            field=models.CharField(max_length=50, verbose_name='地點'),
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=30, verbose_name='店家'),
        ),
        migrations.AlterField(
            model_name='store',
            name='phone_number',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '0912-345-678'", regex='^\\d{4}\\-\\d{3}\\-\\d{3}$')], verbose_name='聯絡電話'),
        ),
    ]
