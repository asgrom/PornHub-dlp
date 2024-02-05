import gi

# Запрос требуемых версий библиотек.
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw

from Source.MainWindow import MainWindow

import sys

# Приложение Adwaita.
class MyApp(Adw.Application):

	def __OnActivate(self, Application: Adw.Application):
		# Инициализация главного окна.
		self.win = MainWindow(application = Application)
		# Представление окна.
		self.win.present()

	# Конструктор.
	def __init__(self, **kwargs):
		# Наследование конструктора базового класса.
		super().__init__(**kwargs)
		# Подключение: при активации приложения.
		self.connect("activate", self.__OnActivate)

# Если точка входа – приложение.
if __name__ == "__main__":
	# Создание приложения.
	Application = MyApp()
	# Выполнение приложения.
	exit(Application.run(sys.argv))