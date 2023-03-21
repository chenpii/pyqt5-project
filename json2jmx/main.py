import glob
import os
import sys
import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QMessageBox



from swaggerjmx.convert import conversion
from swaggerjmx.settings import Settings as ST

from json2jmx.json_jmx import Ui_MainWindow


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
        self.trigger.emit("[{0}] {1}".format(logger_time, message))


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
        self.str_path = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "")
        self.lineEdit_file_path.setText(self.str_path)
        message = "Json目录:{0}".format(self.str_path)
        self.threads.run_(message)
        self.Files = glob.glob(self.str_path + os.sep + "*.json")
        file_name = [file.split('\\')[-1] for file in self.Files]
        message = "读取到待转换的文件列表:{0}".format(file_name)
        self.threads.run_(message)

    def selectFiles(self):
        # 选择多个文件
        self.open_filenames = QtWidgets.QFileDialog.getOpenFileNames(None, '选择文件', '',
                                                                     'JSON Files (*.json);;All files(*.*)')
        message = "选择josn文件:{0}".format(self.open_filenames)
        self.threads.run_(message)

    def selectSaveFile(self):
        # 设置保存路径
        save_filename = QtWidgets.QFileDialog.getSaveFileName(None, "设置保存路径", "", "Jmeter脚本文件 (*.jmx)")
        QtWidgets.QFileDialog.getSaveFileUrl(None, "设置保存路径")
        message = "jmx保存完成:{0}".format(save_filename)
        self.threads.run_(message)
        return save_filename[0]

    def selectSavePath(self):
        # 设置保存路径
        self.save_file_path = QtWidgets.QFileDialog.getExistingDirectory(None, "设置保存路径", "")

        ST.swagger_url_json_path = ''
        ST.report_path = self.save_file_path
        for jsonFile in self.Files:
            file_name = jsonFile.split('\\')[-1]
            try:
                ST.swagger_url_json_path = (str(jsonFile))
                conversion()
                message = "{} 文件格式转换 成功!".format(file_name)
                self.threads.run_(message)
            except Exception as e:
                message = "{} 文件格式转换 失败! 请检查文件内容。".format(file_name)
                QMessageBox.information(self, "提示", message, QMessageBox.Yes)
                self.threads.run_(message)


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
