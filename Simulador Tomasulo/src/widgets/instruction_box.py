from PyQt6.QtWidgets import (QWidget, QHBoxLayout, QLabel, QSizePolicy)
from PyQt6.QtGui import QFont

class InstructionBox(QWidget):

    def __init__(self, parent=None,instruction="",number_of_cycles=0):
        super().__init__(parent)
        self.instruction        = instruction
        self.number_of_cycles   = number_of_cycles

        self.label_font = QFont()
        self.label_font.setPointSize(18)

        self.setupUi()
    
    def setupUi(self):
        
        self.hbox = QHBoxLayout()
        self.hbox.setSpacing(0)

        instruction_label = QLabel(self.instruction)
        instruction_label.setFont(self.label_font)

        number_of_cycles_label = QLabel(str(self.number_of_cycles))
        number_of_cycles_label.setFont(self.label_font)

        instruction_label.setStyleSheet("background-color: rgb(225, 225, 225);")
        instruction_label.setSizePolicy(QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Fixed)

        number_of_cycles_label.setStyleSheet("background-color: rgb(200, 200, 200);")
        number_of_cycles_label.setSizePolicy(QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Fixed)

        self.hbox.addWidget(instruction_label)
        self.hbox.addWidget(number_of_cycles_label)

        self.setLayout(self.hbox)

        

