Title: Настраиваем свой микротик на блокировку рекламы
Date: 2020-06-18 15:00
Author: ifilatov
Tags: routers, howto, best, internet, mikrotik
Slug: adguard_dns_mikrotik
Image: /media/adguard_dns.png
Status: published
Summary: Инструкция, как настроить mikrotik или любой другой роутер на блокировку рекламы

## DoH (DNS OVER HTTPS)

Чтобы настроить использование DoH нужно ввести следующие команды в консоле микротика:

```
# Установка NS CloudFlare для следующих действий
./ip dns set servers=1.1.1.1,1.0.0.1
# Синхронизируем время с time.cloudflare.com
./system ntp client set enabled=yes server-dns-names=time.cloudflare.com
# Качаем сертификат которым рым мы будем валидировать ответы от DNS
./tool fetch url=https://curl.haxx.se/ca/cacert.pem
# Импортируем его в систему
./certificate import file-name=cacert.pem passphrase=""
# Применяем DoH
./ip dns set use-doh-server=https://1.1.1.1/dns-query verify-doh-cert=yes
# Стираем нафиг обычные NS
./ip dns set servers=""
```

## Стандартный режим

> [AdGuard DNS](https://adguard.com/ru/adguard-dns/overview.html) – это альтернативный способ заблокировать рекламу, защитить личные данные и оградить детей от взрослых материалов. Он прост в настройке и использовании и обеспечивает необходимый минимум защиты от рекламы, трекинга и фишинга, независимо от платформы.

Настройка достаточно простая:

``` bash
# Прописываем эти DNS сервера на квладке IP > DNS > Servers
176.103.130.130
176.103.130.131
```

## Режим - Параноик

Более жесткую локировку позволяет сделать скрипт [MikroTik StopAD](https://stopad.hook.sh)

!!! info  
    Скрипт обновляется, у разработчика достаточно много подписчиков, что свидетельствует об интересе к проекту.
    Ресурс постоянно переезжает, а репозиторий нет, так что смотрите за обновлениями.
    В дополненеие к [AdGuard DNS](https://adguard.com/ru/adguard-dns/overview.html) сделал этот вариант, но отказался, т.к. нужны иногда и сервисы Microsoft и рекламные сети.
