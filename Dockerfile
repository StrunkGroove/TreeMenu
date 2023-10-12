FROM python:3
RUN apt-get update && apt-get install -y netcat
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/
CMD ["sh", "-c", "while ! nc -z db 5432; do sleep 1; done && python manage.py runserver 0.0.0.0:8000"]