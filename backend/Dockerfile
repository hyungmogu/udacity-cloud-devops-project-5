# based on https://dev.to/jackmiras/laravel-with-php7-4-in-an-alpine-container-3jk6
FROM php:8.2-fpm-alpine3.16

WORKDIR /var/www/

# Essentials
RUN echo "UTC" > /etc/timezone
RUN apk add --no-cache zip unzip curl sqlite nginx supervisor

# Installing bash
RUN apk add bash
RUN sed -i 's/bin\/ash/bin\/bash/g' /etc/passwd

# Installing composer
RUN curl -sS https://getcomposer.org/installer -o composer-setup.php
RUN php composer-setup.php --install-dir=/usr/local/bin --filename=composer
RUN rm -rf composer-setup.php

# Install application dependencies
COPY ./main .
RUN composer install --no-dev
RUN chown -R nobody:nobody /var/www/storage

# Configure nginx
COPY .docker/nginx.conf /etc/nginx/
COPY .docker/nginx-laravel.conf /etc/nginx/modules/

RUN mkdir -p /run/nginx/
RUN touch /run/nginx/nginx.pid

RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 8000