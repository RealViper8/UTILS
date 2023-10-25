@echo off
title LOADING ...
set VENV_DIR=.venv

if exist "%VENV_DIR%" (
    echo Activating virtual environment..
    call "%VENV_DIR%\Scripts\activate.bat"
)

echo Running Python script...


%@Try@%
    cls
    color 0a
    python main.py
%@EndTry@%
%@Catch@%
    cls
    color 0a
    python3 main.py
%@EndCatch@%

if errorlevel 1 (
    echo An error ocurred !
)
