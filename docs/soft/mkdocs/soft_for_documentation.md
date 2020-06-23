Title: Софт для написания документации
Date: 2020-06-18 10:14
Author: ifilatov
Tags: soft, documentations, vscode, plugins
Status: published
Image: /media/600px-Visual_Studio_Code_1.35_icon.svg.png
Summary: Здесь собран софт, необходимый для написания документации.

## Принцип написания документации

- Все изменения конфигов должны попадать в [git](https://git-scm.com/)
- Документация серверов должна вестить от корня `/`

```bash
# Пример:
├── server.ru
│   ├── etc
│   │   ├── cron.d
│   │   │   ├── 0hourly
│   │   │   └── sysstat
│   │   ├── cron.daily
│   │   │   ├── etckeeper
│   │   │   └── logrotate
│   │   ├── cron.hourly
│   │   │   └── 0anacron
│   │   ├── crontab
│   │   ├── fail2ban
│   │   │   ├── filter.d
│   │   │   │   └── apache-badbots.conf
│   │   │   └── jail.conf
│   │   ├── goaccess.conf
│   │   ├── hosts
│   │   ├── nginx
│   │   │   ├── bx
│   │   │   │   ├── conf
│   │   │   │   │   ├── bitrix.conf
│   │   │   │   │   ├── ssl.conf
│   │   │   ├── nginx.conf
│   │   │   └── ssl
│   │   ├── passwd
│   │   ├── php.ini
│   │   ├── rc.local
│   │   ├── sudoers
│   │   ├── sysctl.conf
│   │   ├── vsftpd
```

- У каждого сервера в корне репозитория должен быть файл `readme.md` с документацией по данному серверу

## Программное обеспечение

Основной инструмент для написания документации это [VSCODE](https://code.visualstudio.com/)

#### Visual Studio Code Plugins

- [Auto MarkdownTOC](https://github.com/huntertran/markdown-toc) - для генерации содержания
- [Markdown All in One](https://github.com/yzhang-gh/vscode-markdown) - для подсветки синтаксиса и других полезных сценариев