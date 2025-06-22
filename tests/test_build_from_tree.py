from tree2proj import ProjBuilder
## 方法2：使用封装好的
tree_str = """
my_project
├── README.md
├── src
│   └── main.py
└── data
    └── sample.txt
"""

ProjBuilder.build_from_tree(tree_str)
