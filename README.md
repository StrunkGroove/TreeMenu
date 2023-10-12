# TreeMenu

create .env
docker-compose up --build
docker-compose up

sudo docker-compose run web python manage.py makemigrations
sudo docker-compose run web python manage.py migrate
sudo docker-compose run web python manage.py shell
exec(open('fill_db.py').read())
