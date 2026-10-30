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
    return sorted(p for p in FILES_DIR.iterdir() if p.is_file())

def show_help():
    print("""
可用命令
  help       显示帮助
  ls         列出可读取的档案
  clear      清屏
  exit       退出终端

直接输入文件名即可读取档案，例如：
  case_overview
  yamada_last_mail.txt

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

    options = [name]
    if not Path(name).suffix:
        options.append(name + ".txt")

    clear_screen();
    for option in options:
        path = FILES_DIR / option
        if path.is_file():
            try:
                print()
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
    print("==============================================")
    print("         YAMADA CASE // 调查终端")
    print("==============================================")
    print("连接状态：本地档案库已挂载")
    print("输入 help 查看命令。")
    print()

    while True:
        try:
            command = input("CASE:// ").strip()
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
            print("可用档案：")
            for path in files:
                print(f"  {path.name}")
        elif lower == "clear":
            clear_screen()
        else:
            read_file(command)

if __name__ == "__main__":
    main()
