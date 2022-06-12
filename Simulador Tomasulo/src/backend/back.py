import enum
import random
from backend.MIPS.instructions import MipsInstructions
from backend.instruction import Instrucao
from backend.parse_instructions import ParseInstructions
from backend.reservation_station import ReservationStation, EnumReservationStationStates

class TomasuloStates(enum.Enum):
    SUCCESS = 1
    BUSY = 2
    FINALIZED = 3

# Classe para controlar todo o algoritmo de Tomasulo
class Tomasulo:
    # Fazendo todas as operações básicas antes de iniciar o tomasulo
    def __init__(self, path) -> None:
        parseInstructions = ParseInstructions(path)
        self.instrucoes = parseInstructions.getInstrucoes()
        self.instrucoesECiclos = parseInstructions.getInstrucoesAndCiclos()
        
        # Criando uma Reservation Station
        self.reservationStation = ReservationStation()
        
    # Executando clocks da CPU para executar o algoritmo
    def clock(self):
        v = True
        print(self.reservationStation.add_sub, self.reservationStation.mul_divide, self.reservationStation.load_store)

        #print(f"Lista: {self.instrucoes}\nTam = {len(self.instrucoes)}")
        #print(f"Reserva: {self.reservationStation.instruction_queue.instruction_queue}\nTam = {len(self.reservationStation.instruction_queue.instruction_queue)}")
        
        if len(self.instrucoes) == 0 and self.reservationStation.isAllReservationsStationsEmpty() and len(self.reservationStation.reg_bank.get_busy_regs()) == 0 and not self.reservationStation.instruction_queue.instruction_queue:
            return TomasuloStates.FINALIZED, [self.reservationStation.add_sub, self.reservationStation.mul_divide, self.reservationStation.load_store], self.reservationStation.instruction_queue.instruction_queue
        
        # Verificando se há espaço para uma nova instrução
        elif self.reservationStation.isInstructionQueueFull():
            self.reservationStation.cycle()
            v = False

        else:
            if len(self.instrucoes) > 0:
                for next_instr in self.instrucoes[:self.reservationStation.instruction_queue.queue_size]:

                    if next_instr.instrucao == MipsInstructions.BEQ and next_instr.rsrc1 != next_instr.rsrc2:
                        self.instrucoes.remove(next_instr)
                        for _ in range(random.randint(0, min(len(self.instrucoes), 3))):
                            self.instrucoes.pop(0)
                    
                    elif next_instr.instrucao == MipsInstructions.BEQ and next_instr.rsrc1 == next_instr.rsrc2:
                        return TomasuloStates.FINALIZED, [self.reservationStation.add_sub, self.reservationStation.mul_divide, self.reservationStation.load_store], self.reservationStation.instruction_queue.instruction_queue

                    else:
                        situation = self.reservationStation.insertInstruction(next_instr)
                        if situation == EnumReservationStationStates.SUCCESS:
                            self.instrucoes.remove(next_instr)

        if v:
            self.reservationStation.cycle()
        
        # Executando as Reservations Stations
        self.reservationStation.executeReservations()
        
        # Ao chegar aqui tudo rodou como esperado
        return TomasuloStates.SUCCESS, [self.reservationStation.add_sub, self.reservationStation.mul_divide, self.reservationStation.load_store], self.reservationStation.instruction_queue.instruction_queue