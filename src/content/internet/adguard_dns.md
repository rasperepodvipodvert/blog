Title: Настраиваем свой микротик на блокировку рекламы
Date: 2020-06-18 15:00
Author: ifilatov
Tags: routers, howto, best, internet, mikrotik
Slug: adguard_dns_mikrotik
Image: /media/adguard_dns.png
Status: published
Summary: Инструкция, как настроить mikrotik или любой другой роутер на блокировку рекламы

> [AdGuard DNS](https://adguard.com/ru/adguard-dns/overview.html) – это альтернативный способ заблокировать рекламу, защитить личные данные и оградить детей от взрослых материалов. Он прост в настройке и использовании и обеспечивает необходимый минимум защиты от рекламы, трекинга и фишинга, независимо от платформы.

Настройка достаточно простая:

```ini
# Прописываем эти DNS сервера на квладке IP > DNS > Servers
176.103.130.130
176.103.130.131
```

Пользуюсь уже неделю, [uBlock Origin](https://ru.wikipedia.org/wiki/UBlock_Origin) можно не ставить, защищает все устройства в сети!
