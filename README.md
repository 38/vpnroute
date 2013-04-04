vpnroute
========
这个脚本是chnroutes的改进版
使用sh install.sh进行安装
和chnroutes的主要区别在于允许用户定义一些可以直接访问的境外网站
而且能够很方便地更新IP列表
使用一个简单的配置文件来存储IP列表
允许注释和include
使用update_vpnroute来自动生成国内的IP地址列表
在/etc/ppp/vpnroute.d/user.conf中添加希望直接访问的境外网站

/etc/ppp/vpnroute.d/china.conf中不要添加内容，因为它可能被覆盖


