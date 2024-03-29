# Generated by Django 5.0.1 on 2024-02-01 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_id', models.CharField(max_length=255, unique=True)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=5000)),
                ('preco', models.CharField(max_length=255)),
                ('email_cliente', models.EmailField(max_length=254, null=True, unique=True)),
            ],
        ),
    ]
