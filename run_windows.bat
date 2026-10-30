@echo off
chcp 65001 >nul
cd /d "%~dp0"
python game.py
if errorlevel 1 (
    echo.
    echo 启动失败。请确认已安装 Python 3，并且 python 命令可用。
    pause
)
