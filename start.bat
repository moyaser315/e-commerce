@echo off
:: Start backend.bat in a new terminal window
echo Starting backend...
start cmd /c backend.bat

:: Optional delay to allow backend to start up properly
echo Waiting for backend to start...
timeout /t 5 /nobreak >nul

:: Start frontend.bat in a new terminal window
echo Starting frontend...
start cmd /c frontend.bat

:: Optional delay to allow frontend to start up properly
echo Waiting for frontend to start...
timeout /t 5 /nobreak >nul

:: Open the default browser to http://localhost:5173/
echo Opening default browser to http://localhost:5173/...
start http://localhost:5173/

echo All services started. Opening browser...
