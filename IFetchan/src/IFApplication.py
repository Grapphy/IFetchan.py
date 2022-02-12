import asyncio

from PyQt5 import QtCore, QtGui, QtWidgets

from .IFMainwindow import Ui_MainWindow
from .IFImageframe import ImageThumbnailFrame
from .IFFourchan import FourchanImage, get_thread_pictures, get_bytes_from_url

from typing import List


class NetworkSignals(QtCore.QObject):
    addNewFrame = QtCore.pyqtSignal(FourchanImage, bytes)
    setProgressBar = QtCore.pyqtSignal(int)
    increaseProgressBar = QtCore.pyqtSignal(str)
    taskFinished = QtCore.pyqtSignal()


class IFetchan(Ui_MainWindow):
    def __init__(self, mainwindow, /) -> None:
        self._x = 0
        self._y = 0
        self.setupUi(mainwindow)
        self.__connect_slots()
        self.__connect_signals()
        self.image_frames: List[ImageThumbnailFrame] = []

    def __connect_slots(self) -> None:
        self.load_pushButton.clicked.connect(self._load_images)
        self.clear_pushButton.clicked.connect(self._clear_images)
        self.output_lineEdit.clicked.connect(self._set_output_folder)
        self.download_pushButton.clicked.connect(self._download_images)

    def __connect_signals(self) -> None:
        self.signals = NetworkSignals()
        self.signals.addNewFrame.connect(self.createImageFrame)
        self.signals.setProgressBar.connect(
            lambda x: self.status_progressBar.setMaximum(x)
        )
        self.signals.increaseProgressBar.connect(self._increment_progress_bar)
        self.signals.taskFinished.connect(self._task_finished)

    async def __load_images(self, board: str, thread_id: str) -> None:
        images = await get_thread_pictures(board, thread_id)
        self.signals.setProgressBar.emit(len(images))
        for image in images:
            self.signals.addNewFrame.emit(
                image, await get_bytes_from_url(image.thumbnail_url)
            )
            self.signals.increaseProgressBar.emit(f"Loaded {image.filename}")
        self.signals.taskFinished.emit()

    async def __download_images(self) -> None:
        output_folder = self.output_lineEdit.text() or "."
        checked_frames = [i for i in self.image_frames if i.isChecked()]
        self.signals.setProgressBar.emit(len(checked_frames))
        for imgf in checked_frames:
            imgbytes = await get_bytes_from_url(imgf.fimage.full_url)
            with open(f"{output_folder}/{imgf.fimage.filename}", "wb") as i:
                i.write(imgbytes)
            self.signals.increaseProgressBar.emit(
                f"Downloaded {imgf.fimage.filename}"
            )
        self.signals.taskFinished.emit()

    def _load_images(self) -> None:
        if self.thread_lineEdit.text():
            thread_board = self.thread_lineEdit.text().split("/")[-3]
            thread_id = self.thread_lineEdit.text().split("/")[-1]
            asyncio.ensure_future(self.__load_images(thread_board, thread_id))

    def _download_images(self) -> None:
        asyncio.ensure_future(self.__download_images())

    def _task_finished(self) -> None:
        self.status_progressBar.setValue(0)
        self.status_progressBar.setFormat("")
        if len(self.image_frames):
            self.clear_pushButton.setEnabled(True)
            self.download_pushButton.setEnabled(True)

    def _clear_images(self) -> None:
        while self.gridLayout_3.count():
            child = self.gridLayout_3.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()

        self._x = 0
        self._y = 0
        self.image_frames = []
        self.clear_pushButton.setEnabled(False)
        self.download_pushButton.setEnabled(False)

    def _set_output_folder(self) -> None:
        output_folder = QtWidgets.QFileDialog.getExistingDirectory()
        self.output_lineEdit.setText(output_folder)

    def createImageFrame(
        self, fimage: FourchanImage, thumbytes: bytes
    ) -> None:
        imgf = ImageThumbnailFrame(
            self.scrollAreaWidgetContents, fimage, thumbytes
        )
        self.gridLayout_3.addWidget(imgf, self._y, self._x, 1, 1)
        self._x += 1
        if self._x == 6:
            self._y += 1
            self._x = 0
        self.image_frames.append(imgf)

    def _increment_progress_bar(self, msg: str) -> None:
        self.status_progressBar.setValue(self.status_progressBar.value() + 1)
        self.status_progressBar.setFormat(msg)
