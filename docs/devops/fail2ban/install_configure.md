Title: Установка и конфигурирование fail2ban
Date: 2020-09-03 8:00
Author: ifilatov
Tags: linux, howto, best, devops, fail2ban
Slug: fail2ban_install_configure
Status: published
Summary: Записки для правильного конфигурирования fail2ban

## Установка/обновление

!!! info "Одназначно, если fail2ban работает у вас на `Python2` переводите его на `Python3`, в разы быстрее"

### CentOS and RHEL 7

```sh
yum install yum-plugin-copr epel-release
yum update
yum install fail2ban
```

### Debian/ubuntu

```sh

```

### дальше для всех

```sh
git clone https://github.com/fail2ban/fail2ban.git
cd fail2ban
sudo python setup.py install 
```

## Доп. настройки

### sshd_config

```sh
LogLevel VERBOSE
```

### jail.local

```ini
[sshd]
enabled = true
filter = sshd[mode=aggressive]
action = iptables-allports
logpath = /var/log/auth.log 
maxretry = 1
bantime = 2w
findtime = 1d
ignoreip = 127.0.0.1/8
```

## Проверка работы

### Firewalld

```sh
firewall-cmd --direct --get-all-rules
fail2ban-client version
```

## Iptables

```sh
iptables -L -n |less
```