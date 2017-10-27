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

python3 medical_prescription/manage.py makemigrations
python3 medical_prescription/manage.py migrate
python3 medical_prescription/manage.py runserver 0.0.0.0:8000
