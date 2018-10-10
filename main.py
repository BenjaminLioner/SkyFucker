# _*_ coding: utf-8 _*_
__author__ = "Carl Benjamin"
__date__ = "2018/10/8 15:42"

import os, sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from SkyFuckerUiMain import Ui_Form


class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # ###############################################
        self.startip_content = ''
        self.endip_content = ''
        self.start_port_content = ''
        self.end_port_content = ''
        self.users_file_path_content = ''
        self.passwords_file_path_content = ''
        self.result_file_path_content = ''

        # ###############################################
        self.getUserFile.clicked.connect(self.open_user_file)
        self.getPassFile.clicked.connect(self.open_pass_file)
        self.startButton.clicked.connect(self.test_variable)
        self.startip.textChanged.connect(self.get_start_ip)
        self.endip.textChanged.connect(self.get_end_ip)
        self.lineEdit.textChanged.connect(self.get_start_port)
        self.end_port.textChanged.connect(self.get_end_port)
        self.result_file_path.textChanged.connect(self.get_result_file_path)

    def open_user_file(self):
        user_file_path = QFileDialog.getOpenFileName(self, "选择用户字典文件", r"C:\Users\Administrator\Desktop",\
                                                     "Txt files(*.txt)")
        self.users_file_path.setText(str(user_file_path[0]))
        self.users_file_path_content = str(user_file_path[0])

    def open_pass_file(self):
        password_file_path =  QFileDialog.getOpenFileName(self, "选择密码字典文件", r"C:\Users\Administrator\Desktop",\
                                                     "Txt files(*.txt)")
        self.passwords_file_path.setText(str(password_file_path[0]))
        self.passwords_file_path_content = str(password_file_path[0])

    def get_start_ip(self):
        startip_content = str(self.startip.text())
        print(startip_content)
        self.startip_content  = startip_content
        # if startip_content == '起始IP':
        #     QMessageBox.information(self, "提示", self.tr('请正确输入起始IP'))
        #     self.label.setText("Information MessageBox")
        #     startip_content = self.startip.text()
        #     print(startip_content)

    def get_end_ip(self):
        endip_content = self.endip.text()
        self.endip_content = endip_content
        return endip_content

    def get_start_port(self):
        start_port = self.lineEdit.text()
        self.start_port_content = start_port
        return start_port

    def get_end_port(self):
        end_port_conten = self.end_port.text()
        self.end_port_content= end_port_conten

        return end_port_conten

    def get_user_file_path(self):
        user_file= self.users_file_path.text()
        self.users_file_path_content = user_file
        return user_file

    def get_pass_file_path(self):
        pass_file = self.passwords_file_path.text()
        self.passwords_file_path_content = pass_file
        return pass_file

    def get_result_file_path(self):
        result_file = self.result_file_path.text()
        self.result_file_path_content = result_file
        return result_file

    def test_variable(self):
        # self.set_value()
        # print(self.startip_content)
        # print(self.endip_content)
        # print(self.start_port_content)
        # print(self.end_port_content)
        # print(self.users_file_path_content)
        # print(self.passwords_file_path_content)
        # print(self.result_file_path_content)
        print(self.startip_content)
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())