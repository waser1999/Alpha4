#!/usr/bin/env python3
# 山田案件：调查终端 Demo
# Python 3，无需安装第三方库

from pathlib import Path
import os
import sys

ROOT = Path(__file__).resolve().parent
FILES_DIR = ROOT / "files"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def list_files():
    with open(ROOT / "opened_files.txt", "r", encoding="utf-8") as f:
        return [FILES_DIR / line.strip() for line in f if line.strip()]

def show_help():
    print("""
可用命令
  help       显示帮助
  ls         列出可读取的档案
  clear      清屏
  exit       退出终端

直接输入文件名即可读取档案，例如：
  case_overview
  a_mysterious_text.txt

文件名可以省略 .txt 扩展名。
""".strip())

def read_file(user_input):
    # 只允许在 files 目录内读取文件，避免通过 ../ 访问其他路径。
    name = user_input.strip()
    if not name:
        return

    candidate = Path(name)
    if candidate.name != name or "/" in name or "\\" in name:
        print("访问拒绝：请输入档案名，不要输入路径。")
        return

    filename = name if candidate.suffix else f"{name}.txt"
    path = FILES_DIR / filename
    file_lists = list_files()
    file_is_opened = path in file_lists
    if path not in file_lists and path.is_file():
        with open(ROOT / "opened_files.txt", "a", encoding="utf-8") as f:
            f.write(f"{filename}\n")

    clear_screen();
    if path.is_file():
        try:
            print()
            if not file_is_opened:
                print(f"你已解锁新的档案。")
            print("=" * 60)
            print(f"档案：{path.name}")
            print("=" * 60)
            print(path.read_text(encoding="utf-8"))
            print("=" * 60)
        except OSError as exc:
            print(f"读取失败：{exc}")
        return

    print(f"档案不存在：{name}")
    print("输入 ls 查看可用档案，或输入 help 查看帮助。")

def main():
    clear_screen()
    print("=" * 40)
    print("         CASE ALPHA 4         ")
    print("=" * 40)
    print("连接状态：本地档案库已挂载")
    print("输入 help 查看命令。")
    print()

    while True:
        try:
            command = input(">: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n终止会话。")
            break

        if not command:
            continue

        lower = command.lower()
        if lower == "exit":
            print("正在关闭调查终端……")
            break
        elif lower == "help":
            show_help()
        elif lower == "ls":
            files = list_files()
            if not files:
                print("没有可用档案。")
                continue
            print("可用档案：")
            for path in files:
                print(f"  {path.name}")
        elif lower == "clear":
            clear_screen()
        else:
            read_file(command)

if __name__ == "__main__":
    main()
