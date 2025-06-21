# tree2proj

`tree2proj` 是一个用于根据 JSON 格式的目录树结构，**自动生成对应的文件夹和文件** 的 Python 工具。它依赖 [`tree2json`](https://pypi.org/project/tree2json/) 包，将项目结构从类似 `tree` 命令的文本解析为 JSON 后，再由本工具落地为真实的项目结构。

---

## ✨ 功能亮点

- 根据目录树结构生成完整项目目录
- 支持命令行（CLI）快速构建项目骨架

---

## 📦 安装方法

确保 Python ≥ 3.7，先安装 `tree2proj`：

```bash
pip install tree2proj
```

## 🧰 用法说明

### ✅ 方式 1：Python 调用

```python
from tree2json import Tree2Json
from builder import ProjBuilder

tree_str = """
bbb
├── 5个创新模块.pdf
├── AIproject
|  ├── mnist.zip
|  └── 论文
├── bihui_pic
|  └── ccccz
├── Blender 4.3.lnk
├── 钉钉.lnk
└── 飞书.lnk
"""

parser = Tree2Json()
parser.from_string(tree_str)

builder = ProjBuilder(parser.to_dict())
builder.create_fs()

```


---

### ✅ 方式 2：命令行使用（CLI）

```bash
tree2proj
```
这会自动读取剪切板中的目录树文本（如果不是，会报错），并生成对应的项目结构。


---

## 🧩 依赖项

* `tree2json` ≥ 0.1.3

---

## 📝 许可协议

本项目遵循 MIT 开源许可证。欢迎自由使用与修改。

---

## 📬 联系作者

作者：[@knighthood](https://github.com/Knighthood2001)

欢迎提 Issue、PR 或交流建议！

## 版本
### v0.1.0
- 发布最基础版本
- 能够实现windows下使用命令行实现创建项目目录
- 添加读取剪切板的功能
