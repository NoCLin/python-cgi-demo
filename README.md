# Python CGI Demo -- 机房机位号展示 服务端

一个用于机房根据IP地址在每台机器显示机器号码的 零依赖HTTP Server。

服务器安装Python3运行server.py，客户端使用浏览器访问即可，建议搭配机房管理软件批量运行。

> 也可使用pyinstaller生成可执行文件，但注意Win7等系统可能需要安装某些运行库。

`wwwroot` 为 HTTP Server 根目录，可自由定制界面并使用前后端分离从cgi获取动态数据。
`cgi-bin`目录下为对应的cgi文件，注意使用 `chmod +x` 添加执行权限。

`mapping.csv`: 映射关系文件，可以使用Excel编辑。

