from PyQt6.QtWidgets import (QScrollArea, QWidget, QVBoxLayout,QSizePolicy)
from PyQt6.QtCore import Qt

from widgets.instruction_box import InstructionBox

from backend.back import Tomasulo

class InstructionsScroll(QScrollArea):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.tomasulu = None
        self.setupUi()

    def setupUi(self):
        self.widget = QWidget()
        self.vbox   = QVBoxLayout()
        self.vbox.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setSizePolicy(QSizePolicy.Policy.Preferred,QSizePolicy.Policy.Minimum)

    
    def remove_children(self):
        for i in reversed(range(self.vbox.count())):
            self.vbox.itemAt(i).widget().setParent(None)

    #@pyqtSignal
    def tomasulu_step(self):
        status, unidades_funcionais, inst_queue = self.tomasulu.clock()


    #@pyqtSignal
    def add_instructions(self,instructions_file_path):

        self.remove_children()

        self.tomasulu = Tomasulo(instructions_file_path)

        instructions = self.tomasulu.instrucoes

        for i in range(len(instructions)):

            instruction = instructions[i]

            object = InstructionBox(instruction_number= i,
                                    instruction= instruction.instrucao,
                                    number_of_cycles= instruction.ciclosNecessarios)
            self.vbox.addWidget(object)

        self.widget.setLayout(self.vbox)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.setWidget(self.widget)
