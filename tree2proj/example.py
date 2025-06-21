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
## 方法1：自定义
parser = Tree2Json()
parser.from_string(tree_str)

builder = ProjBuilder(parser.to_dict())
builder.create_fs()

## 方法2：使用封装好的
from builder import ProjBuilder

tree_str = """
my_project
├── README.md
├── src
│   └── main.py
└── data
    └── sample.txt
"""

ProjBuilder.build_from_tree_str(tree_str)
