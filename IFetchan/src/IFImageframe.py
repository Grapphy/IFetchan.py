from PyQt5 import QtWidgets, QtCore, QtGui

from .IFFourchan import FourchanImage


class ImageThumbnailFrame(QtWidgets.QGroupBox):
    def __init__(
        self, scrollAreaWidgetContents, fimage: FourchanImage, thumbytes: bytes
    ) -> None:
        super().__init__(scrollAreaWidgetContents)

        self.fimage = fimage

        self.setMinimumSize(QtCore.QSize(150, 150))
        self.setMaximumSize(QtCore.QSize(150, 150))
        self.setStyleSheet(
            "color: rgb(255, 255, 255);background-color: rgb(30, 30, 30);"
        )
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setTitle(fimage.filename)
        self.setCheckable(True)
        self.setFlat(True)

        self.PicRelated = QtGui.QPixmap()
        self.PicRelated.loadFromData(thumbytes)
        self.ImageFourchan = QtWidgets.QLabel(self)
        self.ImageFourchan.setGeometry(QtCore.QRect(10, 20, 120, 120))
        self.ImageFourchan.setText("")
        self.ImageFourchan.setPixmap(self.PicRelated)
        self.ImageFourchan.setScaledContents(True)
        self.ImageFourchan.setObjectName("ImageFourchan")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.addWidget(self.ImageFourchan)
