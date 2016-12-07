# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter_signup', '0002_auto_20160412_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslettersignup',
            name='current_referer',
            field=models.CharField(max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='newslettersignup',
            name='referer',
            field=models.CharField(default='', max_length=2048, verbose_name='Initial referer', blank=True),
            preserve_default=False,
        ),
    ]
