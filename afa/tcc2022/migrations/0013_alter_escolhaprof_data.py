# Generated by Django 4.0.3 on 2022-06-28 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcc2022', '0012_alter_escolhaprof_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escolhaprof',
            name='data',
            field=models.DateTimeField(verbose_name='data'),
        ),
    ]
