# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20171218_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available',
        ),
    ]
