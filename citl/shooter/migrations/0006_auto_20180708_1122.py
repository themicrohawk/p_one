# Generated by Django 2.0.5 on 2018-07-08 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooter', '0005_auto_20180706_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='week',
            field=models.IntegerField(choices=[(0, 'W0'), (1, 'W1'), (2, 'W2'), (3, 'W3'), (4, 'W4'), (5, 'W5'), (6, 'W6'), (7, 'W7'), (8, 'W8'), (9, 'W9'), (10, 'W10'), (11, 'W11'), (12, 'W12'), (13, 'W13'), (14, 'W14'), (15, 'W15')], default=0),
        ),
    ]
