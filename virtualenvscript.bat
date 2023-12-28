REM Set the name of the virtual environment
set VENV_NAME=venv

REM Set the Python executable path (modify if needed)
set PYTHON_EXECUTABLE=python3.11

REM Create virtual environment
%PYTHON_EXECUTABLE% -m venv %VENV_NAME%

REM Activate virtual environment
if exist "%VENV_NAME%\Scripts\activate" (
    call "%VENV_NAME%\Scripts\activate"
) else (
    echo Unable to activate virtual environment.
)

REM Optional: Install any required packages
if defined VENV_NAME (
    echo Installing required packages...
    pip install -r requirements.txt
)

echo Virtual environment is activated. Use "deactivate" to exit.
exit /b 0