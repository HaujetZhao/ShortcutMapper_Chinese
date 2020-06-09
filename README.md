> 项目来自于 https://github.com/waldobronchart/ShortcutMapper ，下面为我为方便自己查看，做的中文翻译 README。

# ShortcutMapper

这是一个由 Github 托管的键盘快捷键可视化工具： https://jackalzhao.github.io/ShortcutMapper_Chinese/

为方便在国内使用，在 Gitee 上也有备份：http://haujet.gitee.io/shortcutmapper_chinese/ 

这个项目的目标是，将应用程序的 **快捷键** 映射到 **虚拟键盘** 上，以便于查找和学习新的快捷键。 为减少错误并易于更新，目前所有的快捷键都是从官方在线文档中抄来的。

![Imgur](https://images.gitee.com/uploads/images/2020/0605/115552_70958150_619077.gif)

# 总览

这个项目是直接从 Githun 上的主 **gh-pages** branch 上来的。所有这个 branch 的变化是活动的。

```
/content         网站内容
    /generated   包含生成的包含应用快捷键的 json/js 文件（以本网站格式储存）
    /keyboards   包含 html 键盘布局
    ...
/sources         每个应用快捷键的源文件
/shmaplib        Python 工具库，用于帮助导出快捷工具到 webapp 
/tests           Python 测试，确保没有错误
/utils           用于导出和测试的工具
index.html       主站点
```

# 贡献

## 本地运行

本站的唯一一个页面就是 **index.html** 

这个应用使用 ajax 请求，以载入快捷键数据。但 ajax 使用 file:// 协议时会失败，所以你需要设置浏览器允许这个。这里是如何设置 Chrome:  http://stackoverflow.com/a/21413534 

当上述做完后，只要打开 **index.html** 就可以用了！



### 添加应用快捷键的简单例子  ——by 淳帅二代

例如，我想给 Vditor 添加快捷方式图，我需要做以下几步：

在 `sources` 目录新建文件夹 `Vditor`，建立如下的子目录：

```
/sources
    /Vditor
        /intermediate
```

在 `Vditor` 目录中，我新建了 `生成中间文件.py` 文件，内容是这样的：

```python
# ============================================================
# 先编写下面的脚本，可以用爬虫从网页上批量抓取快捷键
# 要是不会前端抓取，那就只能手动写各个快捷键了
# 获取完快捷键后，运行此脚本，就会生成中间文件
# 最好再手动检查一下那个中间文件
# 之后到项目主目录运行：python utils/export_intermediate_data.py sources/Vditor/intermediate/Vditor.json
# 就会将中间文件转换到 contents 中，也就可以在网页上看到了。
# 更新快捷方式也是以上两步
# ============================================================

import os
import sys

# 将资料库根目录加到 sys.path (这会使 import shmaplib 正常工作)
CWD = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CWD)
sys.path.insert(0, os.path.normpath(os.path.join(CWD, '..', '..')))

# 导入 shmaplib 库
import shmaplib

# 创建中间数据容器
idata = shmaplib.IntermediateShortcutData(app_name="Vditor", version="v3", default_context="通用")

# ============================================================
# 你可以下载一个带快捷键列表的网页，作为源文件，在这里写个脚本代码解析源文件批量生成数据
# 不会前端抓取。。。下面手动添加吧。
# 添加快捷键到容器，像这样就添加了一个快捷键：
context_name = "通用"
label = "表情"
keys_win = "Shift + ;"
keys_mac = "Command + E"
idata.add_shortcut(context_name, label, keys_win, keys_mac)
# ============================================================

# 保存中间文件到 intermediate/Vditor.json
idata.serialize('intermediate/Vditor.json')
```

写好后，把上面的脚本运行一下，再到项目主目录执行 `python utils/export_intermediate_data.py sources/Vditor/intermediate/Vditor.json` ，就把一个程序的快捷键添加到网页上了。

其实原作者在添加 Adobe 这样的软件的时候，就是用的脚本批量抓取的。不过我是不会那样的神奇操作，也只会手动添加了。有能力的朋友，可以尝试贡献下嘛~

以后可能会加入以下应用的快捷键映射图，欢迎参与：

- Windows
- Microsoft Office Word
- Microsoft Office Excel
- Microsoft Office PowerPoint
- PotPlayer
- Affinity Photo
- Affinity Design
- Affinity Publish
- GIMP
- VS code
- Typora
- Vim



## 导出更新的快捷键

**导出脚本** 使用 python3 和一些额外库，我推荐像这样使用 [virtualenv](http://virtualenv.readthedocs.org/en/latest/) ：

```
# 安装 pip
sudo easy_install pip

# 安装 virtualenv
pip install virtualenv

# 在 ShortcutMapper/_venv 目录中创建一个虚拟环境
# 对于 Windows,参照这里：
# http://virtualenv.readthedocs.io/en/latest/userguide/#usage
cd ShortcutMapper/
virtualenv -p /usr/bin/python3 _venv

# 激活环境
source _venv/bin/activate
pip install BeautifulSoup4

# 执行导出
python exporters/adobe-photoshop/scripts/export.py -a
```

一旦你的 virtualenv  安装上了，你只需要在导出之前激活：

```
source _venv/bin/activate

# 对于 Windows，你只需要用这个：
_venv\Source\activate.bat

# 导出所有中间 json 文件到 content/generated/
python utils/export_intermediate_data.py -a
```

## 为一个新应用添加快捷方式

**你能查看的最好的例子是位于 /sources/autodesk-maya 的 Autodesk Maya**

### 导出文件夹设置

首先，尝试寻找为每个平台列出所有应用快捷键的在线资源。以 Adobe 应用为例，我使用他们的在线文档： http://helpx.adobe.com/lightroom/help/keyboard-shortcuts.html

确保它是最新的并且是完整的

你将使用这个资源创建易于手动修改的中间数据格式。

在  **/sources** 创建一个文件夹结构，像这样：

```
/sources
    /my-app
        /intermediate           从原始数据转换后的文件，应当被手动编辑以修改错误的快捷键和太长的标签
        /raw                    原始数据文件
```

然后，理论上，你需要写一个脚本，将原始数据转换到中间文件： `/sources/my-app/raw_to_intermediate.py`

经过中间数据创建这一步，接下来的事情都能自动化了。基本上所有重活代码都在 `shmaplib` 里面。

### 使用 SHMAPlib

SHMAPlib 是 "Shortcut Mapper Lib" 的缩写. 它是一个 Python 库，让你把正确的数据导出到正确的位置。

如果你的脚本是不固定的，并且直接在 **/sources/app/** 下运行，那么你可以像这样导出这个库：

```
# 将资料库根目录加到 sys.path (这会使 import shmaplib 正常工作)
CWD = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CWD)
sys.path.insert(0, os.path.normpath(os.path.join(CWD, '..', '..')))

# 导入 shmaplib 库
import shmaplib
```

从这里你可以解析源文件（html, xml, etc..）并且创建中间数据。

```
import shmaplib

# 创建蹭数据容器
idata = shmaplib.IntermediateShortcutData("Application Name")

# 解析源文件
# ...添加快捷键到容器，像这样：
context_name = "Global Context"
label = "Select All"
keys_win = "Ctrl + A"
keys_mac = "Cmd + A"
idata.add_shortcut(context_name, label, keys_win, keys_mac)

# 保存文件
idata.serialize('intermediate/my-application_v3.json')
```

经手动编辑（总会有一些边角需要修复的）后，接下来你可以导出这个中间文件：

```
# 导出中间文件到前端文件
python utils/export_intermediate_data.py sources/application-name/intermediate/SOURCE.json
```

如果你的应用没有中间格式（例如 Blender），你可以使用下面的指南创建数据：

- *shmaplib.ApplicationConfig*: 主程序数据格式 (名字name, 系统os, 版本version, 和快捷键情景shortcut-contexts)
- *shmaplib.ShortcutContext*: 对于指定情景的快捷键容器 (Lightroom: Global, Develop, Library)
- *shmaplib.Shortcut*: 快捷键的数据格式 (name, key and modifiers)

你将首先创建 AppConfig，然后创建新的情景，用于添加快捷键。

AppConfig 有多个 ShortcutContexts，后者有多个 Shortcuts。

AppConfig 有一系列功能，能导出它到 /content/generated 下的正确的文件夹。

查看 `shmaplib/appdata.py` 以获得更多细节



## Pull Requests Flow

我遵循git-flow流程获取新功能和错误修正。您可以在此处阅读有关内容：https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow

基本上，您将从 `gh-pages` 分支中创建一个类似 `feature / descriptive-feature-name` 的分支，然后开始工作。 完成后，您将创建一个合并到 `develop` 分支中的拉取请求。 这使我可以在更改发布到 `gh-pages` 分支之前对其进行测试。

对于bug修复，您将命名分支为 `bugfix / descriptive-bug-name` 。

### 新键盘的预期内容

理想情况下，Windows和Mac键盘都是从其他现有布局（例如Klingon）创建的：

- content/keyboards/klingon.html
- content/keyboards/klingon_mac.html

这些文件添加到 `content/keyboards/keyboards.js` 的键盘列表中

```
var sitedata_keyboards = {
    ...
    "Klingon": {
        mac: "klingon_mac.html",
        windows: "klingon.html",
        linux: "klingon.html",
    }
}
```

确保在 `/tests` 文件夹中运行所有测试，以确保所有key均有效。

### 新应用的预期内容

请确保阅读了上面的“为一个新应用添加快捷方式”一节，优良作法是使提交内容简短而有条理，以便查看。



首先，我找到一个原始资源并编写一个scraper脚本来生成中间文件 (Example: https://github.com/waldobronchart/ShortcutMapper/commit/76f7b2f6c895bebebd5a5948c3bc759ac7779189)

- sources/thefoundry-nuke/raw/nuke_8.0_user_guide_hotkeys.html
- sources/thefoundry-nuke/raw_to_intermediate_nuke8.py

用 `raw_to_intermediate` 脚本生成中间文件 (Example: https://github.com/waldobronchart/ShortcutMapper/commit/f1db1aa3268e0a82b5394d7e1c26335153872cb5)

- sources/thefoundry-nuke/intermediate/thefoundry_nuke_8.0.json

对中间文件进行一些必要的手动编辑，例如在情境中进行更好的分组，并缩短一些长名称。 最好先保留原始内容，这样您可以更轻松地跟踪更改 (Example: https://github.com/waldobronchart/ShortcutMapper/commit/767556431a983481abd7cc0a30f1878cceef5fe9)

- sources/thefoundry-nuke/intermediate/thefoundry_nuke_8.0.json

继续重新生成应用程序内容（使用`/utils/export_intermediate_data`），直到对更改满意为止。 请注意在导出过程中修复警告

当您对所有更改感到满意时，提交生成的数据 (Example: https://github.com/waldobronchart/ShortcutMapper/commit/5533cdf94e9cab5564b9a946f528638cea6420f3)

- content/generated/apps.js (app was added here)
- content/generated/the-foundry-nuke_8.0_mac.json
- content/generated/the-foundry-nuke_8.0_windows.json

然后创建一个新的请求到`develop`分支。
