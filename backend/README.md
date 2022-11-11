# Backend Microservices

## Add new Microservice

### Init database
```
docker-compose exec postgres createdb <service-db> -U postgres
```

### Migration database
```
docker-compose exec <service-name> alembic upgrade head

docker-compose exec <service-name> alembic revision -m "message" --autogenerate
```

### Init data (Optional)
```
docker-compose exec <service-name> python init_data.py
```

### Freeze all package to requirements.txt
```
pip freeze > requirements.txt
```