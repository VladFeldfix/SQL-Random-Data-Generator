set "currentDirectory=%cd%
pyinstaller --distpath %currentDirectory% -i favicon.ico --onefile SQL-RANDOM-DATA-GENERATOR.py
pause