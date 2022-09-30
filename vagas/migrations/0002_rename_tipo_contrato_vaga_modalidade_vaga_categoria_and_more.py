# Generated by Django 4.1.1 on 2022-09-30 14:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaga',
            old_name='tipo_contrato',
            new_name='modalidade',
        ),
        migrations.AddField(
            model_name='vaga',
            name='categoria',
            field=models.CharField(choices=[('full_stack', 'Full-Stack'), ('front_end', 'Front-End'), ('back_end', 'Back-End'), ('mobile', 'Mobile')], max_length=10, null=True, verbose_name='Categoria'),
        ),
        migrations.AddField(
            model_name='vaga',
            name='contrato',
            field=models.CharField(choices=[('estagio', 'Estágio'), ('pj', 'PJ'), ('clt', 'CLT')], max_length=7, null=True, verbose_name='Contrato'),
        ),
        migrations.AddField(
            model_name='vaga',
            name='data',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Data de criação:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vaga',
            name='beneficios',
            field=models.TextField(max_length=500, verbose_name='Benefícios'),
        ),
    ]
