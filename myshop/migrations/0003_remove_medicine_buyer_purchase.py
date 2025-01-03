# Generated by Django 5.1.2 on 2024-10-24 04:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0002_alter_medicine_buyer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='buyer',
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.buyer')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.medicine')),
            ],
        ),
    ]
