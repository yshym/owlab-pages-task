# Generated by Django 2.2.7 on 2019-11-12 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20191112_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='versions_thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pages', to='pages.VersionsThread'),
        ),
    ]
