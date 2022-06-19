from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QComboBox, QLCDNumber, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QTimeEdit,
    QWidget, QMessageBox)

from qt_material import apply_stylesheet

import sys
from __init__ import *

class Ui_Form(QWidget):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(800, 480)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(-4, -1, 800, 480))
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.view = QWidget()
        self.view.setObjectName(u"view")
        self.label = QLabel(self.view)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 101, 21))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label_2 = QLabel(self.view)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(740, 20, 53, 16))
        self.lcdNumber = QLCDNumber(self.view)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(120, 12, 611, 31))
        self.label_3 = QLabel(self.view)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 350, 101, 21))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.view)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(740, 350, 53, 16))
        self.lcdNumber_2 = QLCDNumber(self.view)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(120, 342, 611, 31))
        self.tabWidget.addTab(self.view, "")
        self.control = QWidget()
        self.control.setObjectName(u"control")
        self.feed = QPushButton(self.control) # feed a unit
        self.feed.setObjectName(u"feed")
        self.feed.setGeometry(QRect(40, 30, 90, 40))
        self.update_ = QPushButton(self.control)
        self.update_.setObjectName(u"update_") # update feed plans
        self.update_.setGeometry(QRect(400, 30, 125, 40))
        self.comboBox = QComboBox(self.control)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(530, 30, 71, 31))
        self.flush = QPushButton(self.control)
        self.flush.setObjectName(u"flush")
        self.flush.setGeometry(530, 150, 90, 40)
        # self.comboBox.
        self.timeEdit = QTimeEdit(self.control)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(410, 90, 118, 42))
        self.add = QPushButton(self.control)
        self.add.setObjectName(u"add") # add feed plans
        self.add.setGeometry(QRect(50, 360, 125, 40))
        self.timeEdit_2 = QTimeEdit(self.control)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setGeometry(QRect(180, 360, 118, 42))
        self.drop = QPushButton(self.control)
        self.drop.setObjectName(u"drop") # drop feed plans
        self.drop.setGeometry(QRect(480, 360, 125, 40))
        self.comboBox_2 = QComboBox(self.control)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(607, 450, 69, 31))
        self.tabWidget.addTab(self.control, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(Form)
    
    # def refresh(self)
    
    @pyqtSlot()
    def feed_func(self):
        waiting.add_waiting(0, 1)
        QMessageBox.information(self, '成功', '喂食成功')

    @pyqtSlot()
    def add_func(self):
        feed_time = self.timeEdit_2.text()
        # * QMessageBox.information(self, 'test', feed_time)
        plans.add_plan(feed_time, 0, 12) #TODO: Add the function of changing the number of unit(s).
        QMessageBox.information(self, '成功', '添加计划成功')

    @pyqtSlot()
    def update_func(self):
        choose = self.comboBox.currentText()
        time = self.timeEdit.text()
        plans.update_plan(choose, time, 0, 12)
        QMessageBox.information(self, '成功', '修改计划成功')

    @pyqtSlot()
    def flush_func(self):
        all_plans = plans.get_all_plans()
        self.comboBox.clear()
        for plan in all_plans:
            self.comboBox.addItem(plan['uuid'])

    @pyqtSlot()
    def delete_func(self):
        choose = self.comboBox.currentText()
        plans.delete_plan(choose)
        QMessageBox.information(self, '成功', '删除计划成功')

    # setupUi
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u7cae\u4ed3\u4f59\u91cf\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4efd", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u5582\u98df\u603b\u91cf\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u4efd", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.view), QCoreApplication.translate("Form", u"\u72b6\u6001", None))
        self.feed.setText(QCoreApplication.translate("Form", u"\u51fa\u7cae1\u4efd", None))
        self.update_.setText(QCoreApplication.translate("Form", u"\u6539\u53d8\u5582\u98df\u8ba1\u5212", None))
        self.add.setText(QCoreApplication.translate("Form", u"\u589e\u52a0\u5582\u98df\u8ba1\u5212", None))
        self.drop.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u5582\u98df\u8ba1\u5212", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.control), QCoreApplication.translate("Form", u"\u63a7\u5236", None))
        self.flush.setText(QCoreApplication.translate("Form", u"刷新", None))
    # retranslateUi

app = QApplication(sys.argv)
main = QMainWindow()
test = Ui_Form()
test.setupUi(main)
main.showFullScreen()

test.feed.clicked.connect(test.feed_func)
test.add.clicked.connect(test.add_func)
test.flush.clicked.connect(test.flush_func)
test.update_.clicked.connect(test.update_func)
test.drop.clicked.connect(test.delete_func)

apply_stylesheet(app, theme='dark_blue.xml')

app.exec_()
