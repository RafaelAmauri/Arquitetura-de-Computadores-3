from register import Register

a = Register()

a.set_reg_as_busy("r2")
a.set_reg_as_busy("r3")
print(a.is_busy("r2"))
print(a.get_busy_regs())