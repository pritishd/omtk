# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rlessard/dev/omtk/scripts/omtk/ui.ui'
#
# Created: Wed Sep 14 14:45:30 2016
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_OpenRiggingToolkit(object):
    def setupUi(self, OpenRiggingToolkit):
        OpenRiggingToolkit.setObjectName("OpenRiggingToolkit")
        OpenRiggingToolkit.resize(936, 818)
        self.centralwidget = QtGui.QWidget(OpenRiggingToolkit)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_modules = QtGui.QLabel(self.layoutWidget)
        self.label_modules.setObjectName("label_modules")
        self.verticalLayout.addWidget(self.label_modules)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_search_modules = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_search_modules.setObjectName("lineEdit_search_modules")
        self.horizontalLayout.addWidget(self.lineEdit_search_modules)
        self.btn_update_modules = QtGui.QPushButton(self.layoutWidget)
        self.btn_update_modules.setObjectName("btn_update_modules")
        self.horizontalLayout.addWidget(self.btn_update_modules)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeWidget = QtGui.QTreeWidget(self.layoutWidget)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.header().setVisible(False)
        self.verticalLayout.addWidget(self.treeWidget)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_jnts = QtGui.QLabel(self.layoutWidget1)
        self.label_jnts.setObjectName("label_jnts")
        self.verticalLayout_2.addWidget(self.label_jnts)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_search_jnt = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_search_jnt.setObjectName("lineEdit_search_jnt")
        self.horizontalLayout_2.addWidget(self.lineEdit_search_jnt)
        self.btn_update_influences = QtGui.QPushButton(self.layoutWidget1)
        self.btn_update_influences.setObjectName("btn_update_influences")
        self.horizontalLayout_2.addWidget(self.btn_update_influences)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.checkBox_hideAssigned = QtGui.QCheckBox(self.layoutWidget1)
        self.checkBox_hideAssigned.setObjectName("checkBox_hideAssigned")
        self.verticalLayout_2.addWidget(self.checkBox_hideAssigned)
        self.treeWidget_jnts = QtGui.QTreeWidget(self.layoutWidget1)
        self.treeWidget_jnts.setSelectionMode(QtGui.QAbstractItemView.ContiguousSelection)
        self.treeWidget_jnts.setRootIsDecorated(True)
        self.treeWidget_jnts.setObjectName("treeWidget_jnts")
        self.treeWidget_jnts.headerItem().setText(0, "Joint Hierarchy")
        self.treeWidget_jnts.header().setVisible(False)
        self.verticalLayout_2.addWidget(self.treeWidget_jnts)
        self.layoutWidget2 = QtGui.QWidget(self.splitter)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtGui.QLabel(self.layoutWidget2)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_search_meshes = QtGui.QLineEdit(self.layoutWidget2)
        self.lineEdit_search_meshes.setObjectName("lineEdit_search_meshes")
        self.horizontalLayout_3.addWidget(self.lineEdit_search_meshes)
        self.btn_update_meshes = QtGui.QPushButton(self.layoutWidget2)
        self.btn_update_meshes.setObjectName("btn_update_meshes")
        self.horizontalLayout_3.addWidget(self.btn_update_meshes)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.treeWidget_meshes = QtGui.QTreeWidget(self.layoutWidget2)
        self.treeWidget_meshes.setSelectionMode(QtGui.QAbstractItemView.ContiguousSelection)
        self.treeWidget_meshes.setObjectName("treeWidget_meshes")
        self.treeWidget_meshes.headerItem().setText(0, "1")
        self.verticalLayout_3.addWidget(self.treeWidget_meshes)
        self.pushButton_selectGrpMeshes = QtGui.QPushButton(self.layoutWidget2)
        self.pushButton_selectGrpMeshes.setObjectName("pushButton_selectGrpMeshes")
        self.verticalLayout_3.addWidget(self.pushButton_selectGrpMeshes)
        self.verticalLayout_5.addWidget(self.splitter)
        OpenRiggingToolkit.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(OpenRiggingToolkit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuRig = QtGui.QMenu(self.menubar)
        self.menuRig.setObjectName("menuRig")
        self.menuJoint = QtGui.QMenu(self.menubar)
        self.menuJoint.setObjectName("menuJoint")
        self.menuInfluences = QtGui.QMenu(self.menubar)
        self.menuInfluences.setObjectName("menuInfluences")
        OpenRiggingToolkit.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(OpenRiggingToolkit)
        self.statusbar.setObjectName("statusbar")
        OpenRiggingToolkit.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(OpenRiggingToolkit)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_4 = QtGui.QLabel(self.dockWidgetContents)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_log_search = QtGui.QLineEdit(self.dockWidgetContents)
        self.lineEdit_log_search.setObjectName("lineEdit_log_search")
        self.horizontalLayout_4.addWidget(self.lineEdit_log_search)
        self.label_3 = QtGui.QLabel(self.dockWidgetContents)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.comboBox_log_level = QtGui.QComboBox(self.dockWidgetContents)
        self.comboBox_log_level.setObjectName("comboBox_log_level")
        self.comboBox_log_level.addItem("")
        self.comboBox_log_level.addItem("")
        self.comboBox_log_level.addItem("")
        self.comboBox_log_level.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_log_level)
        self.pushButton_logs_save = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_logs_save.setObjectName("pushButton_logs_save")
        self.horizontalLayout_4.addWidget(self.pushButton_logs_save)
        self.pushButton_logs_clear = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_logs_clear.setObjectName("pushButton_logs_clear")
        self.horizontalLayout_4.addWidget(self.pushButton_logs_clear)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.tableView_logs = QtGui.QTableView(self.dockWidgetContents)
        self.tableView_logs.setObjectName("tableView_logs")
        self.verticalLayout_4.addWidget(self.tableView_logs)
        self.dockWidget.setWidget(self.dockWidgetContents)
        OpenRiggingToolkit.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget)
        self.actionUpdate = QtGui.QAction(OpenRiggingToolkit)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionImport = QtGui.QAction(OpenRiggingToolkit)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtGui.QAction(OpenRiggingToolkit)
        self.actionExport.setObjectName("actionExport")
        self.actionBuild = QtGui.QAction(OpenRiggingToolkit)
        self.actionBuild.setObjectName("actionBuild")
        self.actionUnbuild = QtGui.QAction(OpenRiggingToolkit)
        self.actionUnbuild.setObjectName("actionUnbuild")
        self.actionRebuild = QtGui.QAction(OpenRiggingToolkit)
        self.actionRebuild.setObjectName("actionRebuild")
        self.actionCreateModule = QtGui.QAction(OpenRiggingToolkit)
        self.actionCreateModule.setObjectName("actionCreateModule")
        self.actionAddNodeToModule = QtGui.QAction(OpenRiggingToolkit)
        self.actionAddNodeToModule.setObjectName("actionAddNodeToModule")
        self.actionRemoveNodeFromModule = QtGui.QAction(OpenRiggingToolkit)
        self.actionRemoveNodeFromModule.setObjectName("actionRemoveNodeFromModule")
        self.actionMirrorJntsLToR = QtGui.QAction(OpenRiggingToolkit)
        self.actionMirrorJntsLToR.setObjectName("actionMirrorJntsLToR")
        self.actionMirrorJntsRToL = QtGui.QAction(OpenRiggingToolkit)
        self.actionMirrorJntsRToL.setObjectName("actionMirrorJntsRToL")
        self.actionMirrorSelection = QtGui.QAction(OpenRiggingToolkit)
        self.actionMirrorSelection.setObjectName("actionMirrorSelection")
        self.actionSelectGrpJnts = QtGui.QAction(OpenRiggingToolkit)
        self.actionSelectGrpJnts.setObjectName("actionSelectGrpJnts")
        self.actionSelectGrpMeshes = QtGui.QAction(OpenRiggingToolkit)
        self.actionSelectGrpMeshes.setObjectName("actionSelectGrpMeshes")
        self.actionUpdateModulesView = QtGui.QAction(OpenRiggingToolkit)
        self.actionUpdateModulesView.setObjectName("actionUpdateModulesView")
        self.actionUpdateInfluencesView = QtGui.QAction(OpenRiggingToolkit)
        self.actionUpdateInfluencesView.setObjectName("actionUpdateInfluencesView")
        self.actionUpdateMeshesView = QtGui.QAction(OpenRiggingToolkit)
        self.actionUpdateMeshesView.setObjectName("actionUpdateMeshesView")
        self.actionSaveLogs = QtGui.QAction(OpenRiggingToolkit)
        self.actionSaveLogs.setObjectName("actionSaveLogs")
        self.actionClearLogs = QtGui.QAction(OpenRiggingToolkit)
        self.actionClearLogs.setObjectName("actionClearLogs")
        self.actionChangeLogLevel = QtGui.QAction(OpenRiggingToolkit)
        self.actionChangeLogLevel.setObjectName("actionChangeLogLevel")
        self.actionUpdateLogSearchQuery = QtGui.QAction(OpenRiggingToolkit)
        self.actionUpdateLogSearchQuery.setObjectName("actionUpdateLogSearchQuery")
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionUpdate)
        self.menuRig.addAction(self.actionBuild)
        self.menuRig.addAction(self.actionUnbuild)
        self.menuRig.addAction(self.actionRebuild)
        self.menuJoint.addAction(self.actionCreateModule)
        self.menuJoint.addAction(self.actionAddNodeToModule)
        self.menuJoint.addAction(self.actionRemoveNodeFromModule)
        self.menuInfluences.addAction(self.actionMirrorJntsLToR)
        self.menuInfluences.addAction(self.actionMirrorJntsRToL)
        self.menuInfluences.addAction(self.actionMirrorSelection)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRig.menuAction())
        self.menubar.addAction(self.menuJoint.menuAction())
        self.menubar.addAction(self.menuInfluences.menuAction())

        self.retranslateUi(OpenRiggingToolkit)
        self.comboBox_log_level.setCurrentIndex(1)
        QtCore.QObject.connect(self.pushButton_selectGrpMeshes, QtCore.SIGNAL("pressed()"), self.actionSelectGrpMeshes.trigger)
        QtCore.QObject.connect(self.btn_update_modules, QtCore.SIGNAL("pressed()"), self.actionUpdateModulesView.trigger)
        QtCore.QObject.connect(self.btn_update_meshes, QtCore.SIGNAL("pressed()"), self.actionUpdateMeshesView.trigger)
        QtCore.QObject.connect(self.btn_update_influences, QtCore.SIGNAL("pressed()"), self.actionUpdateInfluencesView.trigger)
        QtCore.QObject.connect(self.pushButton_logs_clear, QtCore.SIGNAL("pressed()"), self.actionClearLogs.trigger)
        QtCore.QObject.connect(self.pushButton_logs_save, QtCore.SIGNAL("pressed()"), self.actionSaveLogs.trigger)
        QtCore.QObject.connect(self.comboBox_log_level, QtCore.SIGNAL("currentIndexChanged(int)"), self.actionChangeLogLevel.trigger)
        QtCore.QObject.connect(self.lineEdit_log_search, QtCore.SIGNAL("textChanged(QString)"), self.actionUpdateLogSearchQuery.trigger)
        QtCore.QMetaObject.connectSlotsByName(OpenRiggingToolkit)

    def retranslateUi(self, OpenRiggingToolkit):
        OpenRiggingToolkit.setWindowTitle(QtGui.QApplication.translate("OpenRiggingToolkit", "Open Rigging Toolkit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_modules.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Modules", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_update_modules.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.label_jnts.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Influences", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_update_influences.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_hideAssigned.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Hide Assigned", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Meshes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_update_meshes.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_selectGrpMeshes.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Select Meshes Grp", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("OpenRiggingToolkit", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRig.setTitle(QtGui.QApplication.translate("OpenRiggingToolkit", "Rig", None, QtGui.QApplication.UnicodeUTF8))
        self.menuJoint.setTitle(QtGui.QApplication.translate("OpenRiggingToolkit", "Modules", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInfluences.setTitle(QtGui.QApplication.translate("OpenRiggingToolkit", "Influences", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Logs", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Level:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_log_level.setItemText(0, QtGui.QApplication.translate("OpenRiggingToolkit", "Error", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_log_level.setItemText(1, QtGui.QApplication.translate("OpenRiggingToolkit", "Warning", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_log_level.setItemText(2, QtGui.QApplication.translate("OpenRiggingToolkit", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_log_level.setItemText(3, QtGui.QApplication.translate("OpenRiggingToolkit", "Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_logs_save.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_logs_clear.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Update All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate.setToolTip(QtGui.QApplication.translate("OpenRiggingToolkit", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBuild.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Build All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUnbuild.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Unbuild All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRebuild.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Rebuild All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreateModule.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Create Module", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddNodeToModule.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Add Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveNodeFromModule.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Remove Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMirrorJntsLToR.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Mirror R <- L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMirrorJntsRToL.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Mirror R -> L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMirrorSelection.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "Mirror using Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectGrpJnts.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "SelectGrpJnts", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectGrpMeshes.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "SelectGrpMeshes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdateModulesView.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "UpdateModulesView", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdateInfluencesView.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "UpdateInfluencesView", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdateMeshesView.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "UpdateMeshesView", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveLogs.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "SaveLogs", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveLogs.setToolTip(QtGui.QApplication.translate("OpenRiggingToolkit", "SaveLogs", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClearLogs.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "ClearLogs", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChangeLogLevel.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "ChangeLogLevel", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdateLogSearchQuery.setText(QtGui.QApplication.translate("OpenRiggingToolkit", "UpdateLogSearchQuery", None, QtGui.QApplication.UnicodeUTF8))

