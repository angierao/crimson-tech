# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='photographer',
            field=models.CharField(default=b'Unknown', max_length=500),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='content',
            name='subtitle',
            field=models.CharField(default=b'', max_length=500),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(default=b'', max_length=500),
        ),
    ]
