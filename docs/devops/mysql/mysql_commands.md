title: Полезные команды MYSQL

# Полезные команды MYSQL

## Пользователь

??? summary "Показать права пользователя `user`"
    ```mysql
    SHOW GRANTS FOR 'user'@'%';
    ```
??? summary "Установить права для пользователя `user`"
    ```mysql
    ALTER USER 'user'@'%' IDENTIFIED BY 'p@sSwOrD';
    ```

## База данных

??? summary "Создать БД в кодировке utf8mb4_unicode_ci"
    ``` mysql
    create database IF NOT EXISTS db.name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    ```