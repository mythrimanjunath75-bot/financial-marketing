@echo off
echo ========================================
echo  DATABASE VIEWER LAUNCHER
echo ========================================
echo.
echo This script will help you view your database
echo.

REM Check if DB Browser is installed
if exist "C:\Program Files\DB Browser for SQLite\DB Browser for SQLite.exe" (
    echo [*] DB Browser found! Opening database...
    start "" "C:\Program Files\DB Browser for SQLite\DB Browser for SQLite.exe" "%~dp0finance.db"
    exit
)

if exist "C:\Program Files (x86)\DB Browser for SQLite\DB Browser for SQLite.exe" (
    echo [*] DB Browser found! Opening database...
    start "" "C:\Program Files (x86)\DB Browser for SQLite\DB Browser for SQLite.exe" "%~dp0finance.db"
    exit
)

echo [!] DB Browser for SQLite is not installed.
echo.
echo OPTION 1: View in Python (works now)
echo =====================================
python show_db.py
echo.
pause
echo.

echo OPTION 2: Download DB Browser (Best tool)
echo ==========================================
echo.
echo Download from: https://sqlitebrowser.org/dl/
echo.
echo Press any key to open download page in browser...
pause >nul
start https://sqlitebrowser.org/dl/
echo.
echo After installing, run this script again!
echo.
pause
