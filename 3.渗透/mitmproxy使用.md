# mitmproxy使用

### 启动配置

1. mitmproxy -p 8800
 启动mitmproxy并在本地8800端口监听代理

2. 设置浏览器代理为本地（127.0.0.1:8800）

3. 访问mitm.it下载安装证书（访问https信任mitmproxy的代理)
 * firefox安装： firefox ~/.mitmproxy/mitmproxy-ca-cert.p12 
 [](../assets/penetrating/install_cert.png)

### 访问网站查看链接

 [](../assets/penetrating/bing_urls.png)

### 操作

 ``zz`` 清空流
 ``?`` 显示帮助菜单
 vim软件操作详情页信息
 [](../assets/penetrating/mitmproxy_help.png)
 ``Tab键`` 切换标签页
 ``q`` 返回
 ``enter键`` 查看详情
 [](../assets/penetrating/mitmproxy_detail.png)
 ``e`` 编辑详情
 [](../assets/penetrating/mitmproxy_edit.png)

 **例如：修改url**

 [](../assets/penetrating/mitmproxy_editurl.png)

 ``r`` 重放，重新请求
 [](../assets/penetrating/mitmproxy_replay.png)
 ``f`` 设置过滤
 [](../assets/penetrating/mitmproxy_viewfilter.png)
 ``i`` 设置拦截条件
 [](../assets/penetrating/mitmproxy_intercept.png)
 ``a`` 允许请求

 
 
 
 
