# Backend do tomasulo, lendo e despachando as intruções

from backend.MIPS.instructions import MipsInstructions
from backend.instruction import Instrucao
from backend.instruction_queue import InstructionQueue
from backend.register import Register
import enum

class EnumReservationStationStates(enum.Enum):
    SUCCESS = 1
    FULL = 2
    EMPTY = 3

class ReservationStation:
    def __init__(self) -> None:
        self.add_sub = []    # Reserva para 3 instruções simultaneas de add and sub
        self.mul_divide = [] # Reserva para 2 instruções simultaneas de mul e div
        self.load_store = [] # Reserva para 4 instruções simultaneas de load e store
        self.reg_bank = Register()
        
        self.instruction_queue = InstructionQueue() # Fila de despacho de instruções
    
    # Todos os gets abaixo estão com valores de tamanho hardcoded
    # Caso queira mudar o tamanho das RS facilmente, só alterar aqui
    def getAddSubReservationSize(self):
        return 3
    
    def getMulDivideReservationSize(self):
        return 2
    
    def getLoadStoreReservationSize(self):
        return 4

    def getInstructionQeueReservationSize(self):
        return 3
    
    def getAddSubList(self):
        return self.add_sub
    
    def getMulDivideList(self):
        return self.mul_divide
    
    def getLoadStoreList(self):
        return self.load_store
    
    def isAddSubEmpty(self):
        return len(self.add_sub) == 0
    
    def isMulDivideEmpty(self):
        return len(self.mul_divide) == 0
    
    def isLoadStoreEmpty(self):
        return len(self.load_store) == 0
    
    def isAllReservationsStationsEmpty(self):
        return self.isAddSubEmpty() and self.isMulDivideEmpty() and self.isLoadStoreEmpty()
    
    def isInstructionQueueFull(self):
        return len(self.instruction_queue.instruction_queue) == self.instruction_queue.queue_size
    
    def isInstructionQueueEmpty(self):
        return len(self.instruction_queue.instruction_queue) == 0
    
    # Insert a new instruction in the reservation station
    def insertInstruction(self, i: Instrucao):
        # Verificando se ainda há instruções para serem executadas na fila de instruções
        
        if len(self.instruction_queue.instruction_queue) == self.instruction_queue.queue_size:
            return EnumReservationStationStates.FULL
        else:
            # Inserindo na fila de instruções
            self.instruction_queue.instruction_queue.append(i)

            return EnumReservationStationStates.SUCCESS

    def cycle(self):
        
        
        # Pegando uma nova instrução para ser executada
        for execute_inst in self.instruction_queue.instruction_queue:
            execute_situation = EnumReservationStationStates.FULL # Pré considerando a reserva cheia

            tmp = []
            tmp.extend(self.add_sub)
            tmp.extend(self.mul_divide)
            tmp.extend(self.load_store)
    
            self.instruction_queue.check_true_dependency(tmp)
            
            if execute_inst.instrucao in [MipsInstructions.ADD, MipsInstructions.SUB]:
                if execute_inst.dependencies or execute_inst.rsrc1 in self.reg_bank.get_busy_regs() or execute_inst.rsrc2 in self.reg_bank.get_busy_regs():
                    #print(f"{execute_inst} tem dependencia em {execute_inst.dependencies}!")
                    execute_situation = EnumReservationStationStates.FULL

                # Considerando que não há RAW ou WAR
                elif len(self.add_sub) < self.getAddSubReservationSize():
                    self.add_sub.append(ReservationStationCell(execute_inst, True, execute_inst.ciclosNecessarios))
                    self.reg_bank.set_reg_as_busy(execute_inst.rdest)
                    execute_situation = EnumReservationStationStates.SUCCESS

                else:
                    #print(f"Todas unidades funcionais que podem ser usadas por {execute_inst} estao cheias!")
                    execute_situation = EnumReservationStationStates.FULL
                                
            
            elif execute_inst.instrucao in [MipsInstructions.MUL, MipsInstructions.DIV]:
                if execute_inst.dependencies:
                    #print(f"{execute_inst} tem dependencia em {execute_inst.dependencies}!")
                    execute_situation = EnumReservationStationStates.FULL

                elif len(self.mul_divide) < self.getMulDivideReservationSize():
                    self.mul_divide.append(ReservationStationCell(execute_inst, True, execute_inst.ciclosNecessarios))
                    self.reg_bank.set_reg_as_busy(execute_inst.rdest)
                    execute_situation = EnumReservationStationStates.SUCCESS

                else:
                    #print(f"Todas unidades funcionais que podem ser usadas por {execute_inst} estao cheias!")
                    execute_situation = EnumReservationStationStates.FULL
            

            elif execute_inst.instrucao in [MipsInstructions.LW, MipsInstructions.SW]:
                if execute_inst.dependencies:
                    #print(f"{execute_inst} tem dependencia em {execute_inst.dependencies}!")
                    execute_situation = EnumReservationStationStates.FULL

                elif len(self.load_store) < self.getLoadStoreReservationSize():
                    self.load_store.append(ReservationStationCell(execute_inst, True, execute_inst.ciclosNecessarios))
                    self.reg_bank.set_reg_as_busy(execute_inst.rdest)
                    execute_situation = EnumReservationStationStates.SUCCESS

                else:
                    #print(f"Todas unidades funcionais que podem ser usadas por {execute_inst} estao cheias!")
                    execute_situation = EnumReservationStationStates.FULL
            
            else:
                print(f"{execute_inst} - Instrução ainda não suportada!")
            
            
            if execute_situation == EnumReservationStationStates.SUCCESS:

                self.instruction_queue.instruction_queue.remove(execute_inst)
                
            #return execute_situation
    
    # Executando cada uma das Reservations Stations e liberando os espaços
    def executeReservations(self):
        inst: ReservationStationCell
        
        tmp = []
        tmp.extend(self.add_sub)
        tmp.extend(self.mul_divide)
        tmp.extend(self.load_store)
        for inst in tmp:
            inst.runCicle()
            
            if inst.isInstrDone():
                try:
                    self.add_sub.remove(inst)
                    for a in self.instruction_queue.instruction_queue:
                        a.remove_dependency(inst.get_instrucao().rdest)
                        a.remove_dependency(inst.get_instrucao().rsrc1)
                        a.remove_dependency(inst.get_instrucao().rsrc2)

                    self.reg_bank.free_reg(inst.get_instrucao().rdest)
                    #print(f"Removi o {inst}")
                except:
                    pass # A instrução não é desse banco
            
                try:
                    self.mul_divide.remove(inst)
                    for a in self.instruction_queue.instruction_queue:
                        a.remove_dependency(inst.get_instrucao().rdest)
                        a.remove_dependency(inst.get_instrucao().rsrc1)
                        a.remove_dependency(inst.get_instrucao().rsrc2)

                    self.reg_bank.free_reg(inst.get_instrucao().rdest)
                    #print(f"Removi o {inst}")
                except:
                    pass # A instrução não é desse banco
                
                try:
                    self.load_store.remove(inst)
                    for a in self.instruction_queue.instruction_queue:
                        a.remove_dependency(inst.get_instrucao().rdest)
                        a.remove_dependency(inst.get_instrucao().rsrc1)
                        a.remove_dependency(inst.get_instrucao().rsrc2)

                    self.reg_bank.free_reg(inst.get_instrucao().rdest)

                    #print(f"Removi o {inst}")
                except:
                    pass
                
                inst.freeCell()

# Celula que armazena o objeto que é inserido nas Reservation Stations
class ReservationStationCell:
    _instrucao: Instrucao
    _isBusy: bool
    _numCiclos: int
    
    def __init__(self) -> None:
        self._instrucao = None
        self._isBusy = False
        self._numCiclos = 0
    
    def __init__(self, inst: Instrucao, isBusy: bool, nCiclos: int) -> None:
        self._instrucao = inst
        self._isBusy = isBusy
        self._numCiclos = nCiclos
        
    def isBusy(self) -> bool:
        return self._isBusy
    
    def freeCell(self) -> None:
        self._isBusy = False
    
    def runCicle(self) -> None:
        self._numCiclos -= 1
        
    def isInstrDone(self) -> bool:
        return self._numCiclos <= 0
    
    def __str__(self) -> str:
        return f'{self._instrucao.getInstr()} | Reserva ocupada: {self._isBusy}'
    
    def __repr__(self) -> str:
        return f'({self.__str__()})'

    def get_instrucao(self):
        return self._instrucao