@echo off
color F0
title oas Updater

cd /d "%~dp0"
set "_root=%~dp0"
set "_root=%_root:~0,-1%"
cd "%_root%"

set "_pyBin=%_root%\toolkit"
set "_GitBin=%_root%\toolkit\Git\mingw64\bin"
set "_adbBin=%_root%\toolkit\Lib\site-packages\adbutils\binaries"
set "PATH=%_root%\toolkit\alias;%_root%\toolkit\command;%_pyBin%;%_pyBin%\Scripts;%_GitBin%;%_adbBin%;%PATH%"

if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit
:begin

start /B python server.py
timeout /t 5

start python start_script.py "0日常-ove"
start python start_script.py "0日常-一号"
start python start_script.py "0日常-二号"
start python start_script.py "0日常0-体服"

exit /B