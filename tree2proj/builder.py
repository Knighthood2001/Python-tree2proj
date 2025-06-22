import os
from tree2json import Tree2Json

class ProjBuilder:
    def __init__(self, tree_dict):
        self.tree = tree_dict

    def create_fs(self, base_path=None, with_description=True):
        root_name = self.tree.get("name", ".")

        if base_path is None:
            if root_name == ".":
                base_path = os.getcwd()
            else:
                base_path = os.path.join(os.getcwd(), root_name)

        # 👇 改为只遍历 root 的 child，而不是 root 本身
        def _create_node(node, current_path):
            path = os.path.join(current_path, node["name"])
            if node["type"] == "dir":
                os.makedirs(path, exist_ok=True)
                for child in node.get("child", []):
                    _create_node(child, path)
            elif node["type"] == "file":
                os.makedirs(current_path, exist_ok=True)
                open(path, "w", encoding="utf-8").close()

        # ⭐ 如果根目录是 "."，就在当前路径下创建其 child
        # ⭐ 如果是 "aaa"，就在 cwd/aaa 下创建其 child
        os.makedirs(base_path, exist_ok=True)
        for child in self.tree.get("child", []):
            _create_node(child, base_path)
    def build_from_tree(tree_str: str, base_path: str = None):
        """
        从树形字符串中构建项目结构（封装 Tree2Json + ProjBuilder）
        """
        parser = Tree2Json()
        parser.from_string(tree_str)
        builder = ProjBuilder(parser.to_dict())
        builder.create_fs(base_path=base_path)