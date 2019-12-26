# 颗粒污染物监测装置（不限于pm2.5）

## 效果图
![show](https://github.com/eckygao/pm2.5MonitoringDevice/blob/master/img/show.png)

## 组成部分

- esp32 modemcu 开发板
- 颗粒物传感器
- OLED显示屏
- 电池

## 搭建过程

### ESP32刷入micropython固件

- 准备工具

[固件工具 esptool](https://github.com/espressif/esptool)

[串口工具 apmy](https://github.com/scientifichackers/ampy)

- 下载固件

按指引下载适用于 ESP32 的[固件](https://micropython.org/download#esp32)

- 刷写固件

以macos为示例，其它系统参考安装工具说明文档。
此处用的是 20190725_v1.11 版本
```
python esptool.py --port /dev/cu.SLAB_USBtoUART erase_flash
python esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART write_flash -z  0x1000 esp32-20190725-v1.11-178-gad0b7cb01.bin
```

### 上传代码

micropython 固件会顺序调用两个文件 boot.py main.py。当前版本功能简单，只用其中一个即可
```
ampy -p /dev/cu.SLAB_USBtoUART put main.py
```

### 接线
暂略，后补

### 上电
接通电源即可
