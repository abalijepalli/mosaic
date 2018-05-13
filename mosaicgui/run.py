import sys
import mosaicgui.mosaicGUI as mosaicgui
from PyQt4 import QtCore
from mosaicgui.updateService import updateService
from mosaic.utilities.ga import registerLaunch
from PyQt4 import QtGui
from mosaicgui.mplwidget import update_rcParams

@registerLaunch("qt")
def startMOSAICQt():
	update_rcParams()
	
	app = QtGui.QApplication(sys.argv)

	u=updateService()	
	if not u.CheckUpdate():
		dmw = mosaicgui.qtAnalysisGUI()
		dmw.show()
		dmw.raise_()

		# cleanup processing
		app.connect(app, QtCore.SIGNAL("aboutToQuit()"), dmw.OnQuit)
	
		sys.exit(app.exec_())
