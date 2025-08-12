*上一章，我们已经安装好了esptool工具，同时也学习了一些理论知识，本节将直接在ESP32的开发板上进行烧录程序*

> 我的esp32配置如下
>
> 开发板型号为：ESP-32-S3-1-N16R8
>
> 连接口为 typec口
>
> 下载页地址：https://micropython.org/download/ESP32_GENERIC_S3/
>
> 需要下载的固件为：ESP32_GENERIC_S3-20250809-v1.26.0.bin（我已放置在files/micropython目录中）
>

1. 首次烧录前需要擦除ESP32的闪存，在终端中输入以下命令：

```bash
esptool.py erase_flash
```

可以看到如下输出：

![image-20250812142936790](https://oss.yanquankun.cn/oss-cdn/img/image-20250812142936790.png!watermark)

1. 先通过typec线将ESP32开发板连接到电脑上，并获取开发板的串口号

*有关串口号的可以查看官方的提示：*

![image-20250812142332256](https://oss.yanquankun.cn/oss-cdn/img/image-20250812142332256.png!watermark)

打开终端，输入以下命令查看串口号：

```bash
# linux
ls /dev/ttyUSB*
```

```cmd
# windows
mode
```

```bash
# macOS
ls /dev/cu.usbmodem*
```

可以看到我们的串口名为：`/dev/cu.usbmodem51850412331`

![image-20250812143257248](https://oss.yanquankun.cn/oss-cdn/img/image-20250812143257248.png!watermark)

2. 烧录固件到ESP32开发板上

```bash
# 在终端上运行如下烧录命令：
# 注意：由于我是在项目根目录执行的esptool，所以我的bin目录为如下地址，各位可根据自己的实际情况进行修改
esptool --chip esp32s3 --port /dev/cu.usbmodem51850412331 --baud 460800 write-flash 0 ./files/micropython/ESP32_GENERIC_S3-20250809-v1.26.0.bin
```

**参数解析：**

| 参数                                                    | 作用                                                        |
|-------------------------------------------------------|-----------------------------------------------------------|
| esptool                                               | 主命令 ESP32/ESP8266 系列芯片的烧录工具                               |
| --chip esp32                                          | 指定芯片类型 告诉工具目标芯片是 ESP32 系列（也可以是 esp8266、esp32s2、esp32c3 等） |
| --port /dev/cu.usbmodem51850412331                    | 指定串口 ESP32 开发板连接到电脑的串口地址（macOS 格式）                        |
| --baud 460800                                         | 设置波特率 烧录时的通信速度，460800 是常用的高速烧录波特率                         |
| write-flash                                           | 烧录操作 指定要执行的是写入闪存操作                                        |
| 0                                                     | 起始地址 烧录到闪存的起始地址，0 表示从闪存开头开始写入                             |
| ./files/micropython/ESP32_BOARD_NAME-DATE-VERSION.bin | 固件文件路径 要烧录的 MicroPython 固件文件的完整路径                         |

*补充说明*

`波特率选择：`460800 是较快的烧录速度，如果烧录失败可以尝试降低到 115200

`芯片类型：`ESP32-S3 应该使用 --chip esp32s3

可以看到如下烧录结果：

![image-20250812144907878](https://oss.yanquankun.cn/oss-cdn/img/image-20250812144907878.png!watermark)

3. 烧录完成后，重启 ESP32 开发板

在我们的开发板上有两个按钮，一个是 `RST` 按钮（复位按钮），一个是 `BOOT` 按钮（引导模式按钮），如图：

![ba5f69b1d8f466491fb249f4667177ea](https://oss.yanquankun.cn/oss-cdn/img/ba5f69b1d8f466491fb249f4667177ea.jpg!watermark)

| 按钮 全称                | 主要作用        | 使用场景                                                                                                      |
|----------------------|-------------|-----------------------------------------------------------------------------------------------------------|
| RST Reset (复位)       | 重启 ESP32 芯片 | - 程序运行异常时重启<br>- 烧录完成后重启使新程序生效<br>- 调试时重新开始执行程序<br>- 进入下载模式进行固件烧录<br>- 配合 RST 按钮进入烧录状态<br>- 某些情况下手动进入烧录模式 |
| BOO Boot Mode (启动模式) | 控制芯片启动模式    |                                                                                                           |

| 按钮操作组合   | 步骤                                                   | 结果                   |
|----------|------------------------------------------------------|----------------------|
| 普通重启     | 单独按下 RST 按钮                                          | ESP32 重新启动，运行当前固件    |
| 进入下载模式   | 1. 按住 BOOT 按钮<br>2. 按一下 RST 按钮<br>3. 松开 BOOT 按钮      | ESP32 进入烧录模式，可以烧录新固件 |
| 强制进入下载模式 | 1. 按住 BOOT 按钮<br>2. 按住 RST 按钮<br>3. 先松开 RST，再松开 BOOT | 确保进入烧录模式（某些固件可能需要）   |

**实际使用建议**

`烧录完成后：`按一下 RST 按钮重启，让新固件开始运行

`烧录失败时：`尝试手动进入下载模式再重新烧录

`程序调试时：`使用 RST 按钮快速重启程序
自动下载电路

4. 通过Thonny工具连接 ESP32 开发板

下载地址：[https://thonny.org/](https://thonny.org/)

打开 Thonny，选择菜单栏的 `工具` -> `选项` -> `解释器`，在解释器类型中选择 `MicroPython (ESP32)`，然后在端口中选择刚才获取的串口号
`/dev/cu.usbmodem51850412331`

![image-20250812145857323](https://oss.yanquankun.cn/oss-cdn/img/image-20250812145857323.png!watermark)

5. 测试连接是否成功

在 Thonny 的命令行中输入以下代码：

```python
import os
os.uname()
```
如果连接成功，会输出类似如下信息：

![image-20250812150348738](https://oss.yanquankun.cn/oss-cdn/img/image-20250812150348738.png!watermark)

6. 通过 Thonny 上传文件到 ESP32 开发板

* 在 Thonny 中：文件 → 另存为 → 选择 MicroPython 设备

* 或直接拖拽文件到 Thonny 的文件浏览器中

7. 将我们的 `ese-project` 文件上传到 ESP32 开发板上

*注意：在Thonny中将整个项目文件夹上传到ESP32开发板需要分步骤进行，因为Thonny不支持直接上传整个文件夹，我们可以在文件管理区域，将本地的文件，通过上传按钮上传到ESP中*

![image-20250812153908090](https://oss.yanquankun.cn/oss-cdn/img/image-20250812153908090.png!watermark)

8. 运行我们的程序，点击 Thonny 的运行按钮（绿色三角形），或者按下 F5 键，可以看到如下输出：

![image-20250812155037110](https://oss.yanquankun.cn/oss-cdn/img/image-20250812155037110.png!watermark)

> 至此，ESP32 的烧录程序已经完成，接下来我们可以开始编写和运行 MicroPython 程序了。

