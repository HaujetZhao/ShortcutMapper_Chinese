"""
# 脚本功能：将中间文件 intermediate.json 中的快捷键更新到 ShortcutMapper 的数据中（content 文件夹中）

# 运行这个脚本之前，请确保本脚本所在文件夹中有 intermediate.json
"""

import os
import sys
import csv
import logging

# 将资料库根目录加到 sys.path (这会使 import shmaplib 正常工作)
CWD = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CWD)
sys.path.insert(0, os.path.normpath(os.path.join(CWD, '..', '..')))

# 导入 shmaplib 库
import shmaplib

def export_intermediate_file(file_path, explicit_numpad_mode):
    log.info("Exporting from file: %s", file_path)
    exporter = shmaplib.IntermediateDataExporter(file_path, explicit_numpad_mode)
    exporter.parse()
    exporter.export()

log = shmaplib.setuplog(None)
log.setLevel(logging.INFO)
export_intermediate_file('intermediate.json', True)