# desafio-dev
Sistema que importa arquivo txt com dados, ordena os dados e lista ordenadamente as operações de transações financeiras efetuadas em diferentes lojas.

Para usar: 
Clique em Importar e carregue o arqquivo .txt
Clique em Listar Transações para ver os dados de transações já importados e normalizados.

O backend é Python + Django, tem um frontend em react que é uma view que lista dados que vêm da api que está no backend.


# Sistema (Backend)
Python 3.9

# Sistema (FrontEnd)
React 17.0.2

# Instalação
Se tem alguma pasta com o nome venv apague antes de criar um novo.

Crie e active um ambiente virtual:

pip install virtualenv


Criar:
virtualenv env

Ativar:
source env/bin/activate    (Linux ou macOS)
env/Scripts/Activate    (Windows)

# Lista de pacotes a serem intalados.
asgiref==3.4.1

beautifulsoup4==4.9.3

certifi==2021.5.30

charset-normalizer==2.0.2

Django==3.2.8

django-bootstrap-form==3.4

django-bootstrap4==3.0.1

django-cors-headers==3.10.0

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



# Instando os pacotes necessários (Backend)
Os pacotes a serem instalados também podem ser encontrados no arquivo requirements.txt

No diretório onde se encontra o arquivo requirements.txt execute:
pip install -r requirements.txt

# Instando os pacotes necessários (FrontEnd)
Os pacotes a serem instalados também podem ser encontrados no arquivo package.json

Vá até ao diretório onde se encontra o arquivo  package.jsone execute:
npm install package-lock.json

# Usando o Sistema (BackEnd)
python manage.py runserver
iniciar o server em 127.0.0.1:8000

# Usando o Sistema
npm start
iniciar o server em localhost:3000/

# Dados de autenticação
Usuário: admin.
Senha: 123456.

# Links para a API:
127.0.0.1:8000/api
127.0.0.1:8000/api/transacoes-lista/

# Link o front frontend em React que consome do backend 127.0.0.1:8000/api/transacoes-lista/
localhost:3000/
