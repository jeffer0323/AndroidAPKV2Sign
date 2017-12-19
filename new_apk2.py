# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apkv2sign.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import os
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from signapk import BigWorkThread

class Ui_MainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(566, 672)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title1 = QtWidgets.QLabel(self.centralwidget)
        self.title1.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.title1.setStyleSheet("font: 75 11pt \"仿宋\";")
        self.title1.setScaledContents(False)
        self.title1.setWordWrap(False)
        self.title1.setObjectName("title1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 41, 16))
        self.label.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(130, 45, 321, 25))
        self.textBrowser.setObjectName("textBrowser")
        self.bt_pick_apk = QtWidgets.QPushButton(self.centralwidget)
        self.bt_pick_apk.setGeometry(QtCore.QRect(470, 45, 75, 25))
        self.bt_pick_apk.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_pick_apk.setObjectName("bt_pick_apk")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 131, 16))
        self.label_2.setStyleSheet("font: 75 11pt \"仿宋\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 54, 16))
        self.label_3.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 54, 16))
        self.label_4.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 200, 54, 16))
        self.label_5.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 240, 54, 16))
        self.label_6.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.label_6.setObjectName("label_6")
        self.tb_key = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb_key.setGeometry(QtCore.QRect(130, 115, 321, 25))
        self.tb_key.setObjectName("tb_key")
        self.bt_pick_key = QtWidgets.QPushButton(self.centralwidget)
        self.bt_pick_key.setGeometry(QtCore.QRect(470, 115, 75, 25))
        self.bt_pick_key.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_pick_key.setObjectName("bt_pick_key")
        self.key_pwd = QtWidgets.QLineEdit(self.centralwidget)
        self.key_pwd.setGeometry(QtCore.QRect(130, 155, 321, 25))
        self.key_pwd.setText("")
        self.key_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.key_pwd.setObjectName("key_pwd")
        self.alias = QtWidgets.QLineEdit(self.centralwidget)
        self.alias.setGeometry(QtCore.QRect(130, 195, 321, 25))
        self.alias.setText("")
        self.alias.setObjectName("alias")
        self.alias_pwd = QtWidgets.QLineEdit(self.centralwidget)
        self.alias_pwd.setGeometry(QtCore.QRect(130, 235, 321, 25))
        self.alias_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.alias_pwd.setObjectName("alias_pwd")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 280, 171, 16))
        self.label_7.setStyleSheet("font: 75 11pt \"仿宋\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 320, 81, 16))
        self.label_8.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.label_8.setObjectName("label_8")
        self.tb_signed = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb_signed.setGeometry(QtCore.QRect(130, 315, 321, 25))
        self.tb_signed.setLineWrapColumnOrWidth(2)
        self.tb_signed.setObjectName("tb_signed")
        self.bt_pick_signed = QtWidgets.QPushButton(self.centralwidget)
        self.bt_pick_signed.setGeometry(QtCore.QRect(470, 315, 75, 25))
        self.bt_pick_signed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_pick_signed.setObjectName("bt_pick_signed")
        self.bt_start_sign = QtWidgets.QPushButton(self.centralwidget)
        self.bt_start_sign.setGeometry(QtCore.QRect(180, 380, 171, 41))
        self.bt_start_sign.setObjectName("bt_start_sign")
        self.pb = QtWidgets.QProgressBar(self.centralwidget)
        self.pb.setGeometry(QtCore.QRect(30, 440, 511, 23))
        self.pb.setProperty("value", 0)
        self.pb.setTextVisible(False)
        self.pb.setObjectName("pb")
        self.tb_info = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb_info.setGeometry(QtCore.QRect(30, 480, 511, 131))
        self.tb_info.setObjectName("tb_info")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 23))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.bt_pick_apk.clicked.connect(self.choose_apk_file)
        self.bt_pick_key.clicked.connect(self.choose_sign_file)
        self.bt_pick_signed.clicked.connect(self.choose_signed_location)
        self.bt_start_sign.clicked.connect(self.start_sign)
        self.textBrowser.textChanged.connect(self.tv_apk_change)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def tv_apk_change(self):
        self.tb_signed.setText(self.textBrowser.toPlainText().replace('.apk', '_signed_v2.apk'))

    def choose_apk_file(self):
        fname = QFileDialog.getOpenFileName()
        self.textBrowser.setText(fname[0])

    def choose_sign_file(self):
        fname = QFileDialog.getOpenFileName()
        self.tb_key.setText(fname[0])

    def choose_signed_location(self):
        file_path = QFileDialog.getSaveFileName()
        self.tb_signed.setText(file_path[0])

    def start_sign(self):
        self.zip_align(self.textBrowser.toPlainText())


    def notify_ui(self, msg, number):
        self.tb_info.append(msg)
        self.pb.setValue(number)

    def zip_align(self, directory):
        if os.path.isfile("output_signed_v2.apk"):
            os.remove(os.getcwd() + os.sep + 'output_signed_v2.apk')
        zip_align_command = os.getcwd() + os.sep + 'zipalign.exe -v -p 4 ' + directory + ' output_signed_v2.apk'
        sub = subprocess.Popen(zip_align_command, stdout=subprocess.PIPE)
        stdout_value = sub.communicate()
        print((stdout_value[0]).decode('utf-8'))
        self.notify_ui((stdout_value[0]).decode('utf-8'), 50)
        self.apk_v2sign(self.tb_key.toPlainText(), self.alias.text(), self.key_pwd.text(), self.alias_pwd.text(),
                        self.tb_signed.toPlainText(), 'output_signed_v2.apk')

        #os.system(zip_align_command)

    def apk_v2sign(self, jks_name, jks_alias, jks_pwd, jks_alia_pwd, output_file, input_file):
        apk_v2sign_command = os.getcwd() + os.sep + 'apksigner.jar sign  --ks ' + jks_name + ' --ks-key-alias ' + jks_alias + '  --ks-pass pass:' + jks_pwd + ' --key-pass pass:' + jks_alia_pwd + ' --out ' + output_file + ' ' + input_file
        os.system(apk_v2sign_command)
        self.notify_ui('签名成功！', 100)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "安卓V2签名工具"))
        self.title1.setText(_translate("mainWindow", "1.选择要签名的APK："))
        self.label.setText(_translate("mainWindow", "APK："))
        self.bt_pick_apk.setText(_translate("mainWindow", "浏览..."))
        self.label_2.setText(_translate("mainWindow", "2.选择签名文件："))
        self.label_3.setText(_translate("mainWindow", "位置："))
        self.label_4.setText(_translate("mainWindow", "密码："))
        self.label_5.setText(_translate("mainWindow", "别名："))
        self.label_6.setText(_translate("mainWindow", "密码："))
        self.tb_key.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.bt_pick_key.setText(_translate("mainWindow", "浏览..."))
        self.key_pwd.setPlaceholderText(_translate("mainWindow", "请输入签名密码"))
        self.alias.setPlaceholderText(_translate("mainWindow", "请输入签名别名"))
        self.alias_pwd.setPlaceholderText(_translate("mainWindow", "请输入文件密码"))
        self.label_7.setText(_translate("mainWindow", "3.签名后apk存放路径："))
        self.label_8.setText(_translate("mainWindow", "签名后位置："))
        self.tb_signed.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.bt_pick_signed.setText(_translate("mainWindow", "浏览..."))
        self.bt_start_sign.setText(_translate("mainWindow", "开始签名"))

