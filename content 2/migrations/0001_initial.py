# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('subtitle', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='content.Content')),
                ('text', models.TextField()),
            ],
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='content.Content')),
                ('path', models.FileField(upload_to=None)),
            ],
            bases=('content.content',),
        ),
        migrations.AddField(
            model_name='contributor',
            name='content1',
            field=models.ManyToManyField(related_name='contributor', to='content.Content', blank=True),
        ),
        migrations.AddField(
            model_name='content',
            name='contributors',
            field=models.ManyToManyField(related_name='content', to='content.Contributor'),
        ),
    ]
