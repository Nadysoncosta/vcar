# Generated by Django 4.1.7 on 2023-03-07 22:59

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel', '0003_alter_aluguel_codigo_alter_aluguel_data_aluguel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='codigo',
            field=models.BigAutoField(default='', primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='cpf_cliente',
            field=models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to='aluguel.cliente'),
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='placa_carro',
            field=models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to='aluguel.carro'),
        ),
        migrations.AlterField(
            model_name='carro',
            name='placa',
            field=models.CharField(max_length=15),
        ),
    ]