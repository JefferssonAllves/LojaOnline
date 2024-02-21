# Generated by Django 5.0.1 on 2024-02-01 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='grupo',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='email_cliente',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]