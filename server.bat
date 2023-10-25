@echo off
title Server
set VENV_DIR=.venv

if exist "%VENV_DIR%" (
    echo Activating virtual environment..
    call "%VENV_DIR%\Scripts\activate.bat"
)

set /p Input="Port : "


%@Try@%
    cls
    color 0a
    python main.py host %Input%
%@EndTry@%
%@Catch@%
    cls
    color 0a
    python3 main.py host %Input%
%@EndCatch@%

if errorlevel 1 (
    echo An error ocurred !
)
