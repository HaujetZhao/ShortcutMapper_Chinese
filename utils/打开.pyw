# 目的：将 chrome 启用 --allow-file-access-from-files 打开 index.html 文件

from subprocess import run
from shlex import split
from pathlib import Path

程序名 = 'chrome'
文件 = Path('../index.html').absolute().as_uri()

命令参数 = [程序名, 
            '--allow-file-access-from-files', 
            文件
            ]

run(命令参数)
