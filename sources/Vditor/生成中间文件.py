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
keys_win = "Ctrl + "
keys_mac = "Command + "
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
context_name = "通用"
label = "无序列表"
keys_win = "Ctrl + L"
keys_mac = "Command + L"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "有序列表"
keys_win = "Ctrl + O"
keys_mac = "Command + O"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "引用"
keys_win = "Ctrl + J"
keys_mac = "Command + J"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "分割线"
keys_win = "Ctrl + Shift + H"
keys_mac = "Command + Shift + H"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "代码块"
keys_win = "Ctrl + U"
keys_mac = "Command + U"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "代码"
keys_win = "Ctrl + G"
keys_mac = "Command + G"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "元素前 插入空块"
keys_win = "Ctrl + Shift + B"
keys_mac = "Command + Shift + B"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "元素后 插入空块"
keys_win = "Ctrl + Shift + E"
keys_mac = "Command + Shift + E"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "表格"
keys_win = "Ctrl + M"
keys_mac = "Command + M"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "撤销"
keys_win = "Ctrl + Z"
keys_mac = "Command + Z"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "重做"
keys_win = "Ctrl + Y"
keys_mac = "Command + Y"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "隐藏编辑器"
keys_win = "Ctrl + P"
keys_mac = "Command + P"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "格式化"
keys_win = "Ctrl + Shift + F"
keys_mac = "Command + Shift + F"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "全屏"
keys_win = "Ctrl + '"
keys_mac = "Command + '"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "复制当前行/已选内容"
keys_win = "Ctrl + Shift + D"
keys_mac = "Command + Shift + D"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "删除当前行"
keys_win = "Ctrl + Shift + Backspace"
keys_mac = "Command + Shift + Backspace"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "向上移动块元素"
keys_win = "Ctrl + Shift + U"
keys_mac = "Command + Shift + U"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "向下移动块元素"
keys_win = "Ctrl + Shift + D"
keys_mac = "Command + Shift + D"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "移除当前元素"
keys_win = "Ctrl + Shift + X"
keys_mac = "Command + Shift + X"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "At 用户"
keys_win = "Shift + TWO"
keys_mac = "Shift + TWO"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "错误输入"
keys_win = "Backspace"
keys_mac = "Backspace"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------

# ------------------------------------------------------------------------

# ------------------------------------------------------------------------

# ------------------------------------------------------------------------


# 保存文件
idata.serialize('intermediate/Vditor.json')