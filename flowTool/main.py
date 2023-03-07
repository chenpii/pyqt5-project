import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from numpy import Inf

from flowtool import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, Qt

data = {
    "一、二级":
        {
            "工业建筑":
                {
                    "厂房":
                        {
                            "甲、乙": [15, 15, 20, 25, 30, 35],
                            "丙": [15, 15, 20, 25, 30, 40],
                            "丁、戊": [15, 15, 15, 15, 15, 20]
                        },
                    "仓库":
                        {
                            "甲、乙": [15, 15, 25, 25, '-', '-'],
                            "丙": [15, 15, 25, 25, 35, 45],
                            "丁、戊": [15, 15, 15, 15, 15, 20]
                        }
                },
            "民用建筑":
                {
                    "住宅": [15, 15, 15, 15, 15, 15],
                    "公共建筑":
                        {
                            "单层及多层": [15, 15, 15, 25, 30, 40],
                            "高层": ['-', '-', '-', 25, 30, 40]
                        }
                }
        },
    "三级":
        {
            "工业建筑":
                {
                    "乙、丙": [15, 20, 30, 40, 45, '-'],
                    "丁、戊": ['-', '-', '-', 20, 25, 35]
                },
            "单层及多层民用建筑": [15, 15, 20, 25, 30, '-']
        },
    "四级":
        {
            "丁、戊类工业建筑": [15, 15, 20, 25, '-', '-'],
            "单层及多层民用建筑": [15, 15, 20, 25, '-', '-']
        }
}

# 阈值区间
volumeRange = [[0, 1500], [1500, 3000], [3000, 5000], [5000, 20000], [20000, 50000], [50000, float(Inf)]]


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        for item in data.keys():
            self.listWidget_fireLevel.addItem(item)

        self.listWidget_fireLevel.itemClicked.connect(self.fireLevel_Clicked)
        self.listWidget_buildName.itemClicked.connect(self.buildName_Clicked)
        self.listWidget_buildType.itemClicked.connect(self.buildType_Clicked)
        self.listWidget_buildType2.itemClicked.connect(self.buildType2_Clicked)
        self.pushButton.clicked.connect(self.calculate)

    def fireLevel_Clicked(self, item):
        self.listWidget_buildName.clear()
        self.listWidget_buildType.clear()
        self.listWidget_buildType2.clear()
        self.buildName = data[item.text()]
        if (self.buildName != None and type(self.buildName) != list):
            self.listWidget_buildName.setEnabled(True)
            for item in self.buildName.keys():
                self.listWidget_buildName.addItem(item)
            self.listWidget_buildType.setEnabled(True)
            self.listWidget_buildType2.setEnabled(True)

        else:
            self.valueList = self.buildName
            self.listWidget_buildName.setEnabled(False)
            self.listWidget_buildType.setEnabled(False)
            self.listWidget_buildType2.setEnabled(False)

    def buildName_Clicked(self, item):
        self.listWidget_buildType.clear()
        self.listWidget_buildType2.clear()
        self.buildType = self.buildName[item.text()]
        if (self.buildType != None and type(self.buildType) != list):
            self.listWidget_buildType.setEnabled(True)
            for item in self.buildType.keys():
                self.listWidget_buildType.addItem(item)
            self.listWidget_buildType2.setEnabled(True)
        else:
            self.valueList = self.buildType
            self.listWidget_buildType.setEnabled(False)
            self.listWidget_buildType2.setEnabled(False)

    def buildType_Clicked(self, item):
        self.listWidget_buildType2.clear()
        self.buildType2 = self.buildType[item.text()]
        if (self.buildType2 != None and type(self.buildType2) != list):
            self.listWidget_buildType2.setEnabled(True)
            for item in self.buildType2.keys():
                self.listWidget_buildType2.addItem(item)
        else:
            self.valueList = self.buildType2
            self.listWidget_buildType2.setEnabled(False)

    def buildType2_Clicked(self, item):
        self.valueList = self.buildType2[item.text()]

    def calculate(self):
        if (len(self.listWidget_fireLevel.selectedItems()) == 0):
            QMessageBox.information(self, "提示", "请选择防火等级！", QMessageBox.Yes)
        elif (self.listWidget_buildName.isEnabled() and len(self.listWidget_buildName.selectedItems()) == 0):
            QMessageBox.information(self, "提示", "请选择建筑名称！", QMessageBox.Yes)
        elif (self.listWidget_buildType.isEnabled() and len(self.listWidget_buildType.selectedItems()) == 0):
            QMessageBox.information(self, "提示", "请选择建筑类型！", QMessageBox.Yes)
        elif (self.listWidget_buildType2.isEnabled() and len(self.listWidget_buildType2.selectedItems()) == 0):
            QMessageBox.information(self, "提示", "请选择建筑子类！", QMessageBox.Yes)
        else:
            try:
                self.volume = int(self.lineEdit_buildVolume.text())
                for subrange in volumeRange:
                    if (self.volume > subrange[0] and self.volume <= subrange[1]):
                        self.pipeFlow = self.valueList[volumeRange.index(subrange)]
                        break
                _translate = QtCore.QCoreApplication.translate
                self.label_pipeFlow.setText(_translate("MainWindow",
                                                       "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">" + str(
                                                           self.pipeFlow) + "</span></p></body></html>"))
            except Exception:
                QMessageBox.information(self, "提示", "建筑体积输入不合法！", QMessageBox.Yes)
                self.lineEdit_buildVolume.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
