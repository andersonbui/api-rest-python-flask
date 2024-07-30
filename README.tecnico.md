## Compose sample application
### Python/Flask application with Nginx proxy and a Mongo database

Project structure:
```
./
├── app
│   ├── api.py
│   ├── db
│   │   ├── data_storage.py
│   │   └── mongodb.py
│   ├── __init__.py
│   ├── extractores
│   │   ├── ExtractorCSV.py
│   │   ├── ExtractorFabrica.py
│   │   ├── ExtractorFile.py
│   │   ├── ExtractorFileStrategy.py
│   │   └── ExtractorJSONL.py
│   └── services
│       ├── apis_request
│       │   ├── base_api_clients.py
│       │   ├── categories_api_client.py
│       │   ├── currencies_api_client.py
│       │   ├── items_api_client.py
│       │   └── users_api_client.py
│       ├── data_enricher.py
│       └── procesar_archivo.py
├── docker-compose-dev.yml
├── Dockerfile
├── pruebas.http
├── README.md
├── requirements.txt
├── run.py
├── start-dev.sh
├── tests

```


## Despliegue con docker compose para desarrollo

### actualizar variables de entorno
usar el archico ".env.example" para crear su archivo personalizado ".env"

### instalar docker
Si no tiene docker puede instalarlo mediante el siguiente comando en una consola linux. Para otro tipo de sistema operativo por favor dirigirse a la documentación [https://docs.docker.com/desktop/install/windows-install/](oficial de docker) 
```bash
curl -L https://get.docker.com | bash -
```

Definición de archivo tipo "docker compose" para despliegue de la aplicación de entorno de desarrollo (Solo para desarrollo):
[docker-compose-dev.yml](docker-compose-dev.yml)
```bash
services:
  backend:
    build: flask
    ...
  mongo:
    image: mongo
    ...
```

## Ejecutar el servicio en desarrollo
Puede usar el anterior archivo "docker-compose-dev.yml" para ejecutar un entorno de desarrollo o pruebas de este servicio web. **Atención!!** No es recomendable para un entorno de producción.

Usar el siguiente comando para para ejecutar el servicio mendiante docker compose:

```bash
docker compose -f docker-compose-dev.yml up -d
```

El archivo Compose define una aplicación con dos servicios: "backend" y "mongo".
Al lanzar la aplicación, Docker Compose levanta el servicio de mongodb en el puerto 27017 sin autenticacion, y el servicio de api rest en el puerto 5000.

Asegúrese de que el puerto 5000 del host no esté siendo utilizado por otro contenedor o servicio; de lo contrario, se debe cambiar el puerto en el archivo .env

## Expected result

Listing containers must show three containers running and the port mapping as below:
```
$ docker ps
CONTAINER ID        IMAGE                        COMMAND                  CREATED             STATUS              PORTS                  NAMES
dba87a080821        nginx-flask-mongo_backend   "./server.py"            About a minute ago   Up About a minute                          nginx-flask-mongo_backend_1
d7eea5481c77        mongo                       "docker-entrypoint.s…"   About a minute ago   Up About a minute   27017/tcp              nginx-flask-mongo_mongo_1
```

### Ejecucion sin docker compose
Si tiene instalado python y un entonro virtual con venv puede ejecutar Flask directamente mediente su CLI:

```bash
source ./venv/bin/activate
. .env
flask --app app run --debug --host 0.0.0.0
```
pero va a necesitar ejecutar la base de datos mongodb manualmente con docker compose con el comando:
```bash
docker compose -f docker-compose-dev.yml up mongo -d
```

## Peticiones de prueba
En el archivo "pruebas.http" se encuentran dos ejemplos de comandos curl para enviar archivo hacia el servicio web. Estos comando curl ejecutarlos en una consola linux, no funciona el envío de archivos si lo ejecuta directamente sobre el entorno de desarrollo como vscode, que permite ejecutar dichos comandos directamente sobre el archivo mediante un click. La ruta de los archivos del comando curl es relativa a la maquina donde se este ejecutando dicho comando, asi que, **NO olvidar** actualizar la ruta de los archivos en el comando curl en cuestión.

Ejemplo de peticion curl:
```bash
curl --request POST --url http://localhost:5000/api/v1/cargar_datos_archivo \
    --header 'Content-Type: multipart/form-data' \
    --form files=@/opt/projects/prefect/ejemplo_flask/data_mini.csv
```


### Otras opciones de ejecucion

levantar servicio con comando "docker compose"
```bash
$ docker compose -f docker-compose-dev.yml up -d
```

volver a levantar solo backend
```bash
docker compose -f docker-compose-dev.yml up backend --build -d
```

ejecutar analisis lintter 
https://pylint.readthedocs.io/en/latest/user_guide/configuration/index.html
```bash
docker compose -f docker-compose-dev.yml exec backend pylint --recursive=y app
```

### otras opciones
eliminar archivos temporales:
```bash
find . -regex '^.*\(__pycache__\|\.py[co]\)$' -delete
```

Para remover los contenedores de creados mediante "docker compose", ejecutar:
```
docker compose down
```


