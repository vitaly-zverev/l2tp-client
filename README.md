# l2tp-client
Script for l2tp (only shared secret) client, tested on Ubuntu 20.04.

## install packages:
```sh
sudo apt-get install strongswan xl2tpd python3
```

## "user", "password", "ipsec preshared key" and "vpn server ip address" are kept in config.ini 

## How to make a l2tp-vpn connection:
```sh
sudo python3 connect.py
```
## Example:

```sh
$ sudo python3 connect.py
starting service...
ipsec up......
ipsec up established successfully
try to login with user and password
waiting 3s for checking in...
ppp established
ppp established, adding route...
P-t-P estabished
route add -net 10.0.0.0/8  gw 195.209.150.199

l2tp connected
finished
```

### Alternative solutions:
https://hub.docker.com/r/ubergarm/l2tp-ipsec-vpn-client
https://openthreat.ro/openwrt-l2tp-ipsec-vpn-client-for-mikrotik-server/


### Server side manuals:
https://libreswan.org/wiki/VPN_server_for_remote_clients_using_IKEv1_with_L2TP
https://interface31.ru/tech_it/2021/06/nastraivaem-l2tp-vpn-server-na-platforme-linux.html



