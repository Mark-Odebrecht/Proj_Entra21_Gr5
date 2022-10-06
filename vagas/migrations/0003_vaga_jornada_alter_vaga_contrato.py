# Generated by Django 4.1.1 on 2022-10-04 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vagas", "0002_rename_tipo_contrato_vaga_modalidade_vaga_categoria_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="vaga",
            name="jornada",
            field=models.CharField(
                choices=[
                    ("integral", "Período Integral"),
                    ("meio-preiodo", "Meio Período"),
                ],
                max_length=30,
                null=True,
                verbose_name="Jornada",
            ),
        ),
        migrations.AlterField(
            model_name="vaga",
            name="contrato",
            field=models.CharField(
                choices=[
                    ("estagio", "Estágio"),
                    ("clt", "CLT"),
                    ("freelance", "Freelance"),
                    ("pj", "PJ"),
                    ("voluntario", "Voluntário"),
                ],
                max_length=15,
                null=True,
                verbose_name="Contrato",
            ),
        ),
    ]
