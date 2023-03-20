import sys
import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from json2jmx import Ui_MainWindow


class MyThread(QThread):
    # 设置线程变量
    trigger = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)

    def run_(self, message):
        '''
        向信号trigger发送消息
        '''
        logger_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(time.time()))
        self.trigger.emit("[{0}]:{1}".format(logger_time, message))


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_file_path.clicked.connect(self.selectPath)
        self.pushButton_json2jmx.clicked.connect(self.selectSavePath)

        self.threads = MyThread(self)  # 自定义线程类
        self.threads.trigger.connect(self.update_text)  # 当信号接收到消息时，更新数据

    def selectPath(self):
        # 选择文件夹
        str_path = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "")
        self.lineEdit_file_path.setText(str_path)
        message = "选择了Json目录:{0}".format(str_path)
        self.threads.run_(message)  # start the thread
        # return str_path

    def selectFiles(self):
        # 选择多个文件
        open_filenames = QtWidgets.QFileDialog.getOpenFileNames(None, '选择文件', '', 'JSON Files (*.json);;All files(*.*)')
        print(open_filenames)
        message = "选择josn文件:{0}".format(open_filenames)
        self.threads.run_(message)  # start the thread
        return open_filenames

    def selectSavePath(self):
        # 设置保存路径
        save_filename = QtWidgets.QFileDialog.getSaveFileName(None, "设置保存路径", "", "Jmeter脚本文件 (*.jmx)")
        QtWidgets.QFileDialog.getSaveFileUrl(None, "设置保存路径")
        # print(save_filename)
        message = "jmx保存完成:{0}".format(save_filename)
        return save_filename[0]

    def update_text(self, message):
        '''
        添加信息到日志栏中(即控件QTextBrowser中)
        '''
        self.textBrowser_logger.append(message)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
