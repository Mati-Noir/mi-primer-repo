# mi-primer-repo
Repositorio ejemplo clase 17 coderhouse python

## Mi primer commit remoto
esto es un commit remoto

# git init
# git remote add origin  + URL del repositorio (lo copio de github)  # - vincula el repositorio local con el remoto -#
# git pull
# git pull origin main  # Trae lo que tenga el remoto #
# git branch -M main  #-cambia el nombre de la branch que trae por defecto, en lugar de master se usa main ahora-#
# history  # veo el historial #
# git add README.md  # git add + nombre del archivo (readme en este caso, con terminacion .md) 
# git commit -m "esto es mi primer commit"
# git push -u origin main # con esto actualizo el readme de github con lo que tengo en mi archivo local #
# para lo anterior, probablemente me pida autorizacion en la web para sincronizar. una vez hecho, ya queda sincronizado


# Ahora soy yo mati, diciendote como tenes que arrancar para estas clases, asi cuando no revisan como arrancar, lo puedas ver aca:
# 1) para que funcione, primero en la terminal escribis " git init " , asegurandote de que inicie en la carpeta que estas trabajando.
# 2) para que arranque el servidor de la pagina de prueba " http://127.0.0.1:8000/ ", " python manage.py runserver " en la terminal
# 3) algunos de los comandos pueden ser: " http://127.0.0.1:8000/saludo_personalizado "
# 3,1) http://127.0.0.1:8000/saludar
# 3,2) para cerrar el servidor de la pagina, apretas CTRL + Pausa o sino cerra y volve a abrir la aplicacion.
# 3,3) en la seccion de urls, se encuentra las diferentes subpaginas, dentro de la pagina principal.

# Mas al final de la clase 18, el profe juega con el tema de los Class y Curso, entonces segun su modus operandi, seria realizar estos pasos:
# en la terminal: python manage.py shell
# from mi_app.models import Curso
# curso_1 = Curso(nombre="Python", camada=1)
# curso_1.save()
# Curso.objects.all()
# curso_1 = Curso(nombre="Python", camada=2)
# curso_1.save()
# Curso.objects.all()
# exit