# Generated by Django 2.2.7 on 2019-11-12 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20191112_2318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ('-versions_thread', '-version')},
        ),
        migrations.AddField(
            model_name='page',
            name='is_current',
            field=models.BooleanField(default=True),
        ),
    ]
