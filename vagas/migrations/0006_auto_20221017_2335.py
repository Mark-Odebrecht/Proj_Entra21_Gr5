# Generated by Django 4.1.1 on 2022-10-18 02:35

from django.db import migrations
from candidatos.models import Habilidade
from vagas.models import Vaga
#nome, categoria, nivel, descriçao, modalidade, contrato, jornada, local,
# outras_reg, requisitos, salmin, salmax, benefícios, data, pri_habilidade_vaga,
#seg_habilidade_vaga, ter_habilidade_vaga, qua_habilidade_vaga, qui_habilidade_vaga,
#usuario

# DEFAULT_VAGAS = [
#     ('Programador back-end', 'Back-end', 'Junior','criação de modelos de dados', 'Presencial', 'CLT', 'Período Integral', 'Blumenau', 'nao', 'Python, Django, SQL, Git/GitHub', 2500.00,3800.00,'Vale transporte, Plano de saúde, Plano odontológico, Vale Refeição.', 208,'','','','',1)
#     ]

# lista =[]

# lista.append(Vaga('Programador back-end', 'Back-end', 'Junior','criação de modelos de dados', 'Presencial', 'CLT', 'Período Integral', 'Blumenau', 'nao', 'Python, Django, SQL, Git/GitHub', 2500.00,3800.00,'Vale transporte, Plano de saúde, Plano odontológico, Vale Refeição.', 208,'','','','',1))




def criar_vagas(apps,schema_editor):
    DEFAULT_VAGAS = [
        ('Programador back-end', 'Back-end', 'Junior','criação de modelos de dados', 
        'Presencial', 'CLT', 'Período Integral', 'Blumenau', 'nao',
         'Python, Django, SQL, Git/GitHub', 2500.00,3800.00,
        'Vale transporte, Plano de saúde, Plano odontológico, Vale Refeição.', 208,'','','','',1),
        ('Dev React', 'Front-end', 'Sênior', 'Implementar telas com HTML5 e CSS; Desenvolver aplicação em React;',
         'Remoto', 'CLT', 'Período Integral', 'Blumenau', 'sim', 
         'Experiência como desenvolvedor de software (+5 anos); Bom conhecimento em testes unitários / funcionais / integração;', 8000.00, 12000.00, 'Vale-transporte, Plano de Saúde, Participação nos lucros',
         94,'','','','',2), 
        ('Desenvolvedor(a) Python Júnior', 'Back-end', 'Junior', 'Experiência de pelo menos 6 meses', 'Presencial', 'PJ','Período Integral','Blumenau','nao',
        'Sólidos conhecimentos em: Python 3 e ecossistema (pip/ env/ etc), Resolução de problemas, Programação orientada a objetos, Bancos de dados relacionais (SQL), Git/Github/Gitlab',
         2500.00, 3500.00, 'Vale-transporte, Plano de Saúde, Participação nos lucros', 208, 44,'','','',3),
        (
            'Desenvolvedor(a) Pleno PHP/Laravel/Symfony', 'Back-end', 'pleno', 
            'Disponibilidade Full-Time', 'Híbrido', 'CLT', 'Período Integral', 'Blumenau',
            'sim', 'Experiencia previa de pelo menos 2 anos de desenvolvimento em Laravel e/ou Symfony, Formação em ensino superior, Inglês Intermediário (Eliminatorio); Experiência com ferramentas de versionamento de código (GIT,...); Habilidades interpessoais de escrita e de comunicação verbal; Experiência em desenvolvimento de APIs baseados em startdards da industria, Conhecimento em metodologias ágeis (Scrum/Kanban);',
            9000.00, 11000.00, 'Vale-transporte, Plano de Saúde, Participação nos lucros', 189, '','','','',4
        ),
        (
            'Desenvolvedor(a) Front-end React Pleno', 'Front-end', 'pleno',
            'Serão exigidos conhecimentos de bons padrões de desenvolvimento, para que os sistemas evoluam de forma saudável. Esta vaga é para PJ com um modelo totalmente remoto, mas buscamos uma interação diária por meio de nossas plataformas de comunicação.',
            'Híbrido', 'PJ', 'Período Integral', 'Blumenau', 'nao', 
            'Esses são os requisitos técnicos para esta vaga: ReactJs, TypeScript, Redux, Styled-Components, JavaScript, Context API, Next, HTML, CSS, GIT',
            7000.00,9000.00, 'Aniversário-off, Vale-transporte, Plano de Saúde, Participação nos lucros', 94, '', '', '', '', 5
        ),
        (
            'Desenvolvedor(a) Back End - React Native', 'Back-end', 'junior', ' Realizar a manutenção e criação de novas funcionalidades;', 'Presencial',
            'CLT', 'Período Integral', 'Blumenau', 'nao', 
            'Conhecimentos/experiências essenciais: Node.js, JavaScript/TypeScript, MongoDB, REST APIs, Conhecimentos desejáveis:  Test-driven development (ts-mocha)',
            1200.00, 2000.00, 'Plano odontológico, Vale-transporte, Plano de Saúde, Participação nos lucros', 94, '','','','',6
        ),
        (
            'Desenvolvedor(a) Python Sênior - Inglês Falando','Back-end', 'Sênior', 'Experiência de pelo menos 36 meses comprovada', 'Remoto', 'PJ', 'Período Integral', 
            'Blumenau', 'sim', 'Inglês fluente, python avançado', 20000.00, 23000.00, 'Vale-transporte, Plano de Saúde, Participação nos lucros', 208,44,'','','',7
        ),
        (
            'Desenvolvedor(a) Phyton Junior', 'Back-end', 'Junior',
            ' Você vai trabalhar em um projeto greenfield de forma totalmente remota. Por isso, você precisa saber trabalhar de forma autônoma. Porém você contará com um profissional Sênior para, eventualmente, auxiliar nas tarefas.',
            'Remoto', 'CLT', 'Período Integral', 'Blumenau', 'nao', 'Sólidos conhecimentos em: Python 3 e ecossistema (pip/ env/ etc), Django e/ou Flask, Git/Github/Gitlab, Agile/SCRUM', 
            4000, 5500, 'GymPass, Vale-transporte, Plano de Saúde, Participação nos lucros', 208,'','','','',8
        ),
        (
            'DESENVOLVEDOR(A) FULL STACK JÚNIOR', 'Full-stack', 'Junior', 
            'A DG Solutions está crescendo e queremos profissionais de alta performance e engajamento para fazer parte da equipe, sendo assim, estamos em busca de um DESENVOLVEDOR FULL STACK JÚNIOR para nos ajudar com as atividades.',
            'Remoto', 'CLT', 'Período Integral', 'Blumenau', 'sim', 
            'CONHECIMENTOS NECESSÁRIOS: PHP (Lavarel), API Rest, GIT, Python, MySQL, Desenvolvimento Ágil (Scrum e Kanban) - DIFERENCIAL: Ambiente Linux, Node',
            6000,8500,'Vale-transporte, Plano de Saúde, Participação nos lucros', 208, '','','','',9
        ),
        (
            'Desenvolvedor(a) Python + PostgreSQL', 'Back-end', 'Pleno', 'Se você quer crescer na sua carreira, nós temos a oportunidade certa pra você.',
            'Híbrido', 'CLT', 'Período Integral', 'Blumenau', 'sim', 'Python Avançado, banco dados relacional', 
            4000, 5500, 'Plano de Saúde, PPR, Day Off', 208, '','','','',10
        ),
        (
            'Desenvolvedor(a) Sênior', 'Full-stack', 'Sênior', 
            'Buscamos um profissional que tenha amplos conhecimentos e esteja disposto a enfrentar novos desafios.',
            'Presencial', 'CLT', 'Período Integral', 'Blumenau', 'nao', 'CSS, HTML, Git, Python', 6000, 8500,
            'Vale-transporte, Plano de Saúde, Participação nos lucros', 208, '','','','', 11
        ),
        (
            'Desenvolvedor(a)Angular', 'Front-end', 'Pleno', 
            'Essa vaga é para você que não tem experiência. Necessita lógica de programação e ínicio em qualquer linguagem. Cuidaremos do seu aprendizado prévio a execução das funções.', 
            'Remoto','PJ', 'Período Integral', 'Blumenau', 'nao', 'Java, Angular', 4000, 5500,
            'Vale Refeição, Vale Alimentação,  Vale Transporte,  Seguro de Vida, Benefício mensal: R$ 1.300,00.', 11, '','','','',11
        ),
        (
            'Junior Frontend', 'Front-end', 'Junior', 'Necessário conhecimento em HTML e CSS.', 
            'Presencial', 'CLT', 'Período Integral', 'Blumenau', 'nao', 'CSS, HTML, Git', 
            1800,2600, 'Auxilio Educação, Vale-Alimentação, PPR', 37, 94, 79, '','', 3
        )
        
        
    ]


    vaga = apps.get_model('vagas','Vaga')
    for nome, categoria, nivel, descricao, modalidade, contrato, jornada, local, outras_reg,requisitos,salmin,salmax,beneficios,pri,seg,ter,qua,qui,usuario_id in DEFAULT_VAGAS:
        vaga.objects.create(
            nome = nome,
            categoria = categoria,
            nivel = nivel,
            descricao = descricao,
            modalidade = modalidade,
            contrato = contrato,
            jornada = jornada,
            local = local,
            outras_reg = outras_reg,
            requisitos = requisitos,
            salmin = salmin,
            salmax = salmax,
            beneficios = beneficios,
            pri_habilidade_vaga_id = pri,
            seg_habilidade_vaga_id = seg,
            ter_habilidade_vaga_id = ter,
            qua_habilidade_vaga_id = qua,
            qui_habilidade_vaga_id = qui,
            usuario_id = usuario_id
            )

class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0005_auto_20221017_1737'),
    ]

    operations = [
        migrations.RunPython(criar_vagas)
    ]