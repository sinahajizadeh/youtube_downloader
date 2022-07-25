from PyQt5.QtWidgets import *
from y import Ui_MainWindow
import sys
from pytube import YouTube


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Youtube Downloader")
        self.buttondl.clicked.connect(self.yt_downloader)

    def yt_downloader(self):
        vidurl=self.lineEdit.text()

        if self.radioButton2video.isChecked():
            YouTube(vidurl).streams.first().download()

        elif self.radioButton1adio():
            YouTube(vidurl).streams.filter(only_audio=True).first().download()



if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    app.exec_()
