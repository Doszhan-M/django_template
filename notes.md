docker exec -it trust_finance_backend-backend-1 bash 

python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py collectstatic --noinput
python manage.py collect_sitemap


django-admin startproject core
cd app
python manage.py startapp accounts

