echo "Delete migrations"
find . -path "*/migrations/*.pyc"  -delete
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
echo "Create makemigrations and migrate"
python3 medical_prescription/manage.py makemigrations
python3 medical_prescription/manage.py migrate
