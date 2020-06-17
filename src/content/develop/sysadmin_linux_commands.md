Title: Команды для linux сисадмина
Date: 2020-06-17 10:41
Author: ifilatov
Tags: linux, howto, best, devops
Slug: sysadmin_linux_commands
Status: published
Summary: Разные полезные команды для linux админов

```bash
# Показать всех кто коннектился по `ssh`
grep 'Connection closed' /var/log/secure |cut -d ' ' -f 9|sort|uniq -c|sort -n
```
