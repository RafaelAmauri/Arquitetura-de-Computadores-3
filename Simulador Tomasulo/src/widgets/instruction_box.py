from PyQt6.QtWidgets import (QWidget, QHBoxLayout, QLabel, QSizePolicy)

class InstructionBox(QWidget):

    def __init__(self, parent=None,instruction_number=0,instruction="",number_of_cycles=0):
        super().__init__(parent)
        self.instruction_number = instruction_number
        self.instruction        = instruction
        self.number_of_cycles   = number_of_cycles
        self.setupUi()
    
    def setupUi(self):
        
        self.hbox = QHBoxLayout()
        self.hbox.setSpacing(0)

        instruction_number_label = QLabel('{0:03d}'.format(self.instruction_number))
        instruction_label        = QLabel(self.instruction)
        number_of_cycles_label   = QLabel(str(self.number_of_cycles))

        instruction_number_label.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
        instruction_number_label.setStyleSheet("background-color: rgb(255, 255, 255);")

        instruction_label.setStyleSheet("background-color: rgb(225, 225, 225);")
        instruction_label.setSizePolicy(QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Fixed)

        number_of_cycles_label.setStyleSheet("background-color: rgb(200, 200, 200);")
        number_of_cycles_label.setSizePolicy(QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Fixed)

        self.hbox.addWidget(instruction_number_label)
        self.hbox.addWidget(instruction_label)
        self.hbox.addWidget(number_of_cycles_label)

        self.setLayout(self.hbox)

        

