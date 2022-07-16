# 随机图API

## 运行环境要求

- php >= 8.1
- swoole >= 4.5
- swoole 关闭 Short Name
- json php 扩展
- pcntl php 扩展



## 图片要求

图片名称需要连续的整数后缀要求为 webp

如果你的图片未达到要求 那么可以运行 helper.py 这里有一个小工具可以帮助你完成图片的转化



## 配置

复制 .env.example 至 .env

APP_HOST 是你绑定的host

APP_PORT 是服务运行的端口

MAX_IMAGES 代表你的最大图片数量



## 安装与运行

### 安装

`composer install`


### 运行

`php index.php start`

推荐使用supervisor来使程序持久运行
