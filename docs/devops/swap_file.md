Title: Включаем SWAP в файл
Date: 2020-06-22 10:41
Author: ifilatov
Tags: linux, howto, best, devops, swap
Slug: swap_to_file
Image: /media/swap_to_file.jpg
Status: published
Summary: Иногда полезно иметь `swap` в файле на сервере, на пример на купленной VPS на которой мало RAM


Чтобы включить swap в файл делаем следующее:

```bash
sudo dd if=/dev/zero of=/var/swapfile bs=1M count=2048              # создаем пустой файл нужного обьема, в данном случае 2ГБ
sudo chmod 600 /var/swapfile                                        # меняем права
sudo mkswap /var/swapfile                                           # включаем своп
echo /var/swapfile none swap defaults 0 0 | sudo tee -a /etc/fstab  # добавляем в автомонтирование при старте системы
sudo swapon -a                                                      # проверяем, все ли ок
```
