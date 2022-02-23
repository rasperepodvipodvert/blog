Title: Софт для написания документации
Date: 2020-06-18 10:14
Author: ifilatov
Tags: soft, documentations, vscode, plugins
Status: published
Summary: Здесь собран софт, необходимый для написания документации.

## Принцип написания документации

- Все изменения конфигов должны попадать в [git](https://git-scm.com/)
- Документация серверов должна вестить от корня {++/++}

??? summary "Пример"
    ```
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

Основной инструмент для создания Markdown файлов, это [VSCODE](https://code.visualstudio.com/)

### Visual Studio Code Plugins

- [Auto MarkdownTOC](https://github.com/huntertran/markdown-toc) - для генерации содержания
- [Markdown All in One](https://github.com/yzhang-gh/vscode-markdown) - для подсветки синтаксиса и других полезных сценариев

### MkDocs

Данный инструмент я использую для ведения документации, которую необходимо потом передать заказчику.

#### Плагины

##### [awesome-pages](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin)

Плагин MkDocs, упрощает настройку заголовков страниц и их порядка
Awesome-pages позволяет настраивать отображение навигации без необходимости настраивать полную структуру меню в вашем `mkdocs.yml`
Все это делается с помощью небольшого файла конфигурации, который находится непосредственно в соответствующем каталоге вашей документации. Очень удобно!

!!! note "Этот плагин работает без `nav` или `pages` файле mkdocs.yml. Поддерживается и `nav`, но вы можете не получить ожидаемых результатов, особенно если ваша структура навигации не соответствует структуре файла."

Установка:

```sh
pip install mkdocs-awesome-pages-plugin
```

Добавте это в `mkdocs.yml`

```yaml
plugins:
    - search
    - awesome-pages
```

Использование:

Просто создаем файл `.pages` в директории где хотим использовать плагин и пишем в него параметры

```sh
collapse_single_pages: true # Не будет показываться название директории, в место него будет показан заголовок первого `md` файла в каталоге
collapse: true              # Запрещает/разрешает сворачивание раздела
hide: true                  # Скрывает директорию
```


#### Ссылки

- [Mkdocs Material](https://squidfunk.github.io/mkdocs-material/) - mkdocs с темой оформления material

#### Deploy документации в GitHub

??? summary "deploy.bat"

    !!! info "В данном примере используются два репозитория `origin`, `gh-pages` и branch `gh-pages` для публичного репозитория"

    ``cmd
    set OUTPUTDIR=site
    set GITHUB_PAGES_REMOTE=gh-pages
    set GITHUB_PAGES_BRANCH=gh-pages
    mkdocs gh-deploy -m "Generate MkDocs site" -r %GITHUB_PAGES_REMOTE% -b %GITHUB_PAGES_BRANCH% -d %OUTPUTDIR% --force
    rd site /S /Q
    ``

### [Obsidian](Obsidian.md)
