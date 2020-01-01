class Processor:
    def __init__(self, instructions):
        self.code = instructions
        self.regs = {'a':0, 'b':0}
        self.pointer = 0
        self.finished = False



    def process(self):
        instr = ""
        try:
            instr = self.code[self.pointer]
        except:
            self.finished = True
            return
        if instr[0] == "inc":
            self.regs[instr[1]] += 1
            self.pointer += 1
        elif instr[0] == "hlf":
            self.regs[instr[1]] = int(self.regs[instr[1]]/2)
            self.pointer += 1
        elif instr[0] == "tpl":
            self.regs[instr[1]] *= 3
            self.pointer += 1
        elif instr[0] == "jmp":
            self.pointer += instr[1]
        elif instr[0] == "jie":
            if self.regs[instr[1]]%2 == 0:
                self.pointer += instr[2]
            else:
                self.pointer+=1
        elif instr[0] == "jio":
            if self.regs[instr[1]] == 1:
                self.pointer += instr[2]
            else:
                self.pointer+=1
        else:
            self.finished = True
