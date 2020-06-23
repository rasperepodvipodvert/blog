Title: Проверка отправки почты из bitrix
Date: 2020-06-17 10:40
Author: ifilatov
Tags: bitrix, howto
Slug: bitrix_sendmail
Status: published
Summary: Как проверить отправку почты из bitrixvm?

```php
<?php
if (mail("my_mail@mail.ru", "заголовок", "текст")) {
    echo 'Отправлено';
}
else {
    echo 'Не отправлено';
}
?>
```