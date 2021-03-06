# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exportView.ui'
#
# Created: Fri Apr 17 21:12:14 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
root=os.getenv('EXPRESSO_ROOT')
import h5py
import DataHandler
import shutil

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    signalRefreshTrigger=QtCore.pyqtSignal(object)
    def __init__(self, parent=None,dataName=None):
        super(Ui_Form, self).__init__(parent)
        self.dataName=dataName
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(421, 183)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 161, 31))
        self.label.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 221, 31))
        self.label_2.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(253, 140, 71, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 140, 71, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 331, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
	self.lineEdit.setReadOnly(True)
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(380, 70, 23, 25))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(277, 20, 121, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Export Data", None))
        self.label_2.setText(_translate("Form", "Length", None))
        self.pushButton_4.setText(_translate("Form", "Cancel", None))
        self.pushButton_3.setText(_translate("Form", "Ok", None))
        self.toolButton.setText(_translate("Form", "...", None))
	self.fillData()
	self.toolButton.clicked.connect(self.updatePathSlot)
	self.pushButton_3.clicked.connect(self.onOkClickedSlot)
	self.pushButton_4.clicked.connect(self.closedSlot)


    def fillData(self):
	self.comboBox.addItems(['MAT','HDF5'])
	with h5py.File(root+'/data/'+self.dataName+'.hdf5') as f:
	    shape=f['data'].shape
	    self.label_2.setText('Length :'+str(shape[0])+' x '+str(shape[1])+' x '+str(shape[2])+' x '+str(shape[3]))


    def updatePathSlot(self):
	if(self.comboBox.currentText().__str__()=='MAT'):
	    extension='.mat'
	elif(self.comboBox.currentText().__str__()=='HDF5'):
	    extension='.hdf5'
	filename = QtGui.QFileDialog.getSaveFileName(self, 'Dialog Title',root, selectedFilter='*'+extension)
	if(extension not in filename):filename=filename+extension
	self.lineEdit.setText(filename)

    def onOkClickedSlot(self):
	if(self.comboBox.currentText().__str__()=='MAT'):
	    print 'Calling Mat Saver'
	    DataHandler.exportAsMat(self.lineEdit.text().__str__(),self.dataName)
	elif(self.comboBox.currentText().__str__()=='HDF5'):
	    print 'Calling HDF5 Saver'
	    shutil.copyfile(root+'/data/'+self.dataName+'.hdf5',self.lineEdit.text().__str__())
	self.signalRefreshTrigger.emit('\''+self.dataName+'\' has been exported with '+self.comboBox.currentText().__str__()+' format to location \''+self.lineEdit.text().__str__()+'\'')


	self.closedSlot()
 

    def closedSlot(self):
	self.close()
	
	
	

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

