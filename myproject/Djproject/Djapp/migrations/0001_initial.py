# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('addr', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
    ]
