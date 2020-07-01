title: Как установить python2 и pip2 на Ubuntu 20.04
description: Python2 больше не поддерживается!

# Как установить python2 и pip2 на Ubuntu 20.04

``` sh
sudo add-apt-repository universe
sudo apt update
curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py
sudo python2 get-pip.py
```