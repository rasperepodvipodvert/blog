Title: Рецепты для 1С Bitrix
Date: 2020-06-19 10:40
Author: ifilatov
Tags: bitrix, howto, best
Slug: bitrix_recepts
Status: published
Image: /media/1cbitrix.png
Summary: Здесь лежат всякие ништяки по 1С Битрикс

## Инструменты

### Среда разработки

- [Инструменты для разработки под 1С-Битрикс](https://habr.com/en/sandbox/73214/). Здесь автор расказывает как правильно настроить среду разработки [PhpStorm](https://www.jetbrains.com/ru-ru/phpstorm/) и подключиться к проекту.

### Резервное копирование

Как показала практика, бэкапы битрикса лучше делать с помощью [Duplicati](https://www.duplicati.com/). Все прелести этого ПО я не буду описывать выделю лишь только то, что подходит для битрикса:

- [X] Хранение бэкапов в облаке
- [X] Шифрование бэкапов, а это значит можете хранить в любом облаке, даже не шипко защищенном
- [X] Автоматические действия до и после резервного копирования, на пример снять дамп БД перед резервным копирование
- [X] Уведомление о успешном/неуспешном резервном копировании

## Очистка кэша

- [Просто удаляете эту папку и битрикс потом сам пересоздаст кэш по мере потребления](https://qna.habr.com/q/564222)
- [Можно еще правильно настроить битрикс](https://iplogic.ru/baza-znaniy/ochistka-papki-upload-v-bitriks-cherez-agent/)

??? summary "code"
    ```bash
    rm -rf ./bitrix/upload/resize_cache
    ```

## Бэкап

> [Детальное описание](https://tuning-soft.ru/articles/bitrix/backup-bitrix.html) резервного копирования от другого автора, полезно к прочтению!

??? summary "Каталоги, которые можно исключить из бэкапа"
    !!! info
        Для версии битрикса < v12

    ```ini
    /bitrix/backup          # бэкапы самого битрикса
    /bitrix/cache           # неуправляемый кэш
    /bitrix/managed_cache   # управляемый кэш
    /bitrix/stack_cache     # файлы кэша с "вытеснением"
    /upload/resize_cache    # кэш ресайза изображений
    /bitrix/wizards         # мастера и демо-решения
    ```

## Права на файлы

??? summary "code"
    ``` shell
    find /var/www/test.com/public_html -type d -exec chmod 0770 {} \;
    find /var/www/test.com/public_html -type f -exec chmod 0660 {} \;
    ```
