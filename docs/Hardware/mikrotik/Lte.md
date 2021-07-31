Title: Привязка R11e-LTE к сектору базовой станции
Date: 2020-10-19 10:00
Author: ifilatov
Tags: routers, howto, best, internet, mikrotik
Slug: lte_lock
Status: published
Summary: Инструкция, как привязать R11e-LTE к сектору базовой станции

## Ссылки
- [Официальная документация по LTE CELL LOCK](https://wiki.mikrotik.com/wiki/Manual:Interface/LTE#Using_Cell_lock)
- [Полезные испытания Mikrotik LTE KIT](https://asp24.com.ua/blog/polevye-ispytaniya-mikrotik-sxt-lte-kit/?utm_source=rss&utm_medium=rss&utm_campaign=polevye-ispytaniya-mikrotik-sxt-lte-kit)
- [Карта базовых станций](https://www.cellmapper.net/map)

## Настройки

!!! info "При настройке статического IP через SXT LTE нужно учесть"
    - при настройке режиме Passthroungh нужно вырубать DHCP-Server на интерфейсе, который указан в настройках этого режима
    - необходимо указывать статический IP на нижнем роутере, куда вы пробрасываете LTE
    
!!! attention "Привязка возможна только к той станции, к которой уже подключался модем"

### Команда привязки модема

'/interface lte at-chat lte1 input="AT*Cell=2,3,,1550,459"'

### Что есть что

```
AT*Cell=<mode>,<NetworkMode>,<band>,<EARFCN>,<PCI>

<mode> :
0 – Cell/Frequency disabled
1 – Frequency lock enabled
2 – Cell lock enabled

<NetworkMode>
0 – GSM
1 – UMTS_TD
2 – UMTS_WB
3 – LTE

<band>
если требуется блокировка нарезки частот (обычно параметр оставляют пустой)

<EARFCN>
earfcn from lte info

<PCI>
phy-cellid from lte info

           pin-status: ok
  registration-status: registered
        functionality: full
         manufacturer: "MikroTik"
                model: "R11e-LTE"
             revision: "MikroTik_CP_2.160.000_v013"
     current-operator: MegaFon
                  lac: 7652
       current-cellid: 195875305
               enb-id: 765137
            sector-id: 233
           phy-cellid: 459
    access-technology: Evolved 3G (LTE)
       session-uptime: 1d11h22m
                 imei: 355654092401974
                 imsi: 250021083844857
                 uicc: 897010210838548578ff
               earfcn: 1550 (band 3, bandwidth 20Mhz)
                 rsrp: -96dBm
                 rsrq: -5.5dB
                 sinr: 17dB
```
