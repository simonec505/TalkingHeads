# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chatMessages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 15, 19, 15, 58, 928185, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
