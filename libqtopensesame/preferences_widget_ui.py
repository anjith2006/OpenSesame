# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/preferences_widget.ui'
#
# Created: Sun May 29 15:09:20 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(555, 572)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 522, 553))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout_3.setContentsMargins(0, -1, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.checkbox_immediately_rename = QtGui.QCheckBox(self.groupBox_2)
        self.checkbox_immediately_rename.setObjectName("checkbox_immediately_rename")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkbox_immediately_rename)
        self.checkbox_autoresponse = QtGui.QCheckBox(self.groupBox_2)
        self.checkbox_autoresponse.setObjectName("checkbox_autoresponse")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.checkbox_autoresponse)
        self.checkbox_show_random_tips = QtGui.QCheckBox(self.groupBox_2)
        self.checkbox_show_random_tips.setObjectName("checkbox_show_random_tips")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.checkbox_show_random_tips)
        self.checkbox_toolbar_text = QtGui.QCheckBox(self.groupBox_2)
        self.checkbox_toolbar_text.setObjectName("checkbox_toolbar_text")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.checkbox_toolbar_text)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_2.setContentsMargins(0, 9, 0, 0)
        self.formLayout_2.setHorizontalSpacing(6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.checkbox_enable_autosave = QtGui.QCheckBox(self.groupBox)
        self.checkbox_enable_autosave.setObjectName("checkbox_enable_autosave")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkbox_enable_autosave)
        self.label_autosave_interval = QtGui.QLabel(self.groupBox)
        self.label_autosave_interval.setObjectName("label_autosave_interval")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_autosave_interval)
        self.spinbox_autosave_interval = QtGui.QSpinBox(self.groupBox)
        self.spinbox_autosave_interval.setMinimum(1)
        self.spinbox_autosave_interval.setMaximum(1000)
        self.spinbox_autosave_interval.setSingleStep(10)
        self.spinbox_autosave_interval.setObjectName("spinbox_autosave_interval")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinbox_autosave_interval)
        self.button_browse_autosave = QtGui.QPushButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/browse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_browse_autosave.setIcon(icon)
        self.button_browse_autosave.setObjectName("button_browse_autosave")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.button_browse_autosave)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout.setContentsMargins(0, -1, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.checkbox_auto_update_check = QtGui.QCheckBox(self.groupBox_3)
        self.checkbox_auto_update_check.setObjectName("checkbox_auto_update_check")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkbox_auto_update_check)
        self.button_update_check = QtGui.QPushButton(self.groupBox_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_update_check.setIcon(icon1)
        self.button_update_check.setObjectName("button_update_check")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.button_update_check)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout.setContentsMargins(0, 9, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.checkbox_opensesamerun = QtGui.QCheckBox(self.groupBox_4)
        self.checkbox_opensesamerun.setObjectName("checkbox_opensesamerun")
        self.gridLayout.addWidget(self.checkbox_opensesamerun, 1, 0, 1, 2)
        self.checkbox_auto_opensesamerun_exec = QtGui.QCheckBox(self.groupBox_4)
        self.checkbox_auto_opensesamerun_exec.setObjectName("checkbox_auto_opensesamerun_exec")
        self.gridLayout.addWidget(self.checkbox_auto_opensesamerun_exec, 2, 0, 1, 2)
        self.label_opensesamerun_exec = QtGui.QLabel(self.groupBox_4)
        self.label_opensesamerun_exec.setObjectName("label_opensesamerun_exec")
        self.gridLayout.addWidget(self.label_opensesamerun_exec, 3, 0, 1, 1)
        self.edit_opensesamerun_exec = QtGui.QLineEdit(self.groupBox_4)
        self.edit_opensesamerun_exec.setObjectName("edit_opensesamerun_exec")
        self.gridLayout.addWidget(self.edit_opensesamerun_exec, 3, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.checkbox_opensesamerun, QtCore.SIGNAL("toggled(bool)"), self.checkbox_auto_opensesamerun_exec.setEnabled)
        QtCore.QObject.connect(self.checkbox_auto_opensesamerun_exec, QtCore.SIGNAL("toggled(bool)"), self.label_opensesamerun_exec.setEnabled)
        QtCore.QObject.connect(self.checkbox_auto_opensesamerun_exec, QtCore.SIGNAL("toggled(bool)"), self.label_opensesamerun_exec.setDisabled)
        QtCore.QObject.connect(self.checkbox_auto_opensesamerun_exec, QtCore.SIGNAL("toggled(bool)"), self.edit_opensesamerun_exec.setDisabled)
        QtCore.QObject.connect(self.checkbox_enable_autosave, QtCore.SIGNAL("toggled(bool)"), self.spinbox_autosave_interval.setEnabled)
        QtCore.QObject.connect(self.checkbox_enable_autosave, QtCore.SIGNAL("toggled(bool)"), self.label_autosave_interval.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Miscellaneous", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_immediately_rename.setText(QtGui.QApplication.translate("Form", "Offer to rename new items immediately", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_autoresponse.setText(QtGui.QApplication.translate("Form", "Enable auto-response", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_show_random_tips.setText(QtGui.QApplication.translate("Form", "Show random tips on start-up", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_toolbar_text.setText(QtGui.QApplication.translate("Form", "Show text in toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Backups", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_enable_autosave.setText(QtGui.QApplication.translate("Form", "Automatically create backups", None, QtGui.QApplication.UnicodeUTF8))
        self.label_autosave_interval.setText(QtGui.QApplication.translate("Form", "Auto-save interval:", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_autosave_interval.setSuffix(QtGui.QApplication.translate("Form", " minute(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_autosave_interval.setPrefix(QtGui.QApplication.translate("Form", "every ", None, QtGui.QApplication.UnicodeUTF8))
        self.button_browse_autosave.setText(QtGui.QApplication.translate("Form", "Open backup folder", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "Updates", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_auto_update_check.setText(QtGui.QApplication.translate("Form", "Check for updates on start-up", None, QtGui.QApplication.UnicodeUTF8))
        self.button_update_check.setText(QtGui.QApplication.translate("Form", "Check for updates now", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Form", "Run options", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">If you experience stability issues, most notably crashes when you run an experiment for the second time in a single session of OpenSesame, you can enable the \'Run experiments in a separate process\' option.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_opensesamerun.setText(QtGui.QApplication.translate("Form", "Run experiments in a separate process", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_auto_opensesamerun_exec.setText(QtGui.QApplication.translate("Form", "Auto-detect the run command", None, QtGui.QApplication.UnicodeUTF8))
        self.label_opensesamerun_exec.setText(QtGui.QApplication.translate("Form", "Custom run command:", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
