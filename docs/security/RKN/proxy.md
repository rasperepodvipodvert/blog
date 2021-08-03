# Рецепты по защите своего трафика от РКН (Роскомнадзор)

## Ссылки

- [openvpn-install](https://github.com/Nyr/openvpn-install)
- [Настройка VPN на DigitalOcean (l2tp)](https://dgnz.ru/info/nastraivaem-svoj-vpn-l2tp-ipsec-na-digitalocean.html?utm_referrer=https%3A%2F%2Fdgnz.ru%2Finfo%2Fnastraivaem-svoj-vpn-l2tp-ipsec-na-digitalocean.html)
- [rkn_unblock.md](https://gist.github.com/furdarius/ccb61a7bf8e747d43be5e908cc36dd92)

## L2TP Server (mikrotik rady)

!!! info "После запуска команды можно сразу устанавливать соединение на микротике и все будет работать"

!!! warning "Таким образом вы получите один логин и пароль, как создавать пользователей через этот скрипт пока не выяснил"

```sh
wget https://git.io/vpnsetup -O vpnsetup.sh && sudo sh vpnsetup.sh
```

### Mikrotik

```shell
# Создаем интерфейс. Логин/пароль укажите свои, полученные на предыдущем шаге
add connect-to=13.1.0.26 disabled=no ipsec-secret=PASSWORD name=RKN-VPN password=PASSWORD use-ipsec=yes user=vpnuser
# Разрешаем трафику из нашей сети ходить в VPN
add action=mark-routing chain=prerouting dst-address-list=rkn new-routing-mark=RKN passthrough=yes
# Добавляем маршрут, при каком условии трафик будет попадать в маршрут.
add distance=1 gateway=RKN-VPN routing-mark=RKN
# В маршрут будут попадать все сайты из списка RKN. На пример rutracker.org
add address=rutracker.org list=rkn
```


## Mikrotik Client - OpenVPN Server

После использования скрипта авто-установки, чтобы OpenVPN Client в RouterOS сработал, нужно в файле /etc/openvpn/server/server.conf выставить:
Ubuntu2104

```
proto tcp
auth SHA1
#tls-auth
```

```shell

```
