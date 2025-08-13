*上一节，我们讲解了如何在esp32上烧录系统，已经如何开发esp32开发板功能，本节将重点通过温度传感器来学习MQTT的实战*

**消息队列在物联网开发中的用途**

- 队列机制为设备并发提供了有效的缓存
- 消息队列生产者消费者设计模式：两大⻆色之订阅者、发布者

**使用消息队列实现数据通信**

物联网中经常使用 MQTT 协议实现消息队列

目前 MQTT 协议最新版本为 5.0 版本，典型的 `EMQX`、`HBMQTT` 等都能完整支持

*有关MQTT的介绍可以参考第80节的内容*

**进入正文**

1. 首先我们准备了 `mqtt-project` 文件夹，我们将在这个目录中，实现如下功能：

- wifi连接
- 连接 MQTT 服务器，实现订阅和发布消息
- 连接温度传感器，获取温度数据并发布到 MQTT 服务器
- 在 `OLED` 和 `移动设备` 上显示温度数据

2. 新建 `wifi.py` 文件，并运行开发板，可以看到如下输出，则表示 ESP32 成功连接到 WiFi 网络

![image-20250813145216334](https://oss.yanquankun.cn/oss-cdn/img/image-20250813145216334.png!watermark)

3. 我们选用 `EMQX` 作为 MQTT 服务器，首先需要在 `EMQX` 上注册账号并创建一个新的 MQTT 服务器实例。

- 访问 [EMQX Cloud](https://www.emqx.com/zh) 注册账号并登录
- 下载并安装 `EMQX` 客户端 [EMQX](https://mqttx.app/zh/downloads)
- 在 `EMQX` 控制台创建一个新的 MQTT 服务器实例（生产环境我们需要创建真实的EMQX服务），但是为了方便测试，我们可以使用 `EMQX` 提供的公共测试服务器：[EMQX测试服务器](https://www.emqx.com/zh/mqtt/public-mqtt5-broker)
![image-20250813151118482](https://oss.yanquankun.cn/oss-cdn/img/image-20250813151118482.png!watermark)
- 然后在 `MQTTX` 中连接该服务器
![image-20250813151332364](https://oss.yanquankun.cn/oss-cdn/img/image-20250813151332364.png!watermark)
![image-20250813151345512](https://oss.yanquankun.cn/oss-cdn/img/image-20250813151345512.png!watermark)
- 创建一个 `temp_topic` 主题以供我们的开发板对温度的数据进行发布和订阅
![image-20250813151743321](https://oss.yanquankun.cn/oss-cdn/img/image-20250813151743321.png!watermark)

4. 创建 `mqtt_pub.py` 和 `mqtt_sub.py` 文件，分别用于发布和订阅消息，同时需要下载 [MQTT Client](https://github.com/micropython/micropython-lib/tree/master/micropython/umqtt.simple) 安装包，我以下载好放置到lib目录中了

5. 触发mqtt_pub，可以看到如下输出
![mqtt](https://oss.yanquankun.cn/oss-cdn/img/mqtt.png!watermark)
![mqtt2](https://oss.yanquankun.cn/oss-cdn/img/mqtt2.png!watermark)

*注意：*
如果你在使用时，提示mqtt [Errno 116] ETIMEDOUT

那多半是你的网络连接有问题，或者是你的MQTT服务器没有正确配置

可以按如下步骤进行排查：

1.	确认 SSID 和密码：再次检查是否正确。可以在手机上忘记 Wi-Fi 后重新连接，确保 SSID 和密码都正确。
2.	重新启动 ESP32：确保没有缓存的网络连接，手动按一下 ESP32 的复位按钮，清除可能的连接错误。
3.	检查网络设置：
- 尽量不要使用公司内网，可能会有限制，可以切换到个人热点或家庭网络
- 在手机设置中查看热点配置，确保热点是开启的，并且没有设置 Wi-Fi 隔离 或 MAC 过滤。
- 确保热点运行的是 2.4GHz 网络（确保你的手机热点是 2.4GHz，而不是 5GHz，因为大部分 ESP32 只支持 2.4GHz Wi-Fi），ios上在热点页面打开最大兼容性按钮即可