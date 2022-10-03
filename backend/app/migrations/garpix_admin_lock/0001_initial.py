# Generated by Django 3.1 on 2022-09-06 14:40

from django.db import migrations, models
import garpix_admin_lock.models.base_model


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatabasePageLockModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('url_parameters', models.CharField(blank=True, max_length=1024, null=True)),
                ('active', models.BooleanField(default=True)),
                ('user_reference', models.CharField(blank=True, max_length=255, null=True)),
                ('locked', models.BooleanField(default=True)),
                ('locked_at', models.DateTimeField(db_index=True)),
                ('locked_out', models.DateTimeField(db_index=True)),
                ('tab_counter', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Page Lock',
                'verbose_name_plural': 'Page Locks',
                'ordering': ('locked_at',),
            },
            bases=(garpix_admin_lock.models.base_model.BasePageLockModel, models.Model),
        ),
    ]
