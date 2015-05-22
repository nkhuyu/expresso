# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wizard.ui'
#
# Created: Fri May  1 18:07:22 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import wizardProto_pb2
root=os.getenv('EXPRESSO_ROOT')
from google.protobuf import text_format
import wizardViewExtended
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
    def __init__(self,parent=None,flowName=''):
        super(Ui_Form,self).__init__(parent)
	self.flowName=flowName
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(291, 351)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 291, 351))
        self.widget.setStyleSheet(_fromUtf8("background-color:rgba(0, 0, 0, 0)"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.textEdit = QtGui.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(20, 80, 251, 231))
        self.textEdit.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255,100);\n"
"font: 12pt \"Ubuntu Condensed\";"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButtonBack = QtGui.QPushButton(self.widget)
        self.pushButtonBack.setGeometry(QtCore.QRect(120, 320, 71, 27))
        self.pushButtonBack.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255,100)"))
        self.pushButtonBack.setObjectName(_fromUtf8("pushButtonBack"))
        self.pushButtonNext = QtGui.QPushButton(self.widget)
        self.pushButtonNext.setGeometry(QtCore.QRect(200, 320, 71, 27))
        self.pushButtonNext.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255,100)"))
        self.pushButtonNext.setObjectName(_fromUtf8("pushButtonNext"))
        self.heading1Label = QtGui.QLabel(self.widget)
        self.heading1Label.setGeometry(QtCore.QRect(20, 0, 231, 41))
        self.heading1Label.setStyleSheet(_fromUtf8("background-color:rgb(0,0,0,0);\n"
"font: 18pt \"Ubuntu Condensed\";"))
        self.heading1Label.setObjectName(_fromUtf8("heading1Label"))
        self.pushButtonSnapshot = QtGui.QPushButton(self.widget)
        self.pushButtonSnapshot.setGeometry(QtCore.QRect(20, 320, 91, 27))
        self.pushButtonSnapshot.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255,100)"))
        self.pushButtonSnapshot.setObjectName(_fromUtf8("pushButtonSnapshot"))
	self.pushButtonSnapshot.hide()
        self.heading2ComboBox = QtGui.QComboBox(self.widget)
        self.heading2ComboBox.setGeometry(QtCore.QRect(20, 40, 251, 27))
        self.heading2ComboBox.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255,100);selection-color:rgb(0,0,0);selection-background-color:rgba(255,255,255,100);"))
        self.heading2ComboBox.setObjectName(_fromUtf8("heading2ComboBox"))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
	self.textParamHandler=wizardProto_pb2.Param()
	text_format.Merge(open(root+'/src/wizard/''wizardText.prototxt').read(),self.textParamHandler)
	self.pageNumber=0
	self.pushButtonNext.clicked.connect(self.nextPageSlot)
	self.pushButtonBack.clicked.connect(self.previousPageSlot)
	self.pushButtonBack.hide()
	self.totalPages=0
	#self.flowName='Import View'#Comment it Later
	self.textFlowParamHandler=wizardProto_pb2.FlowParam()
	#SnapShotWidget Start
	self.snapshotWidget=wizardViewExtended.Ui_Form(flowName=self.flowName)
        #self.snapshot.setStyleSheet("background-color:rgb(255,255,255)")
        self.snapshotWidget.setGeometry(QtCore.QRect(100,100,891,551))
	self.pushButtonSnapshot.clicked.connect(self.snapshotWidget.show)
	#SnapShotWidget Ends
	#Finding the data corrosponding to heading1==self.flowName(provided by user)
	for idx,elem in enumerate(self.textParamHandler.flow):
	    if(elem.heading1==self.flowName):
		self.textFlowParamHandler.CopyFrom(self.textParamHandler.flow[idx])
		self.heading2ComboBox.addItems([elem.heading2 for elem in self.textFlowParamHandler.subflow])
		self.heading2ComboBox.currentIndexChanged.connect(self.onHeading2Changed)
		self.onHeading2Changed()
		#SnapshotPreview
		
    
    def onHeading2Changed(self):
	self.heading2=self.heading2ComboBox.currentText().__str__()
	self.pageNumber=0;
	self.textSubFlowParamHandler=wizardProto_pb2.SubFlowParam()
	#Finding text,heading3 pairs corrosponding to heading2
	for idx,elem in enumerate(self.textFlowParamHandler.subflow):
	    if(elem.heading2==self.heading2):
		self.textSubFlowParamHandler.CopyFrom(self.textFlowParamHandler.subflow[idx])
		self.createFlows()


    def createFlows(self):
	self.totalPages=len(self.textSubFlowParamHandler.textiter)
	if(self.totalPages==0):
	    self.textEdit.clear();
	    self.pushButtonBack.hide()
	    self.pushButtonNext.hide()
	if(self.totalPages==1):
	    self.pushButtonBack.hide()
	    self.pushButtonNext.hide()
	    self.pageNumber=0;
	    self.setText()
	else:
	    self.pushButtonNext.show()
	    self.pushButtonBack.hide()
	    self.pageNumber=0;
	    self.setText()

    def nextPageSlot(self):
	if(self.totalPages==0):return
	if(self.pageNumber+1==self.totalPages):return
	self.pageNumber=self.pageNumber+1;
	#Show Hide Stuff
	if(self.pageNumber+1==self.totalPages):
	    self.pushButtonNext.hide()
	else:
	    self.pushButtonNext.show()
	if(self.pageNumber==0):
	    self.pushButtonBack.hide()
	else:
	    self.pushButtonBack.show()
	#Set Text
	self.setText()
	pass

    def previousPageSlot(self):
	if(self.totalPages==0):return
	if(self.pageNumber==0):return
	self.pageNumber=self.pageNumber-1;
	#Show Hide Stuff
	if(self.pageNumber+1==self.totalPages):
	    self.pushButtonNext.hide()
	else:
	    self.pushButtonNext.show()

	if(self.pageNumber==0):
	    self.pushButtonBack.hide()
	else:
	    self.pushButtonBack.show()
	#Set Text
	self.setText()
	pass

    def setText(self):
	heading=self.textSubFlowParamHandler.textiter[self.pageNumber].heading3
	text=self.textSubFlowParamHandler.textiter[self.pageNumber].text
	if heading=="":
	    self.textEdit.setText(text)
	else:
	    self.textEdit.setText('<h3>'+heading+'</h3>\n'+text)






    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButtonBack.setText(_translate("Form", "Back", None))
        self.pushButtonNext.setText(_translate("Form", "Next", None))
        self.heading1Label.setText(_translate("Form", self.flowName, None))
        self.pushButtonSnapshot.setText(_translate("Form", "Snapshots", None))


   

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

