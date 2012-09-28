"""
/***************************************************************************
 PgTopoEditor
                                 A QGIS plugin
 Edit toolbar for PostGIS topology primitives (ISO SQL/MM based)
                              -------------------
        begin                : 2011-10-21
        copyright            : (C) 2011 by Sandro Santilli <strk@keybit.net>
        email                : strk@keybit.net
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from pgtopoeditordialog import PgTopoEditorDialog

class PgTopoEditor:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/pgtopoeditor/icon.png"), \
            "PostGIS Topology Editor", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&PostGIS Topology Editor", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&PostGIS Topology Editor",self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):

        # check that a layer is selected
        layer = self.iface.mapCanvas().currentLayer()
        if not layer:
          QMessageBox.information(None, "RemoveEdge", "A topology edge layer must be selected")
          return

        # TODO: check that the layer has an 'edge_id' field

        # create and show the dialog
        dlg = PgTopoEditorDialog()
        # show the dialog
        dlg.show()
        result = dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code
           pass