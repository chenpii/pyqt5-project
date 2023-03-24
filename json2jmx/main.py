# -*- coding: utf-8 -*-
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

        self.pushButton_json_dir.clicked.connect(self.selectJsonPath)
        self.pushButton_trans.clicked.connect(self.selectSaveJmx)

        self.threads = MyThread(self)  # 自定义线程类
        self.threads.trigger.connect(self.update_text)  # 当信号接收到消息时，更新数据

    def selectJsonPath(self):
        # 选择Json文件夹
        json_dir = QtWidgets.QFileDialog.getExistingDirectory(None, "选取Json文件夹", "")
        if ('' != json_dir):
            self.lineEdit_json_dir.setText(json_dir)

    def selectSaveJmx(self):
        # 保存Jmx文件

        json_dir = self.lineEdit_json_dir.text()
        if ('' == json_dir):
            self.threads.run_("Json目录不合法！")
            return

        message = "Json目录:{0}".format(json_dir)
        self.threads.run_(message)
        Files = glob.glob(json_dir + os.sep + "*.json")
        filename_list = [file.split('\\')[-1] for file in Files]
        if (len(filename_list) == 0):
            # self.threads.run_("目录下不存在json文件！")
            QMessageBox.information(self, "提示", "未找到json文件，请检查Json目录！", QMessageBox.Ok)
            return
        self.threads.run_("读取到Json文件：{0}".format(filename_list))

        jmx_dir = QtWidgets.QFileDialog.getExistingDirectory(None, "保存Jmx路径", "")
        if ('' == jmx_dir): return


        ST.swagger_url_json_path = ''
        ST.report_path = jmx_dir
        trans_result = True

        for jsonFile in Files:
            file_name = jsonFile.split('\\')[-1]
            try:
                ST.swagger_url_json_path = (str(jsonFile))
                conversion()
                message = "【{}】 文件格式转换 成功！".format(file_name)
                self.threads.run_(message)
            except Exception as e:
                message = "【{}】 文件格式转换 失败！请检查文件内容。".format(file_name)
                self.threads.run_(message)
                trans_result = False

        message = "文件保存至：【{0}】".format(jmx_dir)
        self.threads.run_(message)

        if (trans_result):
            message = "转换成功！"
        else:
            message = "存在转换失败的文件，请检查文件内容！"
        QMessageBox.information(self, "提示", message, QMessageBox.Ok)

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
