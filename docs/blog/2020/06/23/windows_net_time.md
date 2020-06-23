Title: Синхронизация времени в Windows
Date: 2020-06-22 11:14
Author: ifilatov
Tags: windows, ntp
Status: published
Image: /media/windows_net_time.png
Summary: Пара команд для синхронизации времени в Windows

!!! note  
    Иногда, время на пк с Windows отстает, чтобы быстренько синхронихзироваться держу эти команды под рукой:

``` bat
net stop w32time
w32tm /unregister
w32tm /register
net start w32time
w32tm /resync
```