@echo off
chcp 65001 > nul
echo Dang kiem tra cap nhat tu DataTalksClub...
python scripts\sync_upstream.py
pause
