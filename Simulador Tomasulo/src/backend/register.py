class Register:
    def __init__(self):
        self.regs = {
            "r1": False,
            "r2": False,
            "r3": False,
            "r4": False,
            "r5": False,
        }

    
    def is_busy(self, reg_name):
        return self.regs[reg_name]

    def get_busy_regs(self):
        busy_regs = []

        for i in self.regs:
            if self.regs[i]:
                busy_regs.append(i)

        return busy_regs

    def set_reg_as_busy(self, reg_name):
        self.regs[reg_name] = True

    
    def free_reg(self, reg_name):
        self.regs[reg_name] = False