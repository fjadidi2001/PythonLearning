1. django-admin startproject nameproject
2. python3 manage.py startapp nameapp
3. python3 manage.py makemigrations
4. python3 manage.py migrate
5. python3 manage.py createsuperuser
6.  {% %} return structure
7. {% endfor %}
8. you can add another column to main with ({{ }}) in addition you can use symbols to your 
data with (${{ }})
9. if you have multiple app you have create a directory in root and move base file in your template directory(in root) then you go to settngs
and change TEMPLATES 'DIRS':os.path.join(BASE_DIR, 'templates')