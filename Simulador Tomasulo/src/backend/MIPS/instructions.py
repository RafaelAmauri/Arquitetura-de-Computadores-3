# Arquivo contendo todas as instruções suportadas pelo MIPS

class MipsInstructions:        
    # Instruções aritméticas
    ADD   = 'add'  # add a, b, c 	a = b + c 	adds signed numbers.
    ADDU  = 'addu' # adds unsigned numbers.
    SUB   = 'sub'  # subtracts signed numbers.
    SUB_U = 'subu' # Unsigned subtraction
    MUL   = 'mul'  # gives low 32 bits of signed multiplication.
    MUL_U = 'mulu' # Unsigned multiplication
    DIV   = 'div'  # gives quotient of signed division.
    DIV_U = 'divu' # Unsigned division
    REM   = 'rem'  # gives remainder of signed division.
    REM_U = 'remu' # Unsigned Remainder of division
    MHFI  = 'mfhi' # after mul, gives high 32 bits. after div, gives remainder.
    MFLO  = 'mflo' # after mul, gives low 32 bits. after div, gives quotient.

    # Instruções lógicas
    NEG = 'neg' # neg a, b 	    a = -b 	gives the negative of b.
    AND = 'and' # a = b & c 	bitwise ANDs numbers.
    OR  = 'or'  # a = b | c 	bitwise ORs numbers.
    XOR = 'xor' # a = b ^ c 	bitwise XORs numbers.
    
    # Instruções de desvio
    BEQ  = 'beq'  # Branch if Equal
    BLEZ = 'blez' # Branch if Less Than or Equal to Zero
    BNE  = 'bne'  # Branch if Not Equal
    BGTZ = 'bgtz' # Branch on Greater Than Zero
    
    # Load
    LW = 'lw' # Load Word
    
    # Store
    SB = 'sb' # Store Byte
    SH = 'sh' # Store Halfword
    SW = 'sw' # Store Word
    
    # Shifts
    SLT = 'slt' # Set to 1 if Less Than
    SLTI = 'slti' # Set to 1 if Less Than Immediate
    SLTIU = 'sltiu' # Set to 1 if Less Than Unsigned Immediate
    SLTU = 'sltu' # Set to 1 if Less Than Unsigned
    SLL = 'sll' # Logical Shift Left
    SRL = 'srl' # Logical Shift Right (0-extended)
    SRA = 'sra' # Arithmetic Shift Right (sign-extended)