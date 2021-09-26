"""
# 脚本功能：从 csv 快捷键表格生成中间文件 intermediate.json

# 运行这个脚本之前，请确保本脚本所在文件夹中有 windows.csv 和 mac.csv
# 将软件快捷键按以下的格式填写到 csv 文件中：
# 情景    功能    按键1    按键3    ....

# 然后，用文本编辑器打开那 intermediate.json 文件，看一下有没有需要修改的地方
# 最后，运行 02 将中间文件添加到正式目录.py
"""

import os
import sys
import csv

# 将资料库根目录加到 sys.path (这会使 import shmaplib 正常工作)
CWD = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CWD)
sys.path.insert(0, os.path.normpath(os.path.join(CWD, '..', '..')))

# 导入 shmaplib 库
import shmaplib

def 测试encoding(file):
    try:
        with open(file, encoding='utf-8') as f:
            f.read()
            return 'utf-8'
    except:
        return 'gbk'

# 创建中间数据容器
idata = shmaplib.IntermediateShortcutData(app_name="One Commander", version="V3", default_context="通用")

# 确保 csv 文件存在
文件 = 'windows.csv'
encoding = 测试encoding(文件)
with open(文件, encoding=encoding) as csvfile:
    content = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in content:
        if len(row) < 3: continue
        context_name = row[0]
        label = row[1]
        keys_win = ' + '.join(list(filter(lambda x: x ,row[2:])))
        idata.add_shortcut(context_name, label, keys_win, '')

文件 = 'mac.csv'
encoding = 测试encoding(文件)
with open(文件, encoding=encoding) as csvfile:
    content = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in content:
        if len(row) < 3: continue
        context_name = row[0]
        label = row[1]
        keys_mac = ' + '.join(list(filter(lambda x: x ,row[2:])))
        idata.add_shortcut(context_name, label, '', keys_mac)

idata.serialize('intermediate.json')
