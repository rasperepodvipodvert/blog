Title: Команды для linux сисадмина
Date: 2020-06-17 10:41
Author: ifilatov
Tags: linux, howto, best, devops
Slug: sysadmin_linux_commands
Status: published
Summary: Разные полезные команды для linux админов

## Ссылки по теме

- [Полезные команды на одном листе](https://www.f-notes.info/linux:linux_command)

## Работа с текстом

#### Показать всех кто коннектился по `ssh`

```bash
grep 'Connection closed' /var/log/secure |cut -d ' ' -f 9|sort|uniq -c|sort -n
```
## iptables

```bash
# Блокировка IP через iptables
iptables -A INPUT -s 212.116.121.83 -j DROP
# Разблокировка IP через iptables 
iptables -D INPUT -s 212.116.121.83 -j DROP
```