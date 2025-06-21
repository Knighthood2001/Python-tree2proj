import os

class ProjBuilder:
    def __init__(self, tree_dict):
        self.tree = tree_dict

    # def create_fs(self, base_path=None, with_description=True):
    #     """
    #     创建文件系统结构。
    #     :param base_path: 根目录路径，默认为树的根 name（如果不是"."）
    #     :param with_description: 是否写入 description（暂不处理）
    #     """

    #     # 如果没传 base_path，就根据根节点名字决定
    #     if base_path is None:
    #         root_name = self.tree.get("name", ".")
    #         base_path = os.getcwd() if root_name == "." else os.path.join(os.getcwd(), root_name)

    #     def _create_node(node, current_path):
    #         path = os.path.join(current_path, node["name"])

    #         if node["type"] == "dir":
    #             os.makedirs(path, exist_ok=True)
    #             for child in node.get("child", []):
    #                 _create_node(child, path)

    #         elif node["type"] == "file":
    #             os.makedirs(current_path, exist_ok=True)
    #             open(path, "w", encoding="utf-8").close()

    #     _create_node(self.tree, base_path)
    def create_fs(self, base_path=None, with_description=True):
        root_name = self.tree.get("name", ".")

        if base_path is None:
            # 如果是 "."，用当前工作目录
            if root_name == ".":
                base_path = os.getcwd()
            else:
                # 如果当前路径已经是 root_name，避免重复创建
                cwd = os.path.abspath(os.getcwd())
                if cwd.endswith(os.path.normpath(root_name)):
                    base_path = cwd
                else:
                    base_path = os.path.join(cwd, root_name)

        def _create_node(node, current_path):
            path = os.path.join(current_path, node["name"])
            if node["type"] == "dir":
                os.makedirs(path, exist_ok=True)
                for child in node.get("child", []):
                    _create_node(child, path)
            elif node["type"] == "file":
                os.makedirs(current_path, exist_ok=True)
                open(path, "w", encoding="utf-8").close()

        _create_node(self.tree, base_path)