#!/bin/sh

# wait for Postgres to start
postgres_ready(){
python << END
import sys
import psycopg2
try:
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="", host="db")
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
echo "Delete migrations"
find . -path "*/migrations/*.pyc"  -delete
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
echo "Delete old staticfiles dir"
find . -path "*/staticfiles/*"  -delete
echo "Create makemigrations and migrate"
python3 medical_prescription/manage.py makemigrations
python3 medical_prescription/manage.py migrate
echo "Load all datas"
python3 medical_prescription/manage.py loaddata dataFinal.json
echo "Collecting static"
python3 medical_prescription/manage.py collectstatic
echo "Run server"
python3 medical_prescription/manage.py runserver 0.0.0.0:8000 & .
./node_modules/.bin/gulp default
