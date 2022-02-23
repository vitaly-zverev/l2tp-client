# l2tp-client
script for l2tp (only pskshared secret) client tested on Ubuntu 20.04


## install packages:
```sh
sudo apt-get install strongswan xl2tpd python3
```

## user, password, ipssec preshared key and vpn server address are kept in config.ini 

## How to make a l2tp-vpn connection:
```sh
sudo python3 connect.py
```

### manual source:
https://interface31.ru/tech_it/2021/06/nastraivaem-l2tp-vpn-server-na-platforme-linux.html

