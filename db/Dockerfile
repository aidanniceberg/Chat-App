FROM mysql:latest

WORKDIR /db

# run create.sql on init
ADD ./migrations/create.sql /docker-entrypoint-initdb.d/
