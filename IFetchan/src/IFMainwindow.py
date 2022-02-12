from PyQt5 import QtCore, QtGui, QtWidgets


class ClickableLineEdit(QtWidgets.QLineEdit):
    clicked = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()
        else:
            super().mousePressEvent(event)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1001, 681)
        MainWindow.setMaximumSize(QtCore.QSize(1001, 682))
        MainWindow.setWindowTitle("IFetchan - Fourchan Image Fetch")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("./src/includes/Icon.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bottom_frame = QtWidgets.QFrame(self.centralwidget)
        self.bottom_frame.setGeometry(QtCore.QRect(10, 80, 981, 591))
        self.bottom_frame.setStyleSheet(
            ".QFrame{\n"
            "    background-color: rgb(30, 30, 30);\n"
            "    border: 1px solid rgb(62, 57, 80);\n"
            "    border-left: black;\n"
            "    border-color: rgb(66, 66, 66);\n"
            "    border-bottom-left-radius: 10px;\n"
            "    border-bottom-right-radius: 10px;\n"
            "}"
        )
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.frames_scrollArea = QtWidgets.QScrollArea(self.bottom_frame)
        self.frames_scrollArea.setGeometry(QtCore.QRect(10, 120, 961, 461))
        self.frames_scrollArea.setStyleSheet(
            "background-color: rgb(30, 30, 30);\n" "color: rgb(255, 255, 255);"
        )
        self.frames_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frames_scrollArea.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded
        )
        self.frames_scrollArea.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.frames_scrollArea.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.frames_scrollArea.setWidgetResizable(True)
        self.frames_scrollArea.setObjectName("frames_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 961, 461))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(
            self.scrollAreaWidgetContents
        )
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frames_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.top_frame = QtWidgets.QFrame(self.centralwidget)
        self.top_frame.setGeometry(QtCore.QRect(10, 10, 981, 111))
        self.top_frame.setStyleSheet(
            ".QFrame{\n"
            "    background-color: rgb(36, 36, 36);\n"
            "    border: 1px solid rgb(62, 57, 80);\n"
            "    border-top-left-radius: 10px;\n"
            "    border-top-right-radius: 10px;\n"
            "    border-color: rgb(66, 66, 66);\n"
            "}"
        )
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.download_pushButton = QtWidgets.QPushButton(self.top_frame)
        self.download_pushButton.setEnabled(False)
        self.download_pushButton.setGeometry(QtCore.QRect(260, 70, 140, 31))
        self.download_pushButton.setStyleSheet(
            ".QPushButton{\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color: rgb(41, 41, 41);\n"
            "    border: 1px solid rgb(44, 44, 44);\n"
            "    border-radius: 5px;\n"
            '    font: 10pt "Berlin Sans";\n'
            "}\n"
            "\n"
            ".QPushButton:hover {\n"
            "    background-color: rgb(31, 31, 31);\n"
            "}\n"
            "\n"
            ".QPushButton:pressed {\n"
            "    background-color: rgb(25, 25, 25);\n"
            "}\n"
            "\n"
            ".QPushButton:disabled{\n"
            "    color: rgb(117, 117, 117);\n"
            "    background-color: rgb(38, 38, 38);\n"
            "}"
        )
        self.download_pushButton.setObjectName("download_pushButton")
        self.clear_pushButton = QtWidgets.QPushButton(self.top_frame)
        self.clear_pushButton.setEnabled(False)
        self.clear_pushButton.setGeometry(QtCore.QRect(570, 70, 140, 31))
        self.clear_pushButton.setStyleSheet(
            ".QPushButton{\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color: rgb(41, 41, 41);\n"
            "    border: 1px solid rgb(44, 44, 44);\n"
            "    border-radius: 5px;\n"
            '    font: 10pt "Berlin Sans";\n'
            "}\n"
            "\n"
            ".QPushButton:hover {\n"
            "    background-color: rgb(31, 31, 31);\n"
            "}\n"
            "\n"
            ".QPushButton:pressed {\n"
            "    background-color: rgb(25, 25, 25);\n"
            "}\n"
            "\n"
            ".QPushButton:disabled{\n"
            "    color: rgb(117, 117, 117);\n"
            "    background-color: rgb(38, 38, 38);\n"
            "}"
        )
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.thread_lineEdit = QtWidgets.QLineEdit(self.top_frame)
        self.thread_lineEdit.setGeometry(QtCore.QRect(10, 70, 231, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush
        )
        self.thread_lineEdit.setPalette(palette)
        self.thread_lineEdit.setStyleSheet(
            ".QLineEdit {\n"
            "    background-color: rgb(41, 41, 41);\n"
            "    border: 1px solid rgb(44, 44, 44);\n"
            "    border-radius: 2px;\n"
            "    border-bottom-color: rgb(152, 152, 152);\n"
            '    font: 10pt "Berlin Sans";\n'
            "    padding-left: 7;\n"
            "}\n"
            "\n"
            ".QLineEdit:hover {\n"
            "    background-color: rgb(31, 31, 31);\n"
            "}"
        )
        self.thread_lineEdit.setText("")
        self.thread_lineEdit.setObjectName("thread_lineEdit")
        self.output_lineEdit = ClickableLineEdit(self.top_frame)
        self.output_lineEdit.setGeometry(QtCore.QRect(730, 70, 241, 31))
        self.output_lineEdit.setStyleSheet(
            ".ClickableLineEdit {\n"
            "    color: gray;\n"
            "    background-color: rgb(41, 41, 41);\n"
            "    border: 1px solid rgb(44, 44, 44);\n"
            "    border-radius: 2px;\n"
            "    border-bottom-color: rgb(112, 112, 112);\n"
            '    font: 10pt "Berlin Sans";\n'
            "    padding-left: 7;\n"
            "}\n"
            "\n"
            ".ClickableLineEdit:hover {\n"
            "    background-color: rgb(31, 31, 31);\n"
            "}"
        )
        self.output_lineEdit.setText("")
        self.output_lineEdit.setReadOnly(True)
        self.output_lineEdit.setObjectName("output_lineEdit")
        self.load_pushButton = QtWidgets.QPushButton(self.top_frame)
        self.load_pushButton.setGeometry(QtCore.QRect(415, 70, 140, 31))
        self.load_pushButton.setStyleSheet(
            ".QPushButton{\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color: rgb(41, 41, 41);\n"
            "    border: 1px solid rgb(44, 44, 44);\n"
            "    border-radius: 5px;\n"
            '    font: 10pt "Berlin Sans";\n'
            "}\n"
            "\n"
            ".QPushButton:hover {\n"
            "    background-color: rgb(31, 31, 31);\n"
            "}\n"
            "\n"
            ".QPushButton:pressed {\n"
            "    background-color: rgb(25, 25, 25);\n"
            "}\n"
            "\n"
            ".QPushButton:disabled{\n"
            "    color: rgb(117, 117, 117);\n"
            "    background-color: rgb(38, 38, 38);\n"
            "}"
        )
        self.load_pushButton.setObjectName("load_pushButton")
        self.title_label = QtWidgets.QLabel(self.top_frame)
        self.title_label.setGeometry(QtCore.QRect(240, 10, 491, 41))
        self.title_label.setStyleSheet(
            'font: 20pt "Segoe UI";\n' "color: rgb(255, 255, 255);"
        )
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.loader_frame = QtWidgets.QFrame(self.centralwidget)
        self.loader_frame.setGeometry(QtCore.QRect(250, 120, 491, 61))
        self.loader_frame.setStyleSheet(
            ".QFrame{\n"
            "    background-color: rgb(36, 36, 36);\n"
            "    border: 1px solid rgb(36, 36, 36);\n"
            "    border-bottom-left-radius: 10px;\n"
            "    border-bottom-right-radius: 10px;\n"
            "    border-left-color: rgb(66, 66, 66);\n"
            "    border-bottom-color: rgb(66, 66, 66);\n"
            "    border-right-color: rgb(66, 66, 66);\n"
            "}"
        )
        self.loader_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loader_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loader_frame.setObjectName("loader_frame")
        self.status_progressBar = QtWidgets.QProgressBar(self.loader_frame)
        self.status_progressBar.setGeometry(QtCore.QRect(20, 9, 451, 31))
        self.status_progressBar.setStyleSheet(
            ".QProgressBar {\n"
            "    background-color: rgb(68, 68, 68);\n"
            "    color: white;    \n"
            "    border-style: outset;\n"
            "    border-width: 2px;\n"
            "    border-color: rgb(103, 103, 103);\n"
            "    border-radius: 7px;\n"
            "}\n"
            "\n"
            ".QProgressBar::chunk {\n"
            "    background-color: rgb(145, 180, 161) ; \n"
            "    border-style: outset;\n"
            "    border-width: 2px;\n"
            "    border-color: rgb(103, 103, 103);\n"
            "    border-radius: 7px;\n"
            "}"
        )
        self.status_progressBar.setProperty("value", 0)
        self.status_progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.status_progressBar.setInvertedAppearance(False)
        self.status_progressBar.setObjectName("status_progressBar")
        self.status_progressBar.setFormat("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IFetchan.py"))
        self.download_pushButton.setText(_translate("MainWindow", "Download"))
        self.clear_pushButton.setText(_translate("MainWindow", "Clear"))
        self.thread_lineEdit.setPlaceholderText(
            _translate(
                "MainWindow",
                "Ex: https://boards.4channel.org/c/thread/147251021",
            )
        )
        self.output_lineEdit.setPlaceholderText(
            _translate("MainWindow", "Click to set output folder ...")
        )
        self.load_pushButton.setText(_translate("MainWindow", "Load files"))
        self.title_label.setText(_translate("MainWindow", "4chan Image Fetch"))
