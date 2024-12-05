@echo off
for /f "delims=" %%a in ('dir /b /ad "C:\Users\%USERNAME%\AppData\Local\Programs\Python" ^| findstr /r "^Python[0-9]*$"') do (
    set PYTHON_VERSION=%%a
)

for /f "tokens=3" %%u in ('echo %USERPROFILE%') do set USERNAME=%%u
set SITE_PACKAGES=C:\Users\%USERNAME%\AppData\Local\Programs\Python\%PYTHON_VERSION%\Lib\site-packages

echo Python version: %PYTHON_VERSION%
echo Site Packages Directory: %SITE_PACKAGES%
echo Installing requirements...
pip install -r requirements.txt
echo Copying all folders from 'requirements' directory to site-packages...
for /d %%d in (requirements\*) do (
    echo Moving folder: %%d
    echo To: %SITE_PACKAGES%
    xcopy /e /i /y "%%d\*" "%SITE_PACKAGES%\%%~nxd\"
)
echo Folders copied and existing ones replaced.
pause