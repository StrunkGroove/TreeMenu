# TreeMenu

create .env
docker-compose up --build
docker-compose up

docker-compose run web python manage.py makemigrations menu
docker-compose run web python manage.py migrate menu
sudo docker-compose run web python manage.py shell
exec(open('fill_db.py').read())
