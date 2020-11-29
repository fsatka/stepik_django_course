set -e

python manage.py makemigrations
python manage.py migrate

python load_data_to_db.py
