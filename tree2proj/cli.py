import argparse
import json
import os
import sys
from tree2json import Tree2Json
from tree2proj import ProjBuilder
def main():
    try:
        import pyperclip
        print("已安装pyperclip")
    except ImportError:
        print("❗ 需要安装 pyperclip 模块： pip install pyperclip")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Build project structure from JSON or tree text.")
    parser.add_argument("json_file", nargs="?", help="Path to tree.json (or leave blank to use clipboard)")
    parser.add_argument("--output", "-o", help="Output directory", default=None)
    args = parser.parse_args()

    if args.json_file:
        # 从 JSON 文件读取
        if not os.path.isfile(args.json_file):
            print(f"❌ 文件不存在: {args.json_file}")
            sys.exit(1)
        with open(args.json_file, "r", encoding="utf-8") as f:
            tree = json.load(f)
        builder = ProjBuilder(tree)
        builder.create_fs(base_path=args.output)
    else:
        # 从剪贴板读取字符串
        print("📋 正在从剪贴板读取目录树...")
        tree_str = pyperclip.paste()
        if not tree_str.strip():
            print("❌ 剪贴板为空，请先复制目录树结构文本。")
            sys.exit(1)
        try:
            parser = Tree2Json()
            parser.from_string(tree_str)
            builder = ProjBuilder(parser.to_dict())
            builder.create_fs(base_path=args.output)
        except Exception as e:
            print("❌ 剪贴板内容不是有效的目录树结构")
            print(f"错误信息: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()