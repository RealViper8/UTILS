@echo off
title % Installing requirements %
set VENV_DIR=.venv

if exist "%VENV_DIR%" (
    echo Activating virtual environment..
    call "%VENV_DIR%\Scripts\activate.bat"
)

echo Running Python script...


%@Try@%
    cls
    color 0a
    python -m pip install -r requirements.txt
    python.exe -m pip install --upgrade pip
    echo Done.
%@EndTry@%
%@Catch@%
    cls
    color 0a
    python3 -m pip install -r requirements.txt
    python3 -m pip install --upgrade pip
    echo Done..
%@EndCatch@%

if errorlevel 1 (
    exit
) else (
    exit
)