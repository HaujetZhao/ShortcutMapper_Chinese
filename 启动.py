"""
这个脚本使用 Python 自带的 HTTP 服务功能
将本文件夹绑定在指定端口
并使用默认浏览器打开
默认使用的端口是 8000 
你可以在下方的变量处设置端口、地址

安装上 python 后，双击本脚本，即可运行

默认运行后，会有一个黑窗口（命令行窗口），
如果你是在 Windows 系统上，不想看见这个黑窗口，
可以将本脚本的后缀 py 改成 pyw
就会静默运行了
"""


from http import server
from functools import partial
import contextlib
import socket  # For gethostbyaddr()
import sys
import webbrowser
import os

端口 = 8000
地址 = '::'


def test(HandlerClass=server.BaseHTTPRequestHandler,
         ServerClass=server.ThreadingHTTPServer,
         protocol="HTTP/1.0", port=端口, bind=地址):
    
    ServerClass.address_family, addr = server._get_best_family(bind, port)

    HandlerClass.protocol_version = protocol
    with ServerClass(addr, HandlerClass) as httpd:
        host, port = httpd.socket.getsockname()[:2]
        url_host = f'[{host}]' if ':' in host else host
        print(
            f"已在地址 {host} 的 {port} 端口上启用了 HTTP 服务\n"
            f"请访问这个链接： http://{url_host}:{port}/\n"
            f"..."
        )
        try:
            webbrowser.open(f'http://{url_host}:{port}')
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n接收到退出按键指令，退出中")
            sys.exit(0)

handler_class = partial(server.SimpleHTTPRequestHandler,
                        directory=os.path.dirname(__file__))


# ensure dual-stack is not disabled; ref #38907
class DualStackServer(server.ThreadingHTTPServer):
    def server_bind(self):
        # suppress exception when protocol is IPv4
        with contextlib.suppress(Exception):
            self.socket.setsockopt(
                socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        return super().server_bind()

test(
    HandlerClass=handler_class,
    ServerClass=DualStackServer,
)
