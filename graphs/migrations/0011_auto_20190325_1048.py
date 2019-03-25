# Generated by Django 2.1.5 on 2019-03-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0010_buildingdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='WestEVFuture',
            fields=[
                ('timestamp', models.DateTimeField(primary_key=True, serialize=False)),
                ('value', models.FloatField()),
                ('maxerr', models.FloatField()),
                ('minerr', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='buildingdata',
            name='value',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='buildingenergy',
            name='value',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='evenergy',
            name='value',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='fraserev',
            name='value',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='healthev',
            name='value',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='northev',
            name='value',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='powerdata',
            name='Power',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='roseev',
            name='value',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='westev',
            name='value',
            field=models.FloatField(),
        ),
    ]
