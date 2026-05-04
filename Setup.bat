@echo off
echo Installing NoMark dependencies...
timeout 1 >nul
cls
pip install requests colorama pystyle
cls
echo Done. Run with: python nomark.py
pause
python main.py
