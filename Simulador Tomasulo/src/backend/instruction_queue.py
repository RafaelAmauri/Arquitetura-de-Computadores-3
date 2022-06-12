from backend.instruction import Instrucao

class InstructionQueue:
    def __init__(self):
        self.instruction_queue = []
        self.queue_size = 3


    def add_to_instruction_queue(self, i: Instrucao):
        if len(self.instruction_queue) < self.queue_size:
            self.instruction_queue.append(i)
        else:
            print("FILA CHEIA!")


    def stall():
        pass


    def check_true_dependency(self, tmp):
        for i in range(0, len(self.instruction_queue)-1):
            for j in range(i+1, len(self.instruction_queue)):
                #RAW
                if self.instruction_queue[j].rsrc1  == self.instruction_queue[i].rdest or self.instruction_queue[j].rsrc2 == self.instruction_queue[i].rdest:
                    self.instruction_queue[j].add_dependency(self.instruction_queue[i].rdest)
                #WAR
                if self.instruction_queue[j].rdest == self.instruction_queue[i].rsrc1:
                    self.instruction_queue[j].add_dependency(self.instruction_queue[i].rsrc1)
                #WAR
                if self.instruction_queue[j].rdest == self.instruction_queue[i].rsrc2:
                    self.instruction_queue[j].add_dependency(self.instruction_queue[i].rsrc2)
                #WAW
                if self.instruction_queue[j].rdest == self.instruction_queue[i].rdest:
                    self.instruction_queue[j].add_dependency(self.instruction_queue[i].rdest)

        for i in range(0, len(self.instruction_queue)):
            for j in range(0, len(tmp)):
                #RAW
                if self.instruction_queue[i].rsrc1 == tmp[j].get_instrucao().rdest or self.instruction_queue[i].rsrc2 == tmp[j].get_instrucao().rdest:
                    self.instruction_queue[i].add_dependency(tmp[j].get_instrucao().rdest)
                #WAR
                if self.instruction_queue[i].rdest == tmp[j].get_instrucao().rsrc1:
                    self.instruction_queue[i].add_dependency(tmp[j].get_instrucao().rsrc1)
                #WAR
                if self.instruction_queue[i].rdest == tmp[j].get_instrucao().rsrc2:
                    self.instruction_queue[i].add_dependency(tmp[j].get_instrucao().rsrc2)
                #WAW
                if self.instruction_queue[i].rdest == tmp[j].get_instrucao().rdest:
                    self.instruction_queue[i].add_dependency(tmp[j].get_instrucao().rdest)
