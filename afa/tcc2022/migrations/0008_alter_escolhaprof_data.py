# Generated by Django 4.0.3 on 2022-06-28 02:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcc2022', '0007_alter_escolhaprof_data_alter_escolhaprof_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escolhaprof',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 28, 2, 43, 45, 214153), verbose_name='data'),
        ),
    ]