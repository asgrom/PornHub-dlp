from dublib.Methods import ReadJSON

import ctypes
import locale
import sys 

# Словарь локализаций.
LOCALES = ReadJSON("Source/GUI/Qt/Locales.json")

# Текущая локализация.
CURRENT_LOCALE = LOCALES["EN"]
# Тег текущего языка.
LanguageTag = None

# Если устройство работает под управлением ОС семейства Linux.
if sys.platform in ["linux", "linux2"]:
	# Получение тега текущего языка.
	LanguageTag = locale.getlocale()[0].split('_')[0].upper()

# Если устройство работает под управлением ОС семейства Windows.
elif sys.platform == "win32":
	# Получение сведений о системе Windows.
	WinDLL = ctypes.windll.kernel32
	WinDLL.GetUserDefaultUILanguage()
	# Получение тега текущего языка.
	LanguageTag = locale.windows_locale[WinDLL.GetUserDefaultUILanguage()].split('_')[0].upper()

# Если существует локализация, переключиться на неё.
if LanguageTag in LOCALES.keys():
    CURRENT_LOCALE = LOCALES[LanguageTag]