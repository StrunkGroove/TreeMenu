# TreeMenu

In the task, Materialized Path was used.


For start:  
nano .env  
```
SECRET_KEY=mysecretkey
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

POSTGRES_DB=mydatabase
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
POSTGRES_PORT=5432
```

chmod +x ./wait-for-it.sh  
docker-compose up --build  

docker-compose run web python manage.py makemigrations menu  
docker-compose run web python manage.py migrate  
docker-compose run web python manage.py createsuperuser  
docker-compose run web python manage.py shell  
exec(open('fill_db.py').read())  

Test!
