@ECHO OFF

CALL .\venv\Scripts\activate.bat
cd gbshop
python manage.py runserver
