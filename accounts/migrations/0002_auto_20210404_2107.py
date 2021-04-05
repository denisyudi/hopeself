# Generated by Django 3.1.7 on 2021-04-05 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('Confirmado', 'Confirmado'), ('Cancelado', 'Cancelado')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, null=True)),
                ('cpf', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('fone', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='medico',
            name='fone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]