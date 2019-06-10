# 使用jdb远程debug jar包运行的程序

### 1.启动 

 ``` 
 	java -Xdebug -Xrunjdwp:server=y,transport=dt_socket,address=127.0.0.1:8090,suspend=n -jar pluginDetector.jar
 ```

### 2.链接 

 ```
	jdb -connect com.sun.jdi.SocketAttach:hostname=localhost,port=8090
 ```

### 3.jdb里执行help或？查看详细指令
