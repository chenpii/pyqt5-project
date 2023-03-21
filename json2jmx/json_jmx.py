# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'json_jmx.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 450)
        MainWindow.setMinimumSize(QtCore.QSize(600, 450))
        MainWindow.setMaximumSize(QtCore.QSize(600, 450))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 541, 401))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_description = QtWidgets.QLabel(self.groupBox_3)
        self.label_description.setGeometry(QtCore.QRect(10, 20, 521, 91))
        self.label_description.setObjectName("label_description")
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 20, 441, 91))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_json_dir = QtWidgets.QLabel(self.layoutWidget1)
        self.label_json_dir.setObjectName("label_json_dir")
        self.horizontalLayout.addWidget(self.label_json_dir)
        self.lineEdit_json_dir = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_json_dir.setMinimumSize(QtCore.QSize(133, 20))
        self.lineEdit_json_dir.setObjectName("lineEdit_json_dir")
        self.horizontalLayout.addWidget(self.lineEdit_json_dir)
        self.pushButton_json_dir = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_json_dir.setObjectName("pushButton_json_dir")
        self.horizontalLayout.addWidget(self.pushButton_json_dir)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_jmx_dir = QtWidgets.QLabel(self.layoutWidget1)
        self.label_jmx_dir.setObjectName("label_jmx_dir")
        self.horizontalLayout_2.addWidget(self.label_jmx_dir)
        self.lineEdit_jmx_dir = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_jmx_dir.setMinimumSize(QtCore.QSize(133, 20))
        self.lineEdit_jmx_dir.setObjectName("lineEdit_jmx_dir")
        self.horizontalLayout_2.addWidget(self.lineEdit_jmx_dir)
        self.pushButton_jmx_dir = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_jmx_dir.setObjectName("pushButton_jmx_dir")
        self.horizontalLayout_2.addWidget(self.pushButton_jmx_dir)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.pushButton_trans = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_trans.setObjectName("pushButton_trans")
        self.verticalLayout_2.addWidget(self.pushButton_trans)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.textBrowser_logger = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_logger.setGeometry(QtCore.QRect(10, 20, 521, 91))
        self.textBrowser_logger.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.textBrowser_logger.setTabChangesFocus(False)
        self.textBrowser_logger.setUndoRedoEnabled(False)
        self.textBrowser_logger.setReadOnly(True)
        self.textBrowser_logger.setOverwriteMode(False)
        self.textBrowser_logger.setObjectName("textBrowser_logger")
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jmx自动生成工具"))
        self.groupBox_3.setTitle(_translate("MainWindow", "使用说明"))
        self.label_description.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">此工具实现.json接口文件转换成.jmx格式，方便接口自动化</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1<span style=\" font-weight:600;\">.</span>导出json文件。Yapi上选择按【swaggerjson】方式导出、swagger平台选择【OpenAPI】导出。</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.选择json目录和jmx文件保存目录。</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.点击转换。</p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Json_To_Jmx"))
        self.label_json_dir.setText(_translate("MainWindow", "Json目录："))
        self.pushButton_json_dir.setText(_translate("MainWindow", "浏览"))
        self.label_jmx_dir.setText(_translate("MainWindow", "保存目录："))
        self.pushButton_jmx_dir.setText(_translate("MainWindow", "浏览"))
        self.pushButton_trans.setText(_translate("MainWindow", "转换"))
        self.groupBox.setTitle(_translate("MainWindow", "日志"))
