python manage.py  migrate -   update the database structure so it will correspond to models

python manage.py makemigrations goods -
Migrations for 'goods':
  goods\migrations\0001_initial.py
    - Create model Category
    - Create model Goods


python manage.py runserver -
You have 1 unapplied migration(s).

python manage.py makemigrations good
python  manage.py sqlmigrate good 0001 -  change the database for goods table
python manage.py migrate -  applies the changes

Django database API
python manage.py  shell -  python database shell
from goods.models import Category, Goods
b = Category()
b.name = "Shoes"
b.description = "Shoes and accessories"
b.save()

b = Category.objects.all()   - get all categories
b = Category.objects.get(pk=1)  - get category with the primary key equal to 1
b = Category.objects.filter(name__startswith='Com')


cat.good_set.all()

Computer Logo
https://image.freepik.com/free-icon/open-laptop-computer-with-pixel-boxes_318-39349.jpg
Shoes logo
https://image.flaticon.com/icons/svg/1077/1077995.svg
Books logo
http://icons.iconarchive.com/icons/double-j-design/ravenna-3d/256/Book-icon.png
Kitchen
https://previews.123rf.com/images/iconcraftstudio/iconcraftstudio1603/iconcraftstudio160300615/54206702-k%C3%BCche-symbol-der-gekreuzten-messer-und-gabel.jpg
Home Appliances
https://vision.com.bd/storage/uploads/fullsize/2018-05/home-app.png
