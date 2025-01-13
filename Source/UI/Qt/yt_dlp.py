from Source.Core.Downloader import VideoDownloader

from PyQt6.QtCore import QObject, pyqtSignal

class yt_dlp(QObject):
	"""Потоковый обработчик взаимодейтсвий с библиотекой yt-dlp."""

	finished = pyqtSignal(int)

	def __init__(self, directory: str, link: str, sorting: bool, quality: str):
		"""
		Потоковый обработчик взаимодейтсвий с библиотекой pornhub_dl.
			directory — каталог загрузок;\n
			link — ссылка на видео;\n
			sorting — переключает сортировку по автору;\n
			quality — предпочитаемое качество.
		"""

		super().__init__()

		#---> Генерация статических атрибутов.
		#==========================================================================================#
		self.__SaveDirectory = directory
		self.__Link = link
		self.__SortByUploader = sorting
		self.__Quality = quality

		self.__Downloader = VideoDownloader()
		self.__Downloader.enable_sorting(self.__SortByUploader)

	def run(self):
		"""Запускает процесс скачивания."""
		
		Status = self.__Downloader.download_video(self.__Link, self.__Quality)
		self.finished.emit(Status.code)