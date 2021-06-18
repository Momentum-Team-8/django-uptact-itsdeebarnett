# Generated by Django 3.2.4 on 2021-06-17 21:28

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 6, 17, 21, 28, 18, 697414, tzinfo=utc))),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.note'),
        ),
    ]
