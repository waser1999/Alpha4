山田案件：调查终端 Demo

运行：
  Windows：双击 run_windows.bat
  或在终端中执行：python game.py

命令：
  help   显示帮助
  ls     列出档案
  clear  清屏
  exit   退出
  其他输入会被当作档案名读取；可省略 .txt

添加档案：
  将 UTF-8 编码的 .txt 文件放入 files 文件夹即可。
  例如新增 files/new_evidence.txt 后，输入 new_evidence 即可读取。

本 Demo 是一个本地文件读取原型，暂未加入谜题判定、存档、人物状态或时间线自动推理。
