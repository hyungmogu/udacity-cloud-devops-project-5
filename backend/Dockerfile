# Set the base image
FROM php:8.1-fpm-alpine

# Install system dependencies and PHP extensions
RUN apk update && apk add --no-cache \
    build-base \
    git \
    curl \
    libpng-dev \
    libzip-dev \
    oniguruma-dev \
    zlib-dev \
    && docker-php-ext-install pdo_mysql mbstring zip gd

# Install Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Set the working directory
WORKDIR /var/www

# Copy the application files
COPY ./main /var/www

# Install application dependencies
RUN composer install --optimize-autoloader --no-dev

# Set the correct permissions
RUN chown -R www-data:www-data /var/www && chmod -R 755 /var/www

# Expose the necessary ports
EXPOSE 8000

# Start the PHP-FPM server
CMD ["php", "-S", "0.0.0.0:8000", "-t", "public/"]
