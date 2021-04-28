Instruções para instalar a aplicação localmente.

Baixe o .zip da aplicação em https://github.com/denisyudi/hopeself

Linux (Ubuntu)

Assegure-se de ter o python instalado
$ python3 -V

Para instalar
$ sudo apt update
$ sudo apt -y upgrade
$ sudo apt install -y python3

Dentro da pasta onde ficará sua aplicação inicie o ambiente virtual de sua preferência. 
Aqui é utilizado o venv.
Para instalar o venv
$ sudo apt install -y python3-venv

Usando o venv
$ python3 -m venv seuAmbienteVirtual
$ source seuAmbienteVirtual/bin/activate

Agora com o ambiente virtual rodando:

Instale o pip
(seuAmbienteVirtual) $ sudo apt -y install python3-pip

Instale o Django e dependências

(seuAmbienteVirtual) $ pip3 install django==3.1.7
(seuAmbienteVirtual) $ pip3 install django-widget-tweaks==1.4.8

Criando o projeto
(seuAmbienteVirtual) $ django-admin startproject hopeself

Agora copie o conteudo da pasta hopeself-main para a pasta hopeself que foi criada. 
Assegure-se de estar na pasta hopeself onde se encontra o arquivo manage.py
(seuAmbienteVirtual) $ python3 manage.py runserver

Agora aparecerá um aviso dizendo que algumas migrações precisam ser efetuadas.
(seuAmbienteVirtual) $ python3 manage.py migrate

Rode novamente o servidor
(seuAmbienteVirtual) $ python3 manage.py runserver

Acesse em http://localhost:8000 ou http://127.0.0.1:8000


Para efetuar os teste
(seuAmbienteVirtual) $ python3 manage.py test accounts








Windows

Instale o python3 caso não tenha instalado.
https://python.org/downloads/

Para checar a instalação abra o CMD e digite:
python --version

Confira se o pip foi instalado junto com o python.
pip --version

Caso negativo, deverá instalá-lo.

Utilizando o pip instale o ambiente virtual de sua preferência. 
Aqui é utilizado o virtualenv
pip install virtualenv

Dentro da pasta onde ficará sua aplicação inicie o ambiente virtual.
virtualenv venv
source venv/bin/activate

Dentro do ambiente virtual instale o django e dependências
pip install django==3.1.7
pip install django-widget-tweaks==1.4.8

Confira se a instalação ocorreu com sucesso
django-admin --version

Criando o projeto
django-admin startproject hopeself

Agora copie o conteudo da pasta hopeself-main para a pasta hopeself que foi criada. 
Assegure-se de estar na pasta hopeself onde se encontra o arquivo manage.py

Rodando o servidor
django-admin manage.py runserver

Agora aparecerá um aviso dizendo que algumas migrações precisam ser efetuadas.
django-admin manage.py migrate

Rode o servidor novamente
django-admin manage.py runserver

Acesse a aplicação em http://127.0.0.1:8000





Para efetuar os teste
python3 manage.py test accounts