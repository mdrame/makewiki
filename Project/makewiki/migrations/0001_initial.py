# Generated by Django 2.2.6 on 2019-11-16 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('authur', models.CharField(max_length=300)),
                ('body', models.TextField()),
            ],
        ),
    ]
