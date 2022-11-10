# Generated by Django 4.1.1 on 2022-11-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0002_alter_habilidade_habilidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculo',
            name='cep',
            field=models.CharField(max_length=9, null=True, verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='curriculo',
            name='cpf',
            field=models.CharField(max_length=14, null=True, verbose_name='CPF'),
        ),
        migrations.AddField(
            model_name='curriculo',
            name='data_nasc',
            field=models.DateField(max_length=10, null=True, verbose_name='Data de Nascimento'),
        ),
        migrations.AddField(
            model_name='curriculo',
            name='descricao',
            field=models.TextField(blank=True, help_text='Resumo do seu perfil profissional em no máximo 300 caracteres.', max_length=300, null=True, verbose_name='Descrição'),
        ),
        migrations.AddField(
            model_name='curriculo',
            name='facebook',
            field=models.CharField(blank=True, help_text='URL do seu perfil no Facebook', max_length=100, null=True, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='curriculo',
            name='github',
            field=models.CharField(blank=True, help_text='URL do seu perfil no GitHub', max_length=100, null=True, verbose_name='GitHub'),
        ),
        migrations.AddField(
            model_name='curriculo',
            name='instagram',
            field=models.CharField(blank=True, help_text='URL do seu perfil no Instagram', max_length=100, null=True, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='curriculo',
            name='linkedin',
            field=models.CharField(blank=True, help_text='URL do seu perfil no LinkedIn', max_length=100, null=True, verbose_name='Linkedin'),
        ),
        migrations.AddField(
            model_name='curriculo',
            name='nome',
            field=models.CharField(max_length=50, null=True, verbose_name='Nome'),
        ),
        migrations.AddField(
            model_name='curriculo',
            name='sobrenome',
            field=models.CharField(max_length=50, null=True, verbose_name='Sobrenome'),
        ),
    ]