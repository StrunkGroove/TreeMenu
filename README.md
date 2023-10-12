# TreeMenu

nano .env  
chmod +x ./wait-for-it.sh  
docker-compose up --build  

docker-compose run web python manage.py makemigrations menu  
docker-compose run web python manage.py migrate  
docker-compose run web python manage.py createsuperuser  
docker-compose run web python manage.py shell  
exec(open('fill_db.py').read())  

Test!
