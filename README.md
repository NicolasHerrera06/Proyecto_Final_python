# Proyecto Final curso de CoderHouse "Python"

Este es el proyecto final del curso de Python de la plataforma CoderHouse realizado por los estudiantes Nicolás Herrera, Nicolás Keiniger, Nicolás Yunes el cual consistia en realizar crear una web similar a un blog que contenga un CRUD  el módulo de Login. 

## Requisitos base

Los requisitos base serán parte de los criterios de evaluación para aprobar el proyecto.

●	Inicio: Al momento de ingresar a la app en la ruta base ‘/’

●	Visualizar el home del blog.

●	Poder listar todas las páginas del blog, poder ver en detalle cada una, poder crear, editar o borrar páginas del blog.

●	Las páginas están formadas por un título, un contenido en editor de texto avanzado (ckeditor por ejemplo), una imagen, fecha de posteo de la imagen.

●	Tener una app de registro donde se puedan registrar usuarios en el route accounts/signup, un usuario está compuesto por: email - contraseña - nombre de usuario

●	Tener una app de login en el route accounts/login/ la cual permite loggearse con los datos de administrador o de usuario normal.

●	Tener una app de perfiles en el route accounts/profile/ la cual muestra la info de nuestro usuario y permite poder modificar y/o borrar: imagen - nombre - descripción -  un link a una página web - email y contraseña

●	Contar con un admin en route admin/ donde se puedan manejar las apps y los datos en las apps.

●	Tener una app de mensajería en el route messages/ para que los perfiles se puedan contactar entre sí.

## Comenzando 🚀

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

https://github.com/Skullby/CoderFinal.git


### Pre-requisitos 📋

Para instalar el software y como instalarlas python 3 y Django.

```
pip install Django
```

### Instalación 🔧

Descargarse el proyecto del repositorio https://github.com/Skullby/CoderFinal.git

copiar la ruta de acceso de la carpeta Blog

Modificar en setting.py, en TEMPLATES, DIR modificar la ruta por la ruta de acceso copiada en el paso anterior.

correr en la terminal:  python3 manage.py runserver

Abrir en un navegador la url: http://127.0.0.1:8000/ 


## Ejecutando las pruebas ⚙️

Los casos de pruebas realizados se pueden observar en el documento "Especificación_Casos_Prueba.xlsx"


## Construido con 🛠️

Las herramientas que se utilizaron para crear este  proyecto fueron:

* [Python](https://www.python.org/) - El framework web usado
* [Django](https://www.djangoproject.com/) - El framework web usado


## Autores ✒️

* **Nicolas Yunes** - *Trabajo Inicial* - (https://github.com/Skullby/)
* **Nicolas Keiniger** - *Modificaciones Trabajo* - (https://github.com/nicolaskeiniger)
* **Nicolás Herrera** - *Documentación* - (https://github.com/NicolasHerrera06)
