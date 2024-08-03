@echo off
REM Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b 1
)

REM Set the directory where the Python script is located
set SCRIPT_DIR=C:\C:\VOX\Extensions\OnPlayer\Google

REM Change to the script directory
cd /d "%SCRIPT_DIR%"

REM Run the Python script
python CHDown.py

REM Pause to keep the command window open after execution
pause
