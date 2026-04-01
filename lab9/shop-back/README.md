# Online Shop — Lab 9
venv\Scripts\activate
py -m pip install -r requirements.txt 
python manage.py makemigrations api
python manage.py migrate

# (for admin)
python manage.py createsuperuser
python manage.py seed_data
python manage.py runserver

# Admin
`http://127.0.0.1:8000/admin/` 

# Add item
python manage.py shell -c "
from api.models import Category, Product
c1 = Category.objects.create(name='Electronics')
c2 = Category.objects.create(name='Clothing')
Product.objects.create(name='', price=, description='', count=, is_active=, category=)

