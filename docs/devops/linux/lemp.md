Title: Настройка LEMP - краткая инструкция
Date: 2020-10-29 10:41
Author: ifilatov
Tags: linux, howto, best, devops, lemp, nginx, php-fpm
Slug: lemp_for_bitrix
Status: published
Summary: Инструкция по настройке LEMP для bitrix

## Ссылки по теме

## Настройка php-fpm

```bash
sudo groupadd site1
sudo useradd -g site1 site1
sudo passwd site1
sudo mkdir /var/www/site1
sudo chown site1:site1 -R /var/www/site1
```


??? note "/etc/php/7.3/fpm/pool.d/site1.conf"
    ```ini
    [site1]                                     # идентификатор сайта
    user = site1                                # пользователь в linux
    group = site1                               # группа пользователя
    listen = /var/run/php5-fpm-site1.sock       # расположение сокета который прослушивает php-fpm 
    listen.owner = www-data                     # пользователь от которого запущен nginx
    listen.group = www-data                     # группа от которого запущен nginx
    php_admin_value[disable_functions] = exec,passthru,shell_exec,system
    php_admin_flag[allow_url_fopen] = off
    pm = dynamic
    pm.max_children = 5
    pm.start_servers = 2
    pm.min_spare_servers = 1
    pm.max_spare_servers = 3
    chdir = /
    ```

??? note "/etc/php/7.3/fpm/php.ini"

    ```ini
    [php]
    short_open_tag = On
    display_errors = On
    error_log = "/var/log/php/error.log"
    error_reporting = E_ALL
    log_errors = On
    display_startup_errors = On
    cgi.fix_pathinfo = 0
    date.timezone = "Europe/Moscow"
    mbstring.func_overload = 2
    mbstring.internal_encoding = "UTF-8"
    max_input_vars = 10000
    post_max_size = 1024M
    memory_limit = 256M
    upload_max_filesize = 1024M
    
    [opcache]
    opcache.revalidate_freq = 0
    opcache.validate_timestamps = 1
    opcache.max_accelerated_files = 100000
    opcache.memory_consumption = 512
    opcache.interned_strings_buffer = 64
    opcache.fast_shutdown = 1
    opcache.error_log = "/var/log/php/opcache.log"
    
    [xdebug]
    xdebug.remote_host = "192.168.0.2"
    xdebug.remote_port = 9000
    xdebug.auto_trace = 0
    xdebug.default_enable = 1
    xdebug.idekey = "PhpStorm"
    xdebug.max_nesting_level = 250
    xdebug.profiler_enable = 0
    xdebug.profiler_enable_trigger = 0
    xdebug.profiler_output_dir = "/tmp/"
    xdebug.profiler_output_name = "cachegrind.out.%H%R"
    xdebug.remote_enable = 1
    ```

## Настройка nginx

??? note "/etc/nginx/sites-available/site1.conf"

    ```nginx
    server {
        listen 80;
        listen [::]:80;
        root /var/www/site1;
        index index.php index.html index.htm;
        server_name site1.ru;
        
        upstream php-fpm {
            server unix:/var/run/php5-fpm-site1.sock; # путь до сокета php-fpm конкретного сайта
        }
    
        if (!-e $request_filename) {
           rewrite  ^(.*)$  /bitrix/urlrewrite.php last;
        }
    
        location @bitrix {
            include snippets/fastcgi-php.conf;
            fastcgi_pass php-fpm;
            fastcgi_param SCRIPT_FILENAME $document_root/bitrix/urlrewrite.php;
            }
    
        location ~ \.php$ {
            if (!-f $request_filename) {
              rewrite  ^(.*)/index.php$  $1/ redirect;
            }
            include fastcgi_params;
            fastcgi_pass php-fpm;
            fastcgi_index index.php;
            fastcgi_send_timeout 21600;
            fastcgi_read_timeout 21600;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        }
    
        location = /restore.php {
            include fastcgi_params;
            fastcgi_pass php-fpm;
            fastcgi_index index.php;
            fastcgi_send_timeout 21600;
            fastcgi_read_timeout 21600;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
            client_body_buffer_size 1024m;
            client_max_body_size 1024m;
        }
    
        location ~ /upload/ {
            client_body_buffer_size 1024m;
            client_max_body_size 1024m;
        }
    
        location = /favicon.png {
            log_not_found off;
            access_log off;
        }
    
        location = /robots.txt {
            log_not_found off;
            access_log off;
        }
    
        location ~* ^.+\.(jpg|jpeg|gif|png|svg|js|css|mp3|ogg|mpe?g|avi|zip|gz|bz2?|rar|eot|otf|ttf|woff|woff2)$ {
            log_not_found off;
            access_log off;
            expires 30d;
            add_header Cache-Control public;
        }
    
        location ~ (/bitrix/modules|/upload/support/not_image|/bitrix/php_interface|local/modules|local/php_interface) {
            deny all;
        }
    
        location ~ /.git/ {
            deny all;
        }
    
        location ~ /vendor/ {
            deny all;
        }
    
        location ~ /composer {
            deny all;
        }
    
        location ~ /.gitignore {
            deny all;
        }
    
        error_page 404 /404.html;
    
        location /404.html {
    
        }

    }
    ```

