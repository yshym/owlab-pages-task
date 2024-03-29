# Generated by Django 2.2.7 on 2019-11-12 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20191112_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='VersionsThread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='versions_thread',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pages', to='pages.VersionsThread'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together={('versions_thread', 'version')},
        ),
        migrations.RemoveField(
            model_name='page',
            name='thread_id',
        ),
    ]
