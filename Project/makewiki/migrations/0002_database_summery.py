# Generated by Django 2.2.6 on 2019-11-16 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makewiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='summery',
            field=models.CharField(default='This is the summery', max_length=300),
            preserve_default=False,
        ),
    ]