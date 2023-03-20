import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from test_ui import Ui_MainWindow
import time
import random

class MyThread(QThread):
    #设置线程变量
    trigger = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)

    def run_(self, message):
        '''
        向信号trigger发送消息
        '''
        self.trigger.emit(message)


class Main(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.stop)


        self.threads = MyThread(self) #自定义线程类
        self.threads.trigger.connect(self.update_text)  #当信号接收到消息时，更新数据

        self.thread_no = 0 #序号

    def start(self):
        '''
        当点击start按键时日志栏中应显示start:序号
        '''
        self.thread_no += 1
        message = "start:{0}".format(self.thread_no)
        self.threads.run_(message)  # start the thread

    def stop(self):
        '''
        当点击stop按键时日志栏中应显示stop:序号
        '''
        self.thread_no += 1
        message = "stop:{0}".format(self.thread_no)
        self.threads.run_(message)  # start the thread

    def update_text(self, message):
        '''
        添加信息到日志栏中(即控件QTextBrowser中)
        '''
        self.textBrowser.append(message)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = Main()
    mainWindow.show()

    sys.exit(app.exec_())