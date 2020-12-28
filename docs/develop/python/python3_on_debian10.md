title: Как установить python3 на Debian 10
description: Как установить python3 на Debian 10


```bash
apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget curl
curl -O https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tar.xz
tar -xf Python-3.8.2.tar.xz
cd Python-3.8.2
./configure --enable-optimizations
make -j 2
make altinstall
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
update-alternatives --config python3
python3 -V
```