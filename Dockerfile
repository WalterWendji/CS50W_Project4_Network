FROM python:3
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    default-libmysqlclient-dev \ 
    build-essential
RUN pip install -r requirements.txt

CMD ["./wait-for-db.sh", "python3", "manage.py", "runserver", "0.0.0.0:8000"]