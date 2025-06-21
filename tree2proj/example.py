from tree2json import Tree2Json

from builder import ProjBuilder

tree_str = """
.
├── 5个创新模块.pdf
├── AIproject
|  ├── mnist.zip
|  └── 论文
├── bihui_pic
|  ├── 4
|  └── ccccz
├── Blender 4.3.lnk
├── 钉钉.lnk
└── 飞书.lnk
"""

parser = Tree2Json()
parser.from_string(tree_str)

builder = ProjBuilder(parser.to_dict())
builder.create_fs()
