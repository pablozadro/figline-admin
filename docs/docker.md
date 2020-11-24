# Docker

In production, Django gonna use Docker containers: 

- `mysql:8` Docker image for the database
- `python:3` Docker image for Django and Python server

## Db Service

Build and keep running the `db` service in the background:

```bash
docker-compose up -d --build db
```

Enter the container to give user permissions to test database:

```bash
docker exec -it figline_db bash
mysql -u root -p # use credential in .env
```

```bash
# SELECT User, Host, Password FROM mysql.user; 
# i.e: GRANT ALL PRIVILEGES ON figline_test.* TO 'figline'@'%';
ALTER USER 'figline'@'%' IDENTIFIED WITH mysql_native_password BY '***';
GRANT ALL PRIVILEGES ON [MYSQL_DATABASE_TEST].* TO '[MYSQL_USER]'@'%';
FLUSH PRIVILEGES;
```


## Web Service

Build and keep running the `web` service:

```bash
# For developement workflow the --build is optional
docker-compose up --build web
```

Enter the container and create the superuser:

```bash
docker exec -it figline_web bash
cd project
python manage.py createsuperuser
```