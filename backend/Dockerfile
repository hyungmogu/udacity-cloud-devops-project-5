# Set the base image
FROM php:8.0-fpm-alpine

# Install system dependencies and PHP extensions
RUN apk update && apk add --no-cache \
    build-base shadow nginx \
    postgresql-dev libzip-dev zlib-dev oniguruma-dev \
    && docker-php-ext-install pgsql pdo_pgsql mbstring zip \
    && apk del build-base postgresql-dev libzip-dev zlib-dev

# Create a user and set permissions
RUN usermod -u 1000 www-data && groupmod -g 1000 www-data \
    && chown -R www-data:www-data /var/www \
    && chmod -R 775 /var/www/storage /var/www/bootstrap/cache

# Configure nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Set the working directory
WORKDIR /var/www

# Copy the application files
COPY --chown=www-data:www-data ./main /var/www

# Install composer
COPY --from=composer:2 /usr/bin/composer /usr/bin/composer
RUN composer install --no-dev --optimize-autoloader

# Expose the necessary ports
EXPOSE 80

# Start nginx and php-fpm
CMD ["sh", "-c", "nginx && php-fpm"]