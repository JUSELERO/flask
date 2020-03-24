# Proyecto Bases

Descripcion del proyecto
Integrado por Camilo Sanmiguel y Sebastina Leon

# Guia Git
#### Agregar al aera de staging
_Se Preparan los archivos nuevo o actualizados, para poder hacer commit_

`git add .`

#### Hacer Commit
_Se realiza commit del area de staging_

`git commit -m "mensaje"`

_Se agregar todos los archivos que previamente que han sido trackeados y luego se realiza commit_

`git commit -am "mensaje"`

#### Acualizar Repositorio Local
_Se realiza commit del area de staging_

`git pull origin master`

#### Acualizar Repositorio Remoto
_Se realiza commit del area de staging_

`git push origin master`

# Pasos 


Probado en Ubuntu 19.04

Instalar los siguientes programas

    ~# apt install git python3-pip mariadb-server mariadb-client python3.6-dev libmysqlclient-dev
    ~# pip3 install virtualenv

Clonar el repositorio

        con SSH
    ~$ git clone git@github.com:JUSELERO/flask.git

        con HTTPS
    ~$ git clone https://github.com/JUSELERO/flask.git

crear entorno virtual

    ~$ cd flask
    ~$ virtualenv -p python3 venv
	
        para iniciar el entorno virtual
		
	~$ source venv/bin/activate
	
		para desactivar el entorno virtual
		
	(venv) ~$ deactivate
	
Configurar entorno desarrollo
		
	~# pip install -r requirements.txt
	
	
Iniciar servidor
	
	 ~$ python3 main.py
	 
Documentacion	 
https://flask-mysqldb.readthedocs.io/en/latest/
