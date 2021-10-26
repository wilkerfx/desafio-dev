# desafio-dev
Sistema que importa arquivo txt com dados, ordena os dados e lista ordenadamente as operações de transações financeiras efetuadas em diferentes lojas.
Pacotes usados e necessários para configurar o sistema.
Primeiro efectue o Login.
Usuário: admin.
Senha: 123456.
Segundo Cique em Importar e carregue o arqquivo .txt.
Terceiro cique em Listar Transações para ver os ddos já importados normalizados.

Base de dados usada é PostgreSQL.


# Lista de pacotes a serem intalados.

asgiref==3.4.1
beautifulsoup4==4.9.3
certifi==2021.5.30
charset-normalizer==2.0.2
Django==3.2.8
django-bootstrap-form==3.4
django-bootstrap4==3.0.1
django-crispy-forms==1.13.0
djangorestframework==3.12.4
idna==3.2
numpy==1.21.0
pandas==1.3.0
postgres==4.0
psycopg2==2.9.1
psycopg2-binary==2.9.1
psycopg2-pool==1.1
python-dateutil==2.8.1
pytz==2021.1
readchar==3.0.4
requests==2.26.0
six==1.16.0
soupsieve==2.2.1
sqlparse==0.4.2
urllib3==1.26.6


Os pacotes também podem ser encontrados na pasta do projeto no ficheiros requirements.tx

Pode instalar os pacotes necessários no terminal com os commandos:

Gere um arquivo de requisitos e, em seguida, instale-o em outro ambiente:
Windows.
env\bin\python -m pip install -r requirements.txt

Unix/MacOS.
env/bin/python -m pip install -r requirements.txt

API Endpoint:
/api/
/api/transacoes-lista/
api/transacoes-detalhe/
api/transacoes-criar/



