=====================================================
 GUIA DE IMPLANTAÇÃO NA VPS (DJANGO + MYSQL)
=====================================================

1. CRIAR O BANCO DE DADOS NO MYSQL DA VPS:
-----------------------------------------------------
Acesse o MySQL e execute:
   CREATE DATABASE hugel_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

2. CONFIGURAR O AMBIENTE VIRTUAL E DEPENDÊNCIAS:
-----------------------------------------------------
No terminal da VPS, dentro da pasta do projeto:
   python3 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt

3. CONFIGURAR AS VARIÁVEIS DE AMBIENTE:
-----------------------------------------------------
   cp .env.example .env
   nano .env   (Preencha com a senha do MySQL e o IP/Domínio da VPS)

4. APLICAR MIGRAÇÕES E IMPORTAR OS DADOS (JSON -> MYSQL):
-----------------------------------------------------
   python manage.py migrate
   python manage.py loaddata dados.json

5. ARQUIVOS ESTÁTICOS E ACESSO ADMIN:
-----------------------------------------------------
   python manage.py collectstatic
   python manage.py createsuperuser

6. RODAR A APLICAÇÃO:
-----------------------------------------------------
   gunicorn core_project.wsgi:application --bind 0.0.0.0:8000