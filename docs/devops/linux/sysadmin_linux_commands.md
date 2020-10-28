Title: Команды для linux сисадмина
Date: 2020-06-17 10:41
Author: ifilatov
Tags: linux, howto, best, devops
Slug: sysadmin_linux_commands
Status: published
Summary: Разные полезные команды для linux админов

## Ссылки по теме

- [Полезные команды на одном листе](https://www.f-notes.info/linux:linux_command)
- [[Шпаргалка] Разведка и аудит сервера](https://codeby.net/threads/shpargalka-razvedka-i-audit-servera.63524/)

## Поиск

```sh
find /usr/bin -type f -mtime -1 # найти измененные файлы за сутки
```

## Работа с текстом

#### Показать всех кто коннектился по `ssh`

```bash
grep 'Connection closed' /var/log/secure |cut -d ' ' -f 9|sort|uniq -c|sort -n
```

## Рецепты

??? summary "Проверка водящих подключений к системе."

    ```sh
    lsof -i
    lsof -i :80
    grep 80 /etc/services
    netstat -antup
    netstat -antpx
    netstat -tulpn
    chkconfig --list
    chkconfig --list | grep 3:on
    last
    w
    ```
## Docker

### Portainer

> Инструмент администрирования Docker и Swarm

```bash
docker volume create portainer_data
docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
```

## iptables

```bash
# Блокировка IP через iptables
iptables -A INPUT -s 212.116.121.83 -j DROP
# Разблокировка IP через iptables 
iptables -D INPUT -s 212.116.121.83 -j DROP
```

## journalctl

```bash
# Показать ошибки
journalctl -p err

# Показать логи в реальном времени
journalctl -f

# Логи за определенную дату
journalctl --since=2016-12-20
journalctl --since=2016-12-20 --until=2016-12-21

# Лог конкретного сервиса
journalctl -b -u zabbix-agent.service

```

## logrotate

Эта служба необходима для того, чтобы архивировать старые логи или удалять их с какой-то переодичностью.
Базовые настройки хранятся здесь: ''/etc/logrotate.conf''

Пример ротации конкретного файла:

```bash
/var/log/fail2ban.log {

weekly        # ротация раз в неделю. Возможные варианты daily, weekly, monthly, size (например size=1M)
rotate 4      # сохраняется последние 4 ротированных файла
compress      # сжимать ротируемый файл

delaycompress # сжимать предыдущий файл при следующей ротации
missingok     # отсутствие файла не является ошибкой
postrotate    # скрипт будет выполнен сразу после ротации
fail2ban-client set logtarget /var/log/fail2ban.log /dev/null
endscript

# If fail2ban runs as non-root it still needs to have write access
# to logfiles.
# create 640 fail2ban adm
create 640 root adm # сразу после ротации создать пустой файл с заданными правами и пользователем
}
```

Для немедленного применения изменений можно выполнить:

```bash
''$ logrotate /etc/logrotate.conf''
```

Для проверки внесенный изменений можно запустить команду (никаких действий с логами не будет выполнено):

```bash
''$ logrotate -d /etc/logrotate.conf''

```

## goaccess

### ссылки

- [Настройка goaccess и формата логов](https://root.sysmerge.it/2018/01/goaccess.html)