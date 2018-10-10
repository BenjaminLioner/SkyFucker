# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FuckerBen.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(615, 574)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 611, 571))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 起始IP地址
        self.startip = QtWidgets.QLineEdit(self.layoutWidget)
        self.startip.setObjectName("startip")
        self.horizontalLayout.addWidget(self.startip)
        # 结束IP地址
        self.endip = QtWidgets.QLineEdit(self.layoutWidget)
        self.endip.setObjectName("endip")

        self.horizontalLayout.addWidget(self.endip)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.end_port = QtWidgets.QLineEdit(self.layoutWidget)
        self.end_port.setObjectName("end_port")
        self.horizontalLayout_4.addWidget(self.end_port)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.username_dict = QtWidgets.QLabel(self.layoutWidget)
        self.username_dict.setObjectName("username_dict")
        self.horizontalLayout_2.addWidget(self.username_dict)
        self.users_file_path = QtWidgets.QLineEdit(self.layoutWidget)
        self.users_file_path.setObjectName("users_file_path")
        self.horizontalLayout_2.addWidget(self.users_file_path)
        self.getUserFile = QtWidgets.QPushButton(self.layoutWidget)
        self.getUserFile.setObjectName("getUserFile")
        self.horizontalLayout_2.addWidget(self.getUserFile)
        self.password_dic = QtWidgets.QLabel(self.layoutWidget)
        self.password_dic.setObjectName("password_dic")
        self.horizontalLayout_2.addWidget(self.password_dic)
        self.passwords_file_path = QtWidgets.QLineEdit(self.layoutWidget)
        self.passwords_file_path.setObjectName("passwords_file_path")
        self.horizontalLayout_2.addWidget(self.passwords_file_path)
        self.getPassFile = QtWidgets.QPushButton(self.layoutWidget)
        self.getPassFile.setObjectName("getPassFile")
        self.horizontalLayout_2.addWidget(self.getPassFile)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.startButton = QtWidgets.QPushButton(self.layoutWidget)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_3.addWidget(self.startButton)
        self.endButton = QtWidgets.QPushButton(self.layoutWidget)
        self.endButton.setObjectName("endButton")
        self.horizontalLayout_3.addWidget(self.endButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        # 列表展示
        self.listWidget = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget.setObjectName("listWidget")

        self.verticalLayout_4.addWidget(self.listWidget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        # 选择保存文件
        self.choice_save_file = QtWidgets.QLabel(self.layoutWidget)
        self.choice_save_file.setObjectName("choice_save_file")

        self.horizontalLayout_5.addWidget(self.choice_save_file)
        # 保存结果文件路径
        self.result_file_path = QtWidgets.QLineEdit(self.layoutWidget)
        self.result_file_path.setObjectName("result_file_path")
        self.horizontalLayout_5.addWidget(self.result_file_path)
        # 选择结果文件按钮
        self.choice_result_file = QtWidgets.QPushButton(self.layoutWidget)
        self.choice_result_file.setObjectName("choice_result_file")
        self.horizontalLayout_5.addWidget(self.choice_result_file)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.startip.setText(_translate("Form", "起始IP"))
        self.endip.setText(_translate("Form", "结束IP"))
        self.lineEdit.setText(_translate("Form", "起始端口"))
        self.end_port.setText(_translate("Form", "结束端口"))
        self.username_dict.setText(_translate("Form", "用户名字典"))
        self.getUserFile.setText(_translate("Form", "选择文件"))
        self.password_dic.setText(_translate("Form", "密码字典"))
        self.getPassFile.setText(_translate("Form", "选择文件"))
        self.startButton.setText(_translate("Form", "开始爬取"))
        self.endButton.setText(_translate("Form", "停止爬取"))
        self.choice_save_file.setText(_translate("Form", "结果保存文件"))
        self.choice_result_file.setText(_translate("Form", "选择保存文件"))

