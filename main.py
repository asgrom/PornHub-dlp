from dublib.Methods import CheckPythonMinimalVersion, ReadJSON
from dublib.Terminalyzer import Command, Terminalyzer
from Source.Window import Window, Toolkits

import ctypes
import json
import sys
import os

#==========================================================================================#
# >>>>> ИНИЦИАЛИЗАЦИЯ СКРИПТА <<<<< #
#==========================================================================================#

# Проверка минимальной требуемой версии.
CheckPythonMinimalVersion(3, 10)
# Словарь важных значений.
VARIABLES = {
	"version": "1.4.0",
	"copyright": "Copyright © 2023-2024. DUB1401."
}

#==========================================================================================#
# >>>>> ЧТЕНИЕ НАСТРОЕК <<<<< #
#==========================================================================================#

# Чтение настроек.
Settings = ReadJSON("Settings.json")

# Если директория для загрузки не указана.
if Settings["downloads-directory"] == "":
	# Формирование пути.
	Settings["downloads-directory"] = os.getcwd() + "/Downloads"
	# Если стандартной папки не существует, создать.
	if os.path.exists("Downloads") == False: os.makedirs("Downloads")

#==========================================================================================#
# >>>>> НАСТРОЙКА ОБРАБОТЧИКА КОМАНД <<<<< #
#==========================================================================================#

# Список описаний обрабатываемых команд.
CommandsList = list()

# Создание команды: run.
COM_run = Command("run")
COM_run.add_flag_position(["qt", "gtk"])
CommandsList.append(COM_run)

# Инициализация обработчика консольных аргументов.
CAC = Terminalyzer()
# Получение информации о проверке команд. 
CommandDataStruct = CAC.check_commands(CommandsList)

#==========================================================================================#
# >>>>> ОБРАБОТКА КОМАНД <<<<< #
#==========================================================================================#

# Запуск стандартного окна.
WindowObject = Window(VARIABLES, Settings)
# Стандартная графическая библиотека.
Toolkit = Toolkits.Qt

# Обработка отсутствия команды.
if CommandDataStruct == None:
	# Запуск стандартного окна.
	WindowObject.show(Toolkit)

# Обработка команды: run
if CommandDataStruct.name == "run":
	# Если указана GTK, выполнить запуск с её использованием.
	if "gtk" in CommandDataStruct.flags: Toolkit = Toolkits.GTK
	# Запуск окна.
	WindowObject.show(Toolkit)