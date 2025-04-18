#!/bin/sh

echo "waiting for MySQLl..."

while ! nc -z db 3306; do
    sleep 1
done

echo "MySQL is up - starting Django!"

exec "$@"