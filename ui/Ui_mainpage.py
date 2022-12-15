# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\Project\KingOfEfficiency\ui\qtui\mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(659, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.btn_add)
        self.btn_from_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_from_file.setObjectName("btn_from_file")
        self.horizontalLayout.addWidget(self.btn_from_file)
        self.btn_del = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del.setObjectName("btn_del")
        self.horizontalLayout.addWidget(self.btn_del)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cob_sreach_index = QtWidgets.QComboBox(self.widget)
        self.cob_sreach_index.setObjectName("cob_sreach_index")
        self.horizontalLayout_2.addWidget(self.cob_sreach_index)
        self.lineEdit_sreach_content = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_sreach_content.setObjectName("lineEdit_sreach_content")
        self.horizontalLayout_2.addWidget(self.lineEdit_sreach_content)
        self.btn_sreach = QtWidgets.QPushButton(self.widget)
        self.btn_sreach.setObjectName("btn_sreach")
        self.horizontalLayout_2.addWidget(self.btn_sreach)
        self.gridLayout.addWidget(self.splitter, 0, 2, 1, 1)
        self.tableView_main = QtWidgets.QTableView(self.centralwidget)
        self.tableView_main.setObjectName("tableView_main")
        self.gridLayout.addWidget(self.tableView_main, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "效率之王"))
        self.btn_add.setText(_translate("MainWindow", "增加"))
        self.btn_from_file.setText(_translate("MainWindow", "文件导入..."))
        self.btn_del.setText(_translate("MainWindow", "删除"))
        self.btn_sreach.setText(_translate("MainWindow", "搜索"))
