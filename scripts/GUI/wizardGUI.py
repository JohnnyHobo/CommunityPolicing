# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doxwizard.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName("Wizard")
        Wizard.setEnabled(True)
        Wizard.resize(637, 595)
        Wizard.setSizeGripEnabled(False)
        Wizard.setModal(False)
        Wizard.setWizardStyle(QtWidgets.QWizard.AeroStyle)
        Wizard.setOptions(QtWidgets.QWizard.ExtendedWatermarkPixmap|QtWidgets.QWizard.HaveCustomButton1|QtWidgets.QWizard.IndependentPages)
        self.wizardPage1Individual = QtWidgets.QWizardPage()
        self.wizardPage1Individual.setObjectName("wizardPage1Individual")
        self.formLayout = QtWidgets.QFormLayout(self.wizardPage1Individual)
        self.formLayout.setObjectName("formLayout")
        self.label_15 = QtWidgets.QLabel(self.wizardPage1Individual)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.indFName = QtWidgets.QLineEdit(self.wizardPage1Individual)
        self.indFName.setObjectName("indFName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.indFName)
        self.label_14 = QtWidgets.QLabel(self.wizardPage1Individual)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.indLName = QtWidgets.QLineEdit(self.wizardPage1Individual)
        self.indLName.setObjectName("indLName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.indLName)
        self.label_4 = QtWidgets.QLabel(self.wizardPage1Individual)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.indAlias = QtWidgets.QLineEdit(self.wizardPage1Individual)
        self.indAlias.setObjectName("indAlias")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.indAlias)
        self.label_19 = QtWidgets.QLabel(self.wizardPage1Individual)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.indAssociates = QtWidgets.QLineEdit(self.wizardPage1Individual)
        self.indAssociates.setObjectName("indAssociates")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.indAssociates)
        self.label_20 = QtWidgets.QLabel(self.wizardPage1Individual)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.indPhone = QtWidgets.QLineEdit(self.wizardPage1Individual)
        self.indPhone.setObjectName("indPhone")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.indPhone)
        self.label_17 = QtWidgets.QLabel(self.wizardPage1Individual)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.insState = QtWidgets.QLineEdit(self.wizardPage1Individual)
        self.insState.setObjectName("insState")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.insState)
        self.label_16 = QtWidgets.QLabel(self.wizardPage1Individual)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.indCity = QtWidgets.QLineEdit(self.wizardPage1Individual)
        self.indCity.setObjectName("indCity")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.indCity)
        self.label_18 = QtWidgets.QLabel(self.wizardPage1Individual)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.indZip = QtWidgets.QLineEdit(self.wizardPage1Individual)
        self.indZip.setObjectName("indZip")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.indZip)
        self.label_8 = QtWidgets.QLabel(self.wizardPage1Individual)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.indAddress = QtWidgets.QLineEdit(self.wizardPage1Individual)
        self.indAddress.setObjectName("indAddress")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.indAddress)
        self.label_2 = QtWidgets.QLabel(self.wizardPage1Individual)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.indOrgs = QtWidgets.QLineEdit(self.wizardPage1Individual)
        self.indOrgs.setObjectName("indOrgs")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.indOrgs)
        self.label_5 = QtWidgets.QLabel(self.wizardPage1Individual)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.indComboBoxEthnicity = QtWidgets.QComboBox(self.wizardPage1Individual)
        self.indComboBoxEthnicity.setObjectName("indComboBoxEthnicity")
        self.indComboBoxEthnicity.addItem("")
        self.indComboBoxEthnicity.addItem("")
        self.indComboBoxEthnicity.addItem("")
        self.indComboBoxEthnicity.addItem("")
        self.indComboBoxEthnicity.addItem("")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.indComboBoxEthnicity)
        self.label_6 = QtWidgets.QLabel(self.wizardPage1Individual)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.indDescription = QtWidgets.QLineEdit(self.wizardPage1Individual)
        self.indDescription.setObjectName("indDescription")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.indDescription)
        self.label_3 = QtWidgets.QLabel(self.wizardPage1Individual)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.indLinks = QtWidgets.QLineEdit(self.wizardPage1Individual)
        self.indLinks.setObjectName("indLinks")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.indLinks)
        self.label_21 = QtWidgets.QLabel(self.wizardPage1Individual)
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.indAddWebBtn = QtWidgets.QPushButton(self.wizardPage1Individual)
        self.indAddWebBtn.setObjectName("indAddWebBtn")
        self.horizontalLayout.addWidget(self.indAddWebBtn)
        self.indAddFileBtn = QtWidgets.QPushButton(self.wizardPage1Individual)
        self.indAddFileBtn.setObjectName("indAddFileBtn")
        self.horizontalLayout.addWidget(self.indAddFileBtn)
        self.formLayout.setLayout(13, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_7 = QtWidgets.QLabel(self.wizardPage1Individual)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.indComments = QtWidgets.QLineEdit(self.wizardPage1Individual)
        self.indComments.setObjectName("indComments")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.indComments)
        Wizard.addPage(self.wizardPage1Individual)
        self.wizardPage1Group = QtWidgets.QWizardPage()
        self.wizardPage1Group.setObjectName("wizardPage1Group")
        self.formLayout_2 = QtWidgets.QFormLayout(self.wizardPage1Group)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_32 = QtWidgets.QLabel(self.wizardPage1Group)
        self.label_32.setObjectName("label_32")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_32)
        self.groupName = QtWidgets.QLineEdit(self.wizardPage1Group)
        self.groupName.setObjectName("groupName")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.groupName)
        self.label_25 = QtWidgets.QLabel(self.wizardPage1Group)
        self.label_25.setObjectName("label_25")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.groupAffiliates = QtWidgets.QLineEdit(self.wizardPage1Group)
        self.groupAffiliates.setObjectName("groupAffiliates")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.groupAffiliates)
        self.label_27 = QtWidgets.QLabel(self.wizardPage1Group)
        self.label_27.setObjectName("label_27")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.groupMembers = QtWidgets.QLineEdit(self.wizardPage1Group)
        self.groupMembers.setObjectName("groupMembers")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.groupMembers)
        self.label_24 = QtWidgets.QLabel(self.wizardPage1Group)
        self.label_24.setObjectName("label_24")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.groupPhone = QtWidgets.QLineEdit(self.wizardPage1Group)
        self.groupPhone.setObjectName("groupPhone")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.groupPhone)
        self.label_26 = QtWidgets.QLabel(self.wizardPage1Group)
        self.label_26.setObjectName("label_26")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.groupState = QtWidgets.QLineEdit(self.wizardPage1Group)
        self.groupState.setObjectName("groupState")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.groupState)
        self.label_36 = QtWidgets.QLabel(self.wizardPage1Group)
        self.label_36.setObjectName("label_36")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_36)
        self.groupCity = QtWidgets.QLineEdit(self.wizardPage1Group)
        self.groupCity.setObjectName("groupCity")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.groupCity)
        self.label_34 = QtWidgets.QLabel(self.wizardPage1Group)
        self.label_34.setObjectName("label_34")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_34)
        self.groupZip = QtWidgets.QLineEdit(self.wizardPage1Group)
        self.groupZip.setObjectName("groupZip")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.groupZip)
        self.label_30 = QtWidgets.QLabel(self.wizardPage1Group)
        self.label_30.setObjectName("label_30")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_30)
        self.groupAddress = QtWidgets.QLineEdit(self.wizardPage1Group)
        self.groupAddress.setObjectName("groupAddress")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.groupAddress)
        self.label_35 = QtWidgets.QLabel(self.wizardPage1Group)
        self.label_35.setObjectName("label_35")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.groupDonors = QtWidgets.QLineEdit(self.wizardPage1Group)
        self.groupDonors.setObjectName("groupDonors")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.groupDonors)
        self.label_22 = QtWidgets.QLabel(self.wizardPage1Group)
        self.label_22.setObjectName("label_22")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.groupComboNonprofit = QtWidgets.QComboBox(self.wizardPage1Group)
        self.groupComboNonprofit.setObjectName("groupComboNonprofit")
        self.groupComboNonprofit.addItem("")
        self.groupComboNonprofit.addItem("")
        self.groupComboNonprofit.addItem("")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.groupComboNonprofit)
        self.label_37 = QtWidgets.QLabel(self.wizardPage1Group)
        self.label_37.setObjectName("label_37")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_37)
        self.groupDescription = QtWidgets.QLineEdit(self.wizardPage1Group)
        self.groupDescription.setObjectName("groupDescription")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.groupDescription)
        self.label_29 = QtWidgets.QLabel(self.wizardPage1Group)
        self.label_29.setObjectName("label_29")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.links_2 = QtWidgets.QLineEdit(self.wizardPage1Group)
        self.links_2.setObjectName("links_2")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.links_2)
        self.label_28 = QtWidgets.QLabel(self.wizardPage1Group)
        self.label_28.setObjectName("label_28")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupAddFile = QtWidgets.QPushButton(self.wizardPage1Group)
        self.groupAddFile.setObjectName("groupAddFile")
        self.horizontalLayout_2.addWidget(self.groupAddFile)
        self.groupAddFromWeb = QtWidgets.QPushButton(self.wizardPage1Group)
        self.groupAddFromWeb.setObjectName("groupAddFromWeb")
        self.horizontalLayout_2.addWidget(self.groupAddFromWeb)
        self.formLayout_2.setLayout(12, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_31 = QtWidgets.QLabel(self.wizardPage1Group)
        self.label_31.setObjectName("label_31")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.groupComments = QtWidgets.QLineEdit(self.wizardPage1Group)
        self.groupComments.setObjectName("groupComments")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.groupComments)
        self.groupDescription.raise_()
        self.label_22.raise_()
        self.groupState.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_28.raise_()
        self.label_29.raise_()
        self.label_30.raise_()
        self.groupAffiliates.raise_()
        self.links_2.raise_()
        self.label_32.raise_()
        self.groupZip.raise_()
        self.groupCity.raise_()
        self.groupAddress.raise_()
        self.label_34.raise_()
        self.label_35.raise_()
        self.groupName.raise_()
        self.groupComboNonprofit.raise_()
        self.label_36.raise_()
        self.label_37.raise_()
        self.groupDonors.raise_()
        self.groupPhone.raise_()
        self.label_31.raise_()
        self.groupComments.raise_()
        self.label_27.raise_()
        self.groupMembers.raise_()
        Wizard.addPage(self.wizardPage1Group)
        self.wizardPage1Event = QtWidgets.QWizardPage()
        self.wizardPage1Event.setObjectName("wizardPage1Event")
        self.formLayout_3 = QtWidgets.QFormLayout(self.wizardPage1Event)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_33 = QtWidgets.QLabel(self.wizardPage1Event)
        self.label_33.setObjectName("label_33")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_33)
        self.eventTitle = QtWidgets.QLineEdit(self.wizardPage1Event)
        self.eventTitle.setObjectName("eventTitle")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.eventTitle)
        self.label_48 = QtWidgets.QLabel(self.wizardPage1Event)
        self.label_48.setObjectName("label_48")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_48)
        self.eventFName = QtWidgets.QLineEdit(self.wizardPage1Event)
        self.eventFName.setObjectName("eventFName")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.eventFName)
        self.label_43 = QtWidgets.QLabel(self.wizardPage1Event)
        self.label_43.setObjectName("label_43")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_43)
        self.eventLName = QtWidgets.QLineEdit(self.wizardPage1Event)
        self.eventLName.setObjectName("eventLName")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.eventLName)
        self.label_49 = QtWidgets.QLabel(self.wizardPage1Event)
        self.label_49.setObjectName("label_49")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_49)
        self.eventAlias = QtWidgets.QLineEdit(self.wizardPage1Event)
        self.eventAlias.setObjectName("eventAlias")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.eventAlias)
        self.label_41 = QtWidgets.QLabel(self.wizardPage1Event)
        self.label_41.setObjectName("label_41")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_41)
        self.eventAssociates = QtWidgets.QLineEdit(self.wizardPage1Event)
        self.eventAssociates.setObjectName("eventAssociates")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.eventAssociates)
        self.label_42 = QtWidgets.QLabel(self.wizardPage1Event)
        self.label_42.setObjectName("label_42")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_42)
        self.eventState = QtWidgets.QLineEdit(self.wizardPage1Event)
        self.eventState.setObjectName("eventState")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.eventState)
        self.label_52 = QtWidgets.QLabel(self.wizardPage1Event)
        self.label_52.setObjectName("label_52")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_52)
        self.eventCity = QtWidgets.QLineEdit(self.wizardPage1Event)
        self.eventCity.setObjectName("eventCity")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.eventCity)
        self.label_50 = QtWidgets.QLabel(self.wizardPage1Event)
        self.label_50.setObjectName("label_50")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_50)
        self.eventZip = QtWidgets.QLineEdit(self.wizardPage1Event)
        self.eventZip.setObjectName("eventZip")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.eventZip)
        self.label_51 = QtWidgets.QLabel(self.wizardPage1Event)
        self.label_51.setObjectName("label_51")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_51)
        self.eventOrgs = QtWidgets.QLineEdit(self.wizardPage1Event)
        self.eventOrgs.setObjectName("eventOrgs")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.eventOrgs)
        self.label_53 = QtWidgets.QLabel(self.wizardPage1Event)
        self.label_53.setObjectName("label_53")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_53)
        self.eventDescription = QtWidgets.QLineEdit(self.wizardPage1Event)
        self.eventDescription.setObjectName("eventDescription")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.eventDescription)
        self.label_45 = QtWidgets.QLabel(self.wizardPage1Event)
        self.label_45.setObjectName("label_45")
        self.formLayout_3.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_45)
        self.eventLinks = QtWidgets.QLineEdit(self.wizardPage1Event)
        self.eventLinks.setObjectName("eventLinks")
        self.formLayout_3.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.eventLinks)
        self.label_44 = QtWidgets.QLabel(self.wizardPage1Event)
        self.label_44.setObjectName("label_44")
        self.formLayout_3.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_44)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.eventAddFileBtn = QtWidgets.QPushButton(self.wizardPage1Event)
        self.eventAddFileBtn.setObjectName("eventAddFileBtn")
        self.horizontalLayout_5.addWidget(self.eventAddFileBtn)
        self.eventAddWebBtn = QtWidgets.QPushButton(self.wizardPage1Event)
        self.eventAddWebBtn.setObjectName("eventAddWebBtn")
        self.horizontalLayout_5.addWidget(self.eventAddWebBtn)
        self.formLayout_3.setLayout(11, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.label_47 = QtWidgets.QLabel(self.wizardPage1Event)
        self.label_47.setObjectName("label_47")
        self.formLayout_3.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_47)
        self.eventComments = QtWidgets.QLineEdit(self.wizardPage1Event)
        self.eventComments.setObjectName("eventComments")
        self.formLayout_3.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.eventComments)
        Wizard.addPage(self.wizardPage1Event)
        self.wizardPageCrime = QtWidgets.QWizardPage()
        self.wizardPageCrime.setObjectName("wizardPageCrime")
        self.formLayout_4 = QtWidgets.QFormLayout(self.wizardPageCrime)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_9 = QtWidgets.QLabel(self.wizardPageCrime)
        self.label_9.setObjectName("label_9")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.crimePerp = QtWidgets.QLineEdit(self.wizardPageCrime)
        self.crimePerp.setObjectName("crimePerp")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.crimePerp)
        self.label = QtWidgets.QLabel(self.wizardPageCrime)
        self.label.setObjectName("label")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.crimeCrime = QtWidgets.QLineEdit(self.wizardPageCrime)
        self.crimeCrime.setObjectName("crimeCrime")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.crimeCrime)
        self.label_10 = QtWidgets.QLabel(self.wizardPageCrime)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.eventLinks_2 = QtWidgets.QLineEdit(self.wizardPageCrime)
        self.eventLinks_2.setObjectName("eventLinks_2")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.eventLinks_2)
        self.checkBox = QtWidgets.QCheckBox(self.wizardPageCrime)
        self.checkBox.setObjectName("checkBox")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        self.label_11 = QtWidgets.QLabel(self.wizardPageCrime)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.wizardPageCrime)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dateTimeEdit)
        self.label_61 = QtWidgets.QLabel(self.wizardPageCrime)
        self.label_61.setObjectName("label_61")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_61)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.crimeAddWebBtn = QtWidgets.QPushButton(self.wizardPageCrime)
        self.crimeAddWebBtn.setObjectName("crimeAddWebBtn")
        self.horizontalLayout_7.addWidget(self.crimeAddWebBtn)
        self.crimeAddFileBtn = QtWidgets.QPushButton(self.wizardPageCrime)
        self.crimeAddFileBtn.setObjectName("crimeAddFileBtn")
        self.horizontalLayout_7.addWidget(self.crimeAddFileBtn)
        self.formLayout_4.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.label_59 = QtWidgets.QLabel(self.wizardPageCrime)
        self.label_59.setObjectName("label_59")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_59)
        self.eventCrime_2 = QtWidgets.QLineEdit(self.wizardPageCrime)
        self.eventCrime_2.setObjectName("eventCrime_2")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.eventCrime_2)
        self.label_66 = QtWidgets.QLabel(self.wizardPageCrime)
        self.label_66.setObjectName("label_66")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_66)
        self.crimeComments = QtWidgets.QLineEdit(self.wizardPageCrime)
        self.crimeComments.setObjectName("crimeComments")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.crimeComments)
        Wizard.addPage(self.wizardPageCrime)
        self.wizardPage_3 = QtWidgets.QWizardPage()
        self.wizardPage_3.setObjectName("wizardPage_3")
        self.runAllVideo_2 = QtWidgets.QPushButton(self.wizardPage_3)
        self.runAllVideo_2.setGeometry(QtCore.QRect(320, 476, 300, 27))
        self.runAllVideo_2.setObjectName("runAllVideo_2")
        self.runFacialRecog_2 = QtWidgets.QPushButton(self.wizardPage_3)
        self.runFacialRecog_2.setGeometry(QtCore.QRect(320, 443, 300, 27))
        self.runFacialRecog_2.setObjectName("runFacialRecog_2")
        self.findOnline_2 = QtWidgets.QPushButton(self.wizardPage_3)
        self.findOnline_2.setGeometry(QtCore.QRect(320, 410, 300, 27))
        self.findOnline_2.setObjectName("findOnline_2")
        self.listView = QtWidgets.QListView(self.wizardPage_3)
        self.listView.setGeometry(QtCore.QRect(20, 10, 611, 381))
        self.listView.setObjectName("listView")
        Wizard.addPage(self.wizardPage_3)
        self.wizardPage_2 = QtWidgets.QWizardPage()
        self.wizardPage_2.setObjectName("wizardPage_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.wizardPage_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableViewMatch = QtWidgets.QTableView(self.wizardPage_2)
        self.tableViewMatch.setObjectName("tableViewMatch")
        self.gridLayout_2.addWidget(self.tableViewMatch, 3, 4, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.wizardPage_2)
        self.label_40.setObjectName("label_40")
        self.gridLayout_2.addWidget(self.label_40, 2, 0, 1, 1)
        self.imageViewOrig = QtWidgets.QGraphicsView(self.wizardPage_2)
        self.imageViewOrig.setObjectName("imageViewOrig")
        self.gridLayout_2.addWidget(self.imageViewOrig, 1, 0, 1, 2)
        self.imageViewMatch = QtWidgets.QGraphicsView(self.wizardPage_2)
        self.imageViewMatch.setObjectName("imageViewMatch")
        self.gridLayout_2.addWidget(self.imageViewMatch, 3, 0, 1, 2)
        self.label_55 = QtWidgets.QLabel(self.wizardPage_2)
        self.label_55.setObjectName("label_55")
        self.gridLayout_2.addWidget(self.label_55, 0, 1, 1, 1)
        self.tableViewOrig = QtWidgets.QTableView(self.wizardPage_2)
        self.tableViewOrig.setObjectName("tableViewOrig")
        self.gridLayout_2.addWidget(self.tableViewOrig, 1, 4, 1, 1)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.wizardPage_2)
        self.lcdNumber_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdNumber_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber_3.setDigitCount(9)
        self.lcdNumber_3.setProperty("intValue", 999999999)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.gridLayout_2.addWidget(self.lcdNumber_3, 0, 4, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.createNewBtn = QtWidgets.QPushButton(self.wizardPage_2)
        self.createNewBtn.setObjectName("createNewBtn")
        self.horizontalLayout_6.addWidget(self.createNewBtn)
        self.mergeBtn = QtWidgets.QPushButton(self.wizardPage_2)
        self.mergeBtn.setObjectName("mergeBtn")
        self.horizontalLayout_6.addWidget(self.mergeBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 2, 4, 1, 1)
        Wizard.addPage(self.wizardPage_2)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        _translate = QtCore.QCoreApplication.translate
        Wizard.setWindowTitle(_translate("Wizard", "Wizard"))
        self.label_15.setText(_translate("Wizard", "First Name:"))
        self.indFName.setPlaceholderText(_translate("Wizard", "Suspect First Name (If Known)"))
        self.label_14.setText(_translate("Wizard", "Last Name:"))
        self.indLName.setPlaceholderText(_translate("Wizard", "Suspect Last Name (If Known)"))
        self.label_4.setText(_translate("Wizard", "Alias:"))
        self.indAlias.setPlaceholderText(_translate("Wizard", "Suspect Alias"))
        self.label_19.setText(_translate("Wizard", "Associates:"))
        self.indAssociates.setPlaceholderText(_translate("Wizard", "John Doe, Jane Doe, etc."))
        self.label_20.setText(_translate("Wizard", "Phone:"))
        self.label_17.setText(_translate("Wizard", "State:"))
        self.label_16.setText(_translate("Wizard", "City:"))
        self.label_18.setText(_translate("Wizard", "Zip:"))
        self.label_8.setText(_translate("Wizard", "Address:"))
        self.label_2.setText(_translate("Wizard", "Organizations:"))
        self.label_5.setText(_translate("Wizard", "Ethnicity:"))
        self.indComboBoxEthnicity.setCurrentText(_translate("Wizard", "White (cuck)"))
        self.indComboBoxEthnicity.setItemText(0, _translate("Wizard", "White (cuck)"))
        self.indComboBoxEthnicity.setItemText(1, _translate("Wizard", "Asian (fish eye, gook)"))
        self.indComboBoxEthnicity.setItemText(2, _translate("Wizard", "Mexican (gotta go back)"))
        self.indComboBoxEthnicity.setItemText(3, _translate("Wizard", "Black (nigger)"))
        self.indComboBoxEthnicity.setItemText(4, _translate("Wizard", "Jewish (kike)"))
        self.label_6.setText(_translate("Wizard", "Description:"))
        self.indDescription.setPlaceholderText(_translate("Wizard", "Short description of perp"))
        self.label_3.setText(_translate("Wizard", "Links:"))
        self.indLinks.setPlaceholderText(_translate("Wizard", "Comma Separated (.e.g. facebook.com, archive.is, google.com)"))
        self.label_21.setText(_translate("Wizard", "Video/Images"))
        self.indAddWebBtn.setText(_translate("Wizard", "Add From File"))
        self.indAddFileBtn.setText(_translate("Wizard", "Add From Web"))
        self.label_7.setText(_translate("Wizard", "Comments:"))
        self.indComments.setPlaceholderText(_translate("Wizard", "Any additional comments"))
        self.label_32.setText(_translate("Wizard", "Group Name:"))
        self.groupName.setPlaceholderText(_translate("Wizard", "Suspect First Name (If Known)"))
        self.label_25.setText(_translate("Wizard", "Affiliates"))
        self.groupAffiliates.setPlaceholderText(_translate("Wizard", "John Doe, Jane Doe, etc."))
        self.label_27.setText(_translate("Wizard", "Members"))
        self.label_24.setText(_translate("Wizard", "Phone:"))
        self.label_26.setText(_translate("Wizard", "State:"))
        self.label_36.setText(_translate("Wizard", "City:"))
        self.label_34.setText(_translate("Wizard", "Zip:"))
        self.label_30.setText(_translate("Wizard", "Address:"))
        self.label_35.setText(_translate("Wizard", "Donors"))
        self.label_22.setText(_translate("Wizard", "NonProfit"))
        self.groupComboNonprofit.setCurrentText(_translate("Wizard", "Yes"))
        self.groupComboNonprofit.setItemText(0, _translate("Wizard", "Yes"))
        self.groupComboNonprofit.setItemText(1, _translate("Wizard", "Yes: 501.3c"))
        self.groupComboNonprofit.setItemText(2, _translate("Wizard", "No"))
        self.label_37.setText(_translate("Wizard", "Description:"))
        self.groupDescription.setPlaceholderText(_translate("Wizard", "Short description of perp"))
        self.label_29.setText(_translate("Wizard", "Website"))
        self.links_2.setPlaceholderText(_translate("Wizard", "Comma Separated (.e.g. facebook.com, archive.is, google.com)"))
        self.label_28.setText(_translate("Wizard", "Video/Images"))
        self.groupAddFile.setText(_translate("Wizard", "Add From File"))
        self.groupAddFromWeb.setText(_translate("Wizard", "Add From Web"))
        self.label_31.setText(_translate("Wizard", "Comments:"))
        self.groupComments.setPlaceholderText(_translate("Wizard", "Any additional comments"))
        self.label_33.setText(_translate("Wizard", "Event:"))
        self.label_48.setText(_translate("Wizard", "First Name:"))
        self.eventFName.setPlaceholderText(_translate("Wizard", "Suspect First Name (If Known)"))
        self.label_43.setText(_translate("Wizard", "Last Name:"))
        self.eventLName.setPlaceholderText(_translate("Wizard", "Suspect Last Name (If Known)"))
        self.label_49.setText(_translate("Wizard", "Alias:"))
        self.eventAlias.setPlaceholderText(_translate("Wizard", "Suspect Alias"))
        self.label_41.setText(_translate("Wizard", "Associates:"))
        self.eventAssociates.setPlaceholderText(_translate("Wizard", "John Doe, Jane Doe, etc."))
        self.label_42.setText(_translate("Wizard", "State:"))
        self.label_52.setText(_translate("Wizard", "City:"))
        self.label_50.setText(_translate("Wizard", "Zip:"))
        self.label_51.setText(_translate("Wizard", "Organizations:"))
        self.label_53.setText(_translate("Wizard", "Description:"))
        self.eventDescription.setPlaceholderText(_translate("Wizard", "Short description of perp"))
        self.label_45.setText(_translate("Wizard", "Links:"))
        self.eventLinks.setPlaceholderText(_translate("Wizard", "Comma Separated (.e.g. facebook.com, archive.is, google.com)"))
        self.label_44.setText(_translate("Wizard", "Video/Images"))
        self.eventAddFileBtn.setText(_translate("Wizard", "Add From File"))
        self.eventAddWebBtn.setText(_translate("Wizard", "Add From Web"))
        self.label_47.setText(_translate("Wizard", "Comments:"))
        self.eventComments.setPlaceholderText(_translate("Wizard", "Any additional comments"))
        self.label_9.setText(_translate("Wizard", "Perpetrator:"))
        self.label.setText(_translate("Wizard", "Crime:"))
        self.crimeCrime.setPlaceholderText(_translate("Wizard", "Suspect First Name (If Known)"))
        self.label_10.setText(_translate("Wizard", "Links:"))
        self.eventLinks_2.setPlaceholderText(_translate("Wizard", "Comma Separated (.e.g. facebook.com, archive.is, google.com)"))
        self.checkBox.setText(_translate("Wizard", "Auto Archive?"))
        self.label_11.setText(_translate("Wizard", "Date:"))
        self.label_61.setText(_translate("Wizard", "Video/Images"))
        self.crimeAddWebBtn.setText(_translate("Wizard", "Add From Web"))
        self.crimeAddFileBtn.setText(_translate("Wizard", "Add From File"))
        self.label_59.setText(_translate("Wizard", "Description:"))
        self.eventCrime_2.setPlaceholderText(_translate("Wizard", "Description Of Crime"))
        self.label_66.setText(_translate("Wizard", "Comments:"))
        self.crimeComments.setPlaceholderText(_translate("Wizard", "Any additional comments"))
        self.runAllVideo_2.setAccessibleName(_translate("Wizard", "<html><head/><body><p>Perform All Tests (recommended).</p></body></html>"))
        self.runAllVideo_2.setText(_translate("Wizard", "Run All Tests"))
        self.runFacialRecog_2.setAccessibleName(_translate("Wizard", "<html><head/><body><p>Perform Facial Recognition On Images And Videos In Your Database.</p></body></html>"))
        self.runFacialRecog_2.setText(_translate("Wizard", "Run Facial Recognition"))
        self.findOnline_2.setAccessibleName(_translate("Wizard", "<html><head/><body><p>Search Your Databases And The Web For Image Matches.</p></body></html>"))
        self.findOnline_2.setText(_translate("Wizard", "Reverse Image Search"))
        self.label_40.setText(_translate("Wizard", "Matches"))
        self.label_55.setText(_translate("Wizard", "Remaining"))
        self.createNewBtn.setText(_translate("Wizard", "Create New"))
        self.mergeBtn.setText(_translate("Wizard", "Append Existing"))

