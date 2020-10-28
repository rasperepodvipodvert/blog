Title: Включаем SWAP в файл
Date: 2020-06-22 10:41
Author: ifilatov
Tags: linux, howto, best, devops, swap
Slug: swap_to_file
Image: /media/swap_to_file.jpg
Status: published
Summary: Иногда полезно иметь `swap` в файле на сервере, на пример на купленной VPS на которой мало RAM


## Включение
Чтобы включить swap в файл делаем следующее:

```bash
sudo dd if=/dev/zero of=/var/swapfile bs=1M count=2048              # создаем пустой файл нужного обьема, в данном случае 2ГБ
sudo chmod 600 /var/swapfile                                        # меняем права
sudo mkswap /var/swapfile                                           # включаем своп
echo /var/swapfile none swap defaults 0 0 | sudo tee -a /etc/fstab  # добавляем в автомонтирование при старте системы
sudo swapon -a                                                      # проверяем, все ли ок
```

## Тюнинг

!!! info "Модернизацией этих параметров я добился снижения потребления оперативки на своем zabbix сервере, что позволит запихнуть в него еще какое-то количество метрик!"

```sh
# С какого момента используем swap 100%-90% = после использования 10% оперативки
sysctl vm.swappiness=90
# Сохраняем чтобы применялось после перезагрузки
echo 'vm.swappiness=90' | tee -a /etc/sysctl.d/swap.conf

# Чем меньше параметр, тем больше используется swap
sysctl vm.vfs_cache_pressure=50
vm.vfs_cache_pressure = 50

# Сохраняем чтобы применялось после перезагрузки
echo 'vm.vfs_cache_pressure=50' | tee -a /etc/sysctl.d/swap.conf


# Устанавливаем zram - систему сжатия памяти
# Debian 9 - добавляем в /etc/apt/sources.list
# deb  http://deb.debian.org/debian stretch main contrib non-free
# deb-src  http://deb.debian.org/debian stretch main contrib non-free
apt install linux-image-extra-virtual zram-config

```