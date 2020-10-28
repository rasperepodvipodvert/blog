title: Надежное хранилище данных на стороне Agent2
image:/docs/devops/zabbix/img/zabbix_agent2_buffer.png

# Надежное хранилище данных на стороне Agent2

## zabbix-agent2

Так называется новый агент заббикса.
Функция помогает записывать события при отсутсвии коннекта к вашему zabbix серверу!

Используется для:

- Надежного подключения
- Критических данных
- Спутникового соединения

??? summary "Включаем в: /etc/zabbix/zabbix-agent2.conf"

    ```ini
    # Собственно само включение
    EnablePersistentBuffer=1
    # Период, который будем хранить
    PersistentBufferPeriod=1d
    # Расположение базы в которой будем хранить данные
    PersistentBufferFile=/var/spool/zabbix/agent.db  
    ```