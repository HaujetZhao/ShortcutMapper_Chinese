import os
import sys

# 运行：python 生成中间文件.py
# 之后：python utils/export_intermediate_data.py sources/Vditor/intermediate/Vditor.json

# 将资料库根目录加到 sys.path (这会使 import shmaplib 正常工作)
CWD = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CWD)
sys.path.insert(0, os.path.normpath(os.path.join(CWD, '..', '..')))

# 导入 shmaplib 库
import shmaplib

# 创建中间数据容器
idata = shmaplib.IntermediateShortcutData(app_name="Vditor", version="v3", default_context="通用")

# 解析源文件
# 不会用前端抓取。。。下面手动添加吧。




# ...添加快捷键到容器，像这样：
"""
context_name = "通用"
label = ""
keys_win = ""
keys_mac = ""
idata.add_shortcut(context_name, label, keys_win, keys_mac)
"""
# ------------------------------------------------------------------------
context_name = "通用"
label = "表情"
keys_win = "Shift + ;"
keys_mac = "Command + E"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "标题"
keys_win = "Ctrl + H"
keys_mac = "Command + H"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "粗体"
keys_win = "Ctrl + B"
keys_mac = "Command + B"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "斜体"
keys_win = "Ctrl + I"
keys_mac = "Command + I"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "删除线"
keys_win = "Ctrl + S"
keys_mac = "Command + S"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "链接"
keys_win = "Ctrl + K"
keys_mac = "Command + K"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------

# ------------------------------------------------------------------------

# ------------------------------------------------------------------------

# ------------------------------------------------------------------------

# ------------------------------------------------------------------------

# ------------------------------------------------------------------------

# ------------------------------------------------------------------------


# 保存文件
idata.serialize('intermediate/Vditor.json')