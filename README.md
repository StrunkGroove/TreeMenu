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

# Make the wait-for-it.sh script executable
```
chmod +x ./wait-for-it.sh
```
# Build and run the Docker containers
```
docker-compose up --build
```

# Run Django database migrations and create a superuser
```
docker-compose run web python manage.py makemigrations menu
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```

# Enter Django shell to execute fill_db.py script
```
docker-compose run web python manage.py shell
exec(open('fill_db.py').read())
```
Test!
