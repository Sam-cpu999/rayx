@echo off
color 4
echo ENTER ICON ICO PATH (Press Enter to skip):
set /p icon_file=
echo Getting Python version...
for /f "tokens=2" %%a in ('python --version 2^>^&1') do set PYTHON_VERSION=%%a
echo Running PyInstaller...
set pyinstaller_command=pyinstaller --onefile --noconsole --upx-dir "C:\Program Files\UPX" 
if not "%icon_file%"=="" (
    set pyinstaller_command=%pyinstaller_command% --icon "%icon_file%"
)
set pyinstaller_command=%pyinstaller_command% --exclude-module _lzma --exclude-module _multiprocessing --exclude-module attrs --exclude-module cryptography --exclude-module pytorch --exclude-module torch --exclude-module numpy --exclude-module Cython --exclude-module flask --exclude-module cv2 --exclude-module PyQt5 --exclude-module win32 --exclude-module yaml --exclude-module PythonWin --exclude-module jedi --exclude-module sounddevice --exclude-module google --exclude-module zstandard --hidden-import pyautogui "main.pyw"
echo %pyinstaller_command%
%pyinstaller_command%
echo Cleaning up...
rd /s /q build
del /f /q main.spec
echo Build complete.
exit