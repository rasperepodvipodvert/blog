title: mysql_user

# Не очевидные моменты работы с MySQL

```yaml
- name: Генерируем факт, что пароль у нас такой, и используем его дальше
  set_fact: db_password={{db.password}}

- name: "Удаление базы данных {{db.name}}"
  mysql_db:
    login_user: root
    login_password: "{{db.root_password}}"
    login_host: "{{db.host}}"
    name: "{{db.name}}"
    state: absent

- name: "Создание базы данных {{db.name}}"
  mysql_db:
    login_user: root
    login_password: "{{db.root_password}}"
    login_host: "{{db.host}}"
    name: "{{db.name}}"
    encoding: "utf8"
    state: present

- name: "Удаление пользователя {{db.user}}"
  mysql_user:
    login_user: root
    login_password: "{{db.root_password}}"
    login_host: "{{db.host}}"
    name: "{{db.user}}"
    host_all: yes
    state: absent

- name: "Создание пользователя {{db.user}} {{db_password}}"
  mysql_user:
    login_user: root
    login_password: "{{db.root_password}}"
    login_host: "{{db.host}}"
    name: "{{db.user}}"
    password: "{{ db_password }}"
    update_password: on_create
    priv: '{{db.name}}.*:ALL'
    state: present
    host: '%'
  no_log: no
```