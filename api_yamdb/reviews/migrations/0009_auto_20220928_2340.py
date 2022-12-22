# Generated by Django 2.2.16 on 2022-09-28 17:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20220928_0130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'default_related_name': '%(class)ss', 'ordering': ('-pub_date',), 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'default_related_name': '%(class)ss', 'ordering': ('-pub_date',), 'verbose_name': 'Обзор', 'verbose_name_plural': 'Обзоры'},
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(help_text='Укажите оценку произведения (от 1 до 10)', validators=[django.core.validators.MinValueValidator(1, message='Укажите оценку больше либо равную 1'), django.core.validators.MaxValueValidator(10, message='Укажите оценку меньше либо равную 10')], verbose_name='Оценка'),
        ),
    ]