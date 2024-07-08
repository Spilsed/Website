@echo off
rem Set the path to Python executable (if not in PATH)
set PYTHON_EXECUTABLE=python

rem Set the path to your Python script
set SCRIPT_FILE=satellaview+.py

rem Run the Python script
%PYTHON_EXECUTABLE% %SCRIPT_FILE%

rem Pause at the end (optional)
pause
