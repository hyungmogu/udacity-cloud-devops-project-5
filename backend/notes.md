# Notes

## 1) Installation

## 2) Logging into Laravel container

```
docker exec -it my-container-name /bin/bash
```

**Example**
```
docker exec -it backend-myapp-1 /bin/bash
```

## 3) Checking Laravel version

```
php artisan --version
```

## 4) Creating Controller using Bitnami Laravel Container

```
docker-compose exec <service> <command>
```

**Example**

```
docker-compose exec myapp php artisan make:controller UserController
```
