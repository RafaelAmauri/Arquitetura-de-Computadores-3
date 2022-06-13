# This Python file uses the following encoding: utf-8
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt6.QtCore import pyqtSignal as Signal

import utils.os_utils as OsUtils

from window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    instructions_loaded = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle('Tomasulu Visual')
        self.showMaximized()
        self.stepButton.setEnabled(False)

    #@pyQtSlot
    def load_instructions_from_system(self):

        if self.instructionsScroll.tomasulo != None:

            msg = QMessageBox()

            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("A simulation is still in progress, do you want to start a new one?")
            msg.setInformativeText("Click \'Ok\' to progress, and \'Cancel\' to continue the current simulation")
            msg.setWindowTitle("Tomasulo in Proccess")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            msg.setDefaultButton(QMessageBox.StandardButton.Ok)

            resp = msg.exec()

            if resp == QMessageBox.StandardButton.Cancel:
                return

            self.instructionsList.clean_instructions()

        file_path = QFileDialog.getOpenFileName(
                    self,
                    str("Open instructions"),
                    OsUtils.get_user_home(),
                    filter="Text files (*.txt)")[0]

        if not file_path:
            return 

        self.stepButton.setEnabled(True)

        self.instructions_loaded.emit(file_path)

    #@pyQtSlot
    def tomasulo_finalized(self):
        self.instructionsList.clean_instructions()
        self.stepButton.setEnabled(False)



if __name__ == "__main__":

    qt_app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(qt_app.exec())
