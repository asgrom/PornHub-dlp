:: Переход в директорию проекта.
cd ..\..\

:: Сборка приложения.
pyinstaller --distpath %~dp0\Release --i icon.ico --version-file Build\Windows\metadata.txt --onefile main.py --name pornhub-dl

:: Копирование в директорию сборки необходимых компонентов приложения.
xcopy /Y /I Source\GUI\Qt\Locales.json Build\Windows\Release\Source\GUI\Qt\
xcopy /Y /I yt-dlp Build\Windows\Release\yt-dlp
xcopy /Y Advertisement.gif Build\Windows\Release
xcopy /Y icon.ico Build\Windows\Release
xcopy /Y Settings.json Build\Windows\Release

:: Удаление файлов сборки приложения.
rmdir /q /s Build\pornhub-dl