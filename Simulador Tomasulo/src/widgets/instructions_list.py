
from PyQt6.QtWidgets import (QWidget,QLabel,QVBoxLayout, QHBoxLayout, QLineEdit, QSizePolicy)
from PyQt6.QtCore import Qt 

class InstructionsList(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        
        self.setSizePolicy(QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Fixed)

        self.main_vbox = QVBoxLayout()
        self.main_vbox.setSpacing(50)
        self.main_vbox.setContentsMargins(0,0,0,0)
        self.main_vbox.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.main_vbox.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.instruction_queue_vbox = QVBoxLayout()
        self.instruction_queue_vbox.setSpacing(0)
        self.instruction_queue_vbox.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.__init_instruction_vbox(self.instruction_queue_vbox,"Instruction Queue",3)
        self.main_vbox.addLayout(self.instruction_queue_vbox)

        self.setLayout(self.main_vbox)
        
        self.registers_operations_hbox = QHBoxLayout()

        self.load_store_vbox = QVBoxLayout()
        self.load_store_vbox.setSpacing(0)
        self.load_store_vbox.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.__init_instruction_vbox(self.load_store_vbox,"Load/Store RS",4)
        self.registers_operations_hbox.addLayout(self.load_store_vbox)

        self.add_sub_vbox = QVBoxLayout()
        self.add_sub_vbox.setSpacing(0)
        self.add_sub_vbox.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.__init_instruction_vbox(self.add_sub_vbox,"Add/Sub RS",3)
        self.registers_operations_hbox.addLayout(self.add_sub_vbox)

        self.mul_div_vbox = QVBoxLayout()
        self.mul_div_vbox.setSpacing(0)
        self.mul_div_vbox.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.__init_instruction_vbox(self.mul_div_vbox,"Mul/Div RS",2)
        self.registers_operations_hbox.addLayout(self.mul_div_vbox)

        self.__change_line_edit_text(self.mul_div_vbox,"test",2)

        self.main_vbox.addLayout(self.registers_operations_hbox)

    def __init_instruction_vbox(self, vbox : QVBoxLayout, label : str, number_of_instructions : int):

        qlabel = QLabel(label)
        qlabel.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
        vbox.addWidget(qlabel)

        for i in range(number_of_instructions):
            lineEdit = QLineEdit()
            lineEdit.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
            lineEdit.setReadOnly(True)

            vbox.addWidget(lineEdit)
        
    
    def __change_line_edit_text(self,vbox: QHBoxLayout, label : str, index : int,):
        item : QLineEdit = vbox.itemAt(index).widget()
        item.setText(label)


        