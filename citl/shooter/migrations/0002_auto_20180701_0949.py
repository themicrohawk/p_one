# Generated by Django 2.0.5 on 2018-07-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='week',
            field=models.IntegerField(choices=[('W1', 'w1'), ('W2', 'w2'), ('W3', 'w3'), ('W4', 'w4'), ('W5', 'w5'), ('W6', 'w6'), ('W7', 'w7'), ('W8', 'w8'), ('W9', 'w9'), ('W10', 'w10'), ('W11', 'w11'), ('W12', 'w12'), ('W13', 'w13'), ('W14', 'w14'), ('W15', 'w15')]),
        ),
    ]
