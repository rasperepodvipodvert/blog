# Рецепты по защите своего трафика от РКН (Роскомнадзор)

## Ссылки

- [openvpn-install](https://github.com/Nyr/openvpn-install)
- [Настройка VPN на DigitalOcean (l2tp)](https://dgnz.ru/info/nastraivaem-svoj-vpn-l2tp-ipsec-na-digitalocean.html?utm_referrer=https%3A%2F%2Fdgnz.ru%2Finfo%2Fnastraivaem-svoj-vpn-l2tp-ipsec-na-digitalocean.html)
- [rkn_unblock.md](https://gist.github.com/furdarius/ccb61a7bf8e747d43be5e908cc36dd92)

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