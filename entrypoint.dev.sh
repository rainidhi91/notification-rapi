#!/bin/sh

ls -la

if [ "$DATABASE" = "postgres" ] || [ "$DATABASE" = "PSQL" ]
then
    echo "Waiting for postgres on $PSQL_HOST:$PSQL_PORT ..."

    while ! nc -z $PSQL_HOST $PSQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Collect static files
# echo "Flushing.."
# python manage.py flush --no-input

# Collect static files
# echo "Collect static files"
# python manage.py collectstatic --noinput

# # Make database migrations
# echo "Make database migrations"
# python manage.py makemigrations

# # Apply database migrations
# echo "Apply database migrations"
# python manage.py migrate

# # Create admin user if not created
# python initadmin.py

# Start server
# echo "Starting server"
# python manage.py runserver 0.0.0.0:8000

exec "$@"
