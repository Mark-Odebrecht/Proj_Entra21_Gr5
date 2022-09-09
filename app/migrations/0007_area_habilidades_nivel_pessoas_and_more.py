# Generated by Django 4.1 on 2022-08-29 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_empresas_cnpj'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('cpf', models.CharField(max_length=10, verbose_name='CPF')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereco')),
                ('data_nasc', models.CharField(max_length=10, verbose_name='Data de Nascimento')),
            ],
        ),
        migrations.AlterModelOptions(
            name='empresatamanho',
            options={'verbose_name': 'Tamanho da empresa', 'verbose_name_plural': 'Tamanho das empresas'},
        ),
        migrations.CreateModel(
            name='HabilidadexCandidatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tempo_experiencia', models.CharField(choices=[('a', '0-1 anos'), ('b', '2-3 anos')], max_length=1)),
                ('habilidade', models.ManyToManyField(to='app.habilidades')),
            ],
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('pessoas_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.pessoas')),
                ('perfil_linkedin', models.CharField(max_length=100, verbose_name='Linkedin')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.area', verbose_name='Area')),
                ('habilidades', models.ManyToManyField(to='app.habilidadexcandidatos')),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nivel', verbose_name='Nivel')),
            ],
            bases=('app.pessoas',),
        ),
    ]
