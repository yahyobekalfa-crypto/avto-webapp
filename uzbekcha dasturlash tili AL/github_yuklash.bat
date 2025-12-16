@echo off
setlocal

echo Git qidirilmoqda...

set "GIT_PATH="

if exist "C:\Program Files\Git\cmd\git.exe" (
    set "GIT_PATH=C:\Program Files\Git\cmd\git.exe"
) else if exist "C:\Program Files\Git\bin\git.exe" (
    set "GIT_PATH=C:\Program Files\Git\bin\git.exe"
) else if exist "C:\Program Files (x86)\Git\cmd\git.exe" (
    set "GIT_PATH=C:\Program Files (x86)\Git\cmd\git.exe"
) else if exist "%LOCALAPPDATA%\Programs\Git\cmd\git.exe" (
    set "GIT_PATH=%LOCALAPPDATA%\Programs\Git\cmd\git.exe"
)

if "%GIT_PATH%"=="" (
    echo XATOLIK: Git topilmadi! Iltimos, Git o'rnatilganiga ishonch hosil qiling.
    echo https://git-scm.com/download/win
    pause
    exit /b
)

echo Git topildi: "%GIT_PATH%"

echo.
echo === GitHub ga yuklash boshlandi ===
cd /d "%~dp0"

echo.
echo 1. Eski git fayllarini tozalash...
if exist .git (
    rd /s /q .git
)

echo.
echo 2. Repository yaratish...
"%GIT_PATH%" init
"%GIT_PATH%" add .
"%GIT_PATH%" commit -m "AL Tili v1.0.1 - Birinchi yuklanish"
"%GIT_PATH%" branch -M main

echo.
echo 3. GitHub bilan bog'lash...
"%GIT_PATH%" remote add origin https://github.com/yahyobekalfa-crypto/uzbekchadasturlash.git

echo.
echo 4. Yuklash (Push)...
"%GIT_PATH%" push -u origin main

echo.
echo === TUGADI ===
echo Agar "Everything up-to-date" yoki muvaffaqiyatli xabarlarni ko'rsangiz, demak yuklandi.
echo.
pause
