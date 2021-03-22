# Настройка мониторинга mikrotik по SNMP на zabbix

## Действия на микротике
```
ip firewall filter add chain=input protocol=udp in-interface-list=WAN action=accept place-before=1
snmp community add name=ts_123456 addresses=0.0.0.0/0
snmp set enabled=yes location=TS trap-community=ts_123456 trap-version=2
```

## Действия на zabbix

1. Установить [шаблон](https://www.zabbix.com/ru/integrations/mikrotik)

!!! note подходит и для zabbix 5.0