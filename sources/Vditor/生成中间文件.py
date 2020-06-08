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
context_name = "通用"
label = "表情"
keys_win = "Shift + ;"
keys_mac = "command + E"
idata.add_shortcut(context_name, label, keys_win, keys_mac)


# 保存文件
idata.serialize('intermediate/Vditor.json')