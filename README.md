# 机房机位号展示 服务端

一个用于机房根据IP地址在每台机器显示机器号码的 零依赖HTTP Server。

服务器安装Python3运行server.py，客户端使用浏览器访问即可，建议搭配机房管理软件批量运行。

> 也可使用pyinstaller生成可执行文件，但注意Win7可能需要安装某些运行库。

`index.html`: HTML界面模板文件，`${ip}`与`${id}`用于模板替换。

`mapping.csv`: 映射关系文件，可以使用Excel编辑。

