from random import randint

class Grammar:
    def __init__(self, start=None):
        """
        one for the start string, and one for the collection of rules.
        """
        self.rules = {}
        self.startcode = start

    def read(self, filename):
        file = open(filename,'r')
        line = file.readline()[:-1]
        while line != '':
            syms = line.split(' ')
            lhs = syms[0]
            rhs = syms[2:]
            self.__setitem__(lhs,rhs)
            line = file.readline()[:-1]

    def __setitem__(self,var,rhs):
        if var in self.rules:
            self.rules[var].append(rhs)
        else:
            self.rules[var] = rhs

    def __getitem__(self,var):
        return self.rules[var][randint(0,len(self.rules[var])-1)]
    
    def generate(self):
        self.startcode = self.startcode.split(' ')
        def helper(startcode):
            for i in range(len(self.startcode)):
                if startcode[i] in self.rules.keys():
                    return True
        while helper(self.startcode) is True:
            self.applyTo(self.startcode)
            for i in range(len(self.startcode)):
                if type(self.startcode[i]) == list:
                    """change unsolved list to string"""
                    self.startcode[i] = ' '.join(self.startcode[i])
            """make all the unsolved words go together"""
            self.startcode = ' '.join(self.startcode)
            """prepare to next loop"""
            self.startcode = self.startcode.split()
        self.startcode = ' '.join(self.startcode)
        return self.startcode

    def applyTo(self,deriv=None):
        for i in range(len(deriv)):
            if deriv[i] in self.rules.keys():
                deriv[i] = self.__getitem__(deriv[i])
        return deriv


g = Grammar("<plea> <> <plea>")
g.read("excuse.grm")
print(g.generate())