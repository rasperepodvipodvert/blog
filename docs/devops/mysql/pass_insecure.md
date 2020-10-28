title: [Warning] Using a password on the command line interface can be insecure.

## mysqldump: [Warning] Using a password on the command line interface can be insecure.

```sh
# Сохраняем логин и пароль от БД в надежном хранилище
mysql_config_editor set --login-path=local --host=localhost --user=username --password

# Теперь используем для доступа к базе эти сохраненные данные
mysqldump --login-path=local db_name

# Логинимся в mysql используя сохраненные данные
mysql --login-path=local

# Смотрим, какие данные сохранены
mysql_config_editor print --login-path=local
```