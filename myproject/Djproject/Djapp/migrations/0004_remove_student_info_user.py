# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Djapp', '0003_student_info_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_info',
            name='user',
        ),
    ]
