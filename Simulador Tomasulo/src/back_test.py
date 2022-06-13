import time
import backend.back
import os

b = backend.back.Tomasulo(os.getcwd()+'/assets/instrucoes2.txt')

for i in range(100):
    status, unidades_funcionais, inst_queue = b.clock()
    load_store = unidades_funcionais[2]
    
    if status == backend.back.TomasuloStates.FINALIZED:
        break