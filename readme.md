python manage.py  migrate -   update the database structure so it will correspond to models

python manage.py makemigrations goods -
Migrations for 'goods':
  goods\migrations\0001_initial.py
    - Create model Category
    - Create model Goods


python manage.py runserver -
You have 1 unapplied migration(s).

python  manage.py sqlmigrate goods 0001 -  change the database for goods table
python manage.py migrate -  applies the changes
python manage.py  shell -  python database shell
