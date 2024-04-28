@ECHO OFF 
:: Activate Virtual Env.
ECHO Activando entorno virtal
CALL .venv\Scripts\activate
::RUN server
ECHO Ejecutando servidor
PYTHON -m flask --app run run
PAUSE