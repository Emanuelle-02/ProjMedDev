# Generated by Django 4.1.3 on 2022-11-07 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entregas',
            name='status',
            field=models.CharField(choices=[('EM ANDAMENTO', 'EM ANDAMENTO'), ('ENTREGUE', 'ENTREGUE'), ('CANCELADA', 'CANCELADA')], default=2, max_length=150),
            preserve_default=False,
        ),
    ]
