from Source.GUI.Qt.QtWindow import QtWindow
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtGui

import ctypes
import enum
import sys

#==========================================================================================#
# >>>>> ДОПОЛНИТЕЛЬНЫЕ ТИПЫ ДАННЫХ <<<<< #
#==========================================================================================#

# Типы графических библиотек.
class Toolkits(enum.Enum):
	GTK = "gtk"
	Qt = "qt"

#==========================================================================================#
# >>>>> ОСНОВНОЙ КЛАСС <<<<< #
#==========================================================================================#

# Дескриптор окна.
class Window:

	# Сворачивает терминал Windows.
	def __MinimizeCMD(self):
		# Если не включён режим отладки, свернуть консоль.
		if self.__Settings["debug"] == False and sys.platform == "win32": ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

	# Инициализирует приложение Qt.
	def __InitApplication_Qt(self):
		# Создание экземпляра приложения.
		self.__Application = QApplication(sys.argv)
		# Настройка внешнего вида.
		self.__Application.setStyle("Fusion")
		self.__Application.setWindowIcon(QtGui.QIcon("icon.ico"))
		# Создание окна.
		self.__Window = QtWindow(self.__Application, self.__Veriables, self.__Settings)

	# Конструктор.
	def __init__(self, variables: dict, settings: dict):

		#---> Генерация динамических свойств.
		#==========================================================================================#
		# Словарь важных значений.
		self.__Veriables = variables
		# Глобальные настройки.
		self.__Settings = settings
		# Экзмепляр приложения.
		self.__Application = None
		# Экземпляр окна.
		self.__Window = None
		
	# Отображает окно.
	def show(self, toolkit: Toolkits) -> int:
		# Код завершения.
		ExitCode = 0

		# Если используется Qt:
		if toolkit == Toolkits.Qt:
			# Инициализация приложения.
			self.__InitApplication_Qt()
			# Открытие окна.
			self.__Window.show()
			# Сворачивание терминала на Windows.
			self.__MinimizeCMD()
			# Запуск приложения Qt.
			ExitCode = self.__Application.exec()

		# Если используется GTK:
		if toolkit == Toolkits.GTK:
			# Если используется ОС семейства Windows, выбросить исключение.
			if sys.platform == "win32": raise ImportError("GTK isn't support on Windows.")

		return ExitCode