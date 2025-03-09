#!/bin/bash


python3 manage.py migrate
python3 manage.py createcachetable
python3 manage.py collectstatic --noinput
python3 manage.py startup_check_accounts

if [ "$DEPLOY" = "TRUE" ]; then
    echo "------------------------------------------------------------------------------------"
    echo "DEPLOYMENT MODE"
    echo "------------------------------------------------------------------------------------"
    gunicorn --workers=9 core.wsgi --bind 0.0.0.0:8000 \
    --log-level=info --access-logfile '-' --error-logfile '-' \
    --access-logformat "%(m)s: %(U)s - %(s)s"
else
    echo "------------------------------------------------------------------------------------"
    echo "DEVELOPMENT MODE"
    echo "------------------------------------------------------------------------------------"
    gunicorn --workers=1 --threads=2 core.wsgi --bind 0.0.0.0:8000 \
    --log-level=info --access-logfile '-' --error-logfile '-' \
    --access-logformat "%(m)s: %(U)s - %(s)s" --reload
fi
