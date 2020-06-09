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
context_name = "通用"
label = "标题变大"
keys_win = "Ctrl + Shift + EQUAL or Ctrl + NUMPAD_PLUS"
keys_mac = "Command + Shift + EQUAL or Cmd + NUMPAD_PLUS"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "标题变小"
keys_win = "Ctrl + MINUS or Ctrl + NUMPAD_MINUS"
keys_mac = "Command + MINUS or Cmd + NUMPAD_MINUS"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "H1标题"
keys_win = "Ctrl + Alt + ONE"
keys_mac = "Command + Alt + ONE"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "H2标题"
keys_win = "Ctrl + Alt + TWO"
keys_mac = "Command + Alt + TWO"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "H3标题"
keys_win = "Ctrl + Alt + THREE"
keys_mac = "Command + Alt + THREE"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "H4标题"
keys_win = "Ctrl + Alt + FOUR"
keys_mac = "Command + Alt + FOUR"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "H5标题"
keys_win = "Ctrl + Alt + FIVE"
keys_mac = "Command + Alt + FIVE"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "通用"
label = "H6标题"
keys_win = "Ctrl + Alt + SIX"
keys_mac = "Command + Alt + SIX"
idata.add_shortcut(context_name, label, keys_win, keys_mac)

# =========================================
context_name = "标题"
label = "标题变大"
keys_win = "Ctrl + Shift + EQUAL or Ctrl + NUMPAD_PLUS"
keys_mac = "Command + Shift + EQUAL or Cmd + NUMPAD_PLUS"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "标题"
label = "变小"
keys_win = "Ctrl + MINUS or Ctrl + NUMPAD_MINUS"
keys_mac = "Command + MINUS or Cmd + NUMPAD_MINUS"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "标题"
label = "H1"
keys_win = "Ctrl + Alt + ONE"
keys_mac = "Command + Alt + ONE"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "标题"
label = "H2"
keys_win = "Ctrl + Alt + TWO"
keys_mac = "Command + Alt + TWO"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "标题"
label = "H3"
keys_win = "Ctrl + Alt + THREE"
keys_mac = "Command + Alt + THREE"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "标题"
label = "H4"
keys_win = "Ctrl + Alt + FOUR"
keys_mac = "Command + Alt + FOUR"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "标题"
label = "H5"
keys_win = "Ctrl + Alt + FIVE"
keys_mac = "Command + Alt + FIVE"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "标题"
label = "H6"
keys_win = "Ctrl + Alt + SIX"
keys_mac = "Command + Alt + SIX"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "标题"
label = "弹出菜单"
keys_win = "Ctrl + H"
keys_mac = "Command + H"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# =========================================
context_name = "链接"
label = "输入框/元素之间切换"
keys_win = "Alt + Enter"
keys_mac = "Option + Enter"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "链接"
label = "输入框之间切换"
keys_win = "Tab"
keys_mac = "Tab"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# =======================================
context_name = "列表 "
label = "缩进"
keys_win = "Tab or Ctrl + Shift + I"
keys_mac = "Tab or Command + Shift + I"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "列表 "
label = "反向缩进"
keys_win = "Shift + Tab or Ctrl + Shift + O or Enter"
keys_mac = "Shift + Tab or Command + Shift + O or Enter"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "列表 "
label = "完成和待办之间切换"
keys_win = "Ctrl + Shift + J"
keys_mac = "Cmd + Shift + J"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "引用"
label = "在顶层引用前插入空块"
keys_win = "Ctrl + Alt + Enter"
keys_mac = "Command + Option + Enter"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "引用"
label = "在顶层引用后插入空块"
keys_win = "Alt + Enter"
keys_mac = "Option + Enter"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "引用"
label = "插入块元素"
keys_win = "Ctrl + Shift + ; or Shift + ."
keys_mac = "Command + Shift + ; or Shift + ."
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "引用"
label = "引用和块元素之间切换"
keys_win = "Ctrl + ;"
keys_mac = "Command + ;"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "代码块"
label = "输入框和代码块之间切换"
keys_win = "Alt + Enter"
keys_mac = "Option + Enter"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "代码块"
label = "隐藏编辑界面"
keys_win = "Esc"
keys_mac = "Esc"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "代码块"
label = "选中所有代码"
keys_win = "Ctrl + A"
keys_mac = "Command + A"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "表格"
label = "当前行下插入新行"
keys_win = "Ctrl + EQUAL or Ctrl + NUMPAD_PLUS"
keys_mac = "Cmd + EQUAL or Cmd + NUMPAD_PLUS"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "表格"
label = "删除行"
keys_win = "Ctrl + MINUS or Ctrl + NUMPAD_MINUS"
keys_mac = "Cmd + MINUS Cmd + NUMPAD_MINUS"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "表格"
label = "当前列后插入新列"
keys_win = "Ctrl + Shift + EQUAL or Ctrl + Shift + NUMPAD_PLUS"
keys_mac = "Cmd + Shift + EQUAL or Cmd + Shift + NUMPAD_PLUS"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "表格"
label = "删除列"
keys_win = "Ctrl + Shift + MINUS or Ctrl + Shift + NUMPAD_MINUS"
keys_mac = "Cmd + Shift + MINUS or Cmd + Shift + NUMPAD_MINUS"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "表格"
label = "左对齐"
keys_win = "Ctrl + Shift + L"
keys_mac = "Cmd + Shift + L"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "表格"
label = "中对齐"
keys_win = "Ctrl + Shift + C"
keys_mac = "Cmd + Shift + C"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "表格"
label = "右对齐"
keys_win = "Ctrl + Shift + R"
keys_mac = "Cmd + Shift + R"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "表格"
label = "光标移动到输入框中"
keys_win = "Alt + Enter"
keys_mac = "Option + Enter"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "表格"
label = "输入框之间切换"
keys_win = "Tab"
keys_mac = "Tab"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "表格"
label = "光标移动到上一个元素"
keys_win = "Shift + Tab or Backspace"
keys_mac = "Shift + Tab or Backspace"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------
context_name = "表格"
label = "将光标移动到下一个元素"
keys_win = "Tab"
keys_mac = "Tab"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ------------------------------------------------------------------------



# 保存文件
idata.serialize('intermediate/Vditor.json')