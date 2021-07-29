Title: Установка HomeAssistant на виртуалку - краткая инструкция
Date: 2020-12-27 15:00
Author: ifilatov
Tags: howto, hass
Slug: hass_install
Status: published
Summary: Установка HomeAssistant на виртуалку - краткая инструкция

## Подготовка системы

- Устанавливаем конетейнер `debian-10-standard_10.7-1_amd64.tar.gz`
- Ставим статический IP обязательно! Он же контроллер, не должен зависеть от вашегно роутера...
- Авторизация в системе по ssh ключу, нафиг эти пароли
- Ставим рускую локаль `dpkg-reconfigure locales`
- Ставим правильную таймзону `dpkg-reconfigure tzdata`
- Обновляем систему `apt update && apt upgrade -y`

## Установка

- Ставим софт ориентируясь на [инструкцию](https://www.home-assistant.io/docs/installation/raspberry-pi/)

- Поскольку виртуалка чисто под hass отдельного пользователя не создаем
- Все операции выполняю изпод `root`
- Виртуальное окружение ставить то же не будем, ибо вся виртуалка под hass

```sh
# Дополненные мной команды для установки всех компонентов homeassistant
apt-get install python3 python3-pkgconfig python3-dev python3-venv python3-pip libffi-dev libssl-dev libjpeg-dev zlib1g-dev autoconf build-essential libopenjp2-7 libtiff5 ffmpeg libavformat-dev libavdevice-dev mc tmux
python3 -m pip install wheel av
pip3 install homeassistant
```

## Автозапуск через systemd

```ini
[Unit]
Description=Home Assistant
After=network-online.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/.homeassistant
ExecStart=/usr/local/bin/hass -c "/root/.homeassistant"
ExecReload=/bin/kill -HUP $MAINPID
KillMode=process
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

## Обновление python

```shell
# качаем свежий python
wget https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz
tar -zxf Python-3.9.5.tgz
cd Python-3.9.5/
# подготавливаем сборку
./configure --enable-optimizations
make -j 2 # собираем на 2-х ядрах
make altinstall # устанавливаем рядом с другими пайтонами
# добавляем альтернативу питона
update-alternatives --install /usr/bin/python3.9 python3 /usr/local/bin/python3.9 3
update-alternatives --config python3 # выбираем установленную альтернативу как основную
# переходим в директорию куда клонировали hass
cd /root/core
git pull # получаем обновления
python3.9 -m pip install -r requirements_all.txt # ставим новые пакеты в новый python3
```