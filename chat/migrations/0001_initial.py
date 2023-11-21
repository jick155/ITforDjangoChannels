# Generated by Django 4.2.5 on 2023-09-30 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=30)),
                ('exchange', models.CharField(max_length=30)),
                ('market', models.CharField(max_length=30)),
                ('industry', models.CharField(max_length=30)),
                ('isnormal', models.BooleanField()),
                ('isattention', models.BooleanField()),
                ('isdisposition', models.BooleanField()),
                ('ishalted', models.BooleanField()),
                ('symbol', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]