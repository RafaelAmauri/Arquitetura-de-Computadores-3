from instruction import Instrucao

a = InstructionQueue()

b = Instrucao()

b.createInstruction(1, "add", "r1", "r2", "r3")
a.add_to_instruction_queue(b)

b = Instrucao()
b.createInstruction(1, "mul", "r2", "r1", "r3")
a.add_to_instruction_queue(b)

b = Instrucao()
b.createInstruction(1, "sub", "r1", "r1", "r2")
a.add_to_instruction_queue(b)

a.check_true_dependency()

for i in a.instruction_queue:
    print(i)
    print(i.dependencies)