# Generated by Django 2.1.5 on 2019-03-08 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0007_auto_20190308_0916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buildingenergy',
            name='id',
        ),
        migrations.RemoveField(
            model_name='evenergy',
            name='id',
        ),
        migrations.RemoveField(
            model_name='fraserev',
            name='id',
        ),
        migrations.RemoveField(
            model_name='healthev',
            name='id',
        ),
        migrations.RemoveField(
            model_name='northev',
            name='id',
        ),
        migrations.RemoveField(
            model_name='roseev',
            name='id',
        ),
        migrations.AlterField(
            model_name='buildingenergy',
            name='timestamp',
            field=models.DateTimeField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='evenergy',
            name='timestamp',
            field=models.DateTimeField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fraserev',
            name='timestamp',
            field=models.DateTimeField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='healthev',
            name='timestamp',
            field=models.DateTimeField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='northev',
            name='timestamp',
            field=models.DateTimeField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='roseev',
            name='timestamp',
            field=models.DateTimeField(primary_key=True, serialize=False),
        ),
    ]
