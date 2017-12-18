# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Подгруппа',
                'verbose_name_plural': 'Подгруппы',
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы', 'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары', 'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(related_name='subcategories', to='shop.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(default=1, related_name='products', to='shop.Subcategory'),
            preserve_default=False,
        ),
    ]
