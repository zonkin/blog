# wpa命令连接无线网络

## wpa2网络连接
### iwlist wlan0 scan 扫描无线网络
### wpa_passphrease 网络名称 密码 > ~/wpa2.conf
  生成wpa网络连接配置文件，主要是对密码加密
### wpa_supplicant -B -i wlan0 -c ~/wpa2.conf
  -B  后台守护运行
  -i  网络接口，网卡，ifconfig查看
  -c  连接配置文件
### dhclient wlan0
  dhcp 自动获取ip，dns，配置路由等
