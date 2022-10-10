# Generated by Django 4.1.1 on 2022-10-08 04:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidatos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Exemplo: "Desenvolvedor Web"', max_length=100, verbose_name='Nome da Vaga')),
                ('categoria', models.CharField(choices=[('Full-stack', 'Full-Stack'), ('Front-end', 'Front-end'), ('Back-end', 'Back-end'), ('Mobile', 'Mobile')], max_length=10, null=True, verbose_name='Categoria')),
                ('nivel', models.CharField(choices=[('Junior', 'Junior'), ('Pleno', 'Pleno'), ('Sênior', 'Sênior')], max_length=6, verbose_name='Nível da Vaga')),
                ('descricao', models.TextField(help_text='Resumo da vaga de emprego e funções exercidas em no máximo 500 caracteres.', max_length=500, verbose_name='Descrição da vaga')),
                ('modalidade', models.CharField(choices=[('Presencial', 'Presencial'), ('Híbrido', 'Híbrido'), ('Remoto', 'Remoto')], max_length=10, null=True, verbose_name='Modalidade da Vaga')),
                ('contrato', models.CharField(choices=[('Estágio', 'Estágio'), ('CLT', 'CLT'), ('Freelance', 'Freelance'), ('PJ', 'PJ'), ('Voluntário', 'Voluntário')], max_length=15, null=True, verbose_name='Contrato')),
                ('jornada', models.CharField(choices=[('Período Integral', 'Período Integral'), ('Meio Preíodo', 'Meio Período')], max_length=30, null=True, verbose_name='Jornada')),
                ('local', models.CharField(help_text='Onde reside sua empresa, para vagas presenciais. Para trabalho remoto, use "Online".', max_length=30, verbose_name='Local da Vaga')),
                ('outras_reg', models.CharField(choices=[('sim', 'Sim'), ('nao', 'Não')], max_length=3, verbose_name='Aceita candidatos de outras regiões?')),
                ('requisitos', models.CharField(help_text='Exemplos: "Formação em nível superior", "Tecnólogo", etc.', max_length=50, verbose_name='Requisitos')),
                ('salmin', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Salário Mínimo')),
                ('salmax', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Salário Máximo')),
                ('beneficios', models.TextField(help_text='Exemplos: "Vale refeição", "Plano de saúde", etc.', max_length=500, verbose_name='Benefícios')),
                ('data', models.DateField(auto_now_add=True, verbose_name='Data de criação:')),
                ('pri_habilidade_vaga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pri_habilidade_vaga+', to='candidatos.habilidade', verbose_name='1ª - Habilidade')),
                ('qua_habilidade_vaga', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pri_habilidade_vaga+', to='candidatos.habilidade', verbose_name='4ª - Habilidade')),
                ('qui_habilidade_vaga', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='pri_habilidade_vaga+', to='candidatos.habilidade', verbose_name='5ª - Habilidade')),
                ('seg_habilidade_vaga', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pri_habilidade_vaga+', to='candidatos.habilidade', verbose_name='2ª - Habilidade')),
                ('ter_habilidade_vaga', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pri_habilidade_vaga+', to='candidatos.habilidade', verbose_name='3ª - Habilidade')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Vaga',
                'verbose_name_plural': 'Vagas',
            },
        ),
    ]
