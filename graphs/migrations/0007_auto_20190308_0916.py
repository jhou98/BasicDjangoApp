# Generated by Django 2.1.5 on 2019-03-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0006_delete_evdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='westev',
            name='id',
        ),
        migrations.AlterField(
            model_name='westev',
            name='timestamp',
            field=models.DateTimeField(primary_key=True, serialize=False),
        ),
    ]
