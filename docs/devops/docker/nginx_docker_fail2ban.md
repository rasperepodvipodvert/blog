Title: fail2ban для nginx в докере
Date: 2020-08-18 11:40
Author: ifilatov
Tags: idea, howto, tasks
Status: published
Summary: Здесь я расскажу, как настроить fail2ban если ваше приложение в docker

# fail2ban для nginx в докере

Если вы, так же как и я, используете docker для публикации своих приложений в production, то наверняка хотите их защитить с помощью fail2ban от подбора паролей и черезмерной активности!
Дак вот если все делать по мануалам из интернета - ничего у вапс не получится, а все потому, что iptables (ufw, firewalld) в linux с установленным docker окружением работают несколько иначе!

## Конфиги


```ini
[nginx-badbots]
enabled  = true
port     = http,https
filter   = nginx-badbots
chain    = DOCKER-USER
logpath  = /docker/logs/nginx/*ccess.log
maxretry = 1
findtime = 604800
bantime  = 604800
```