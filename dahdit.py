class morse:

    def __init__(self, *args):
        self.dah = "dah"
        self.dit = 'dit'
        self.di = 'di'
        self.end_w = ','
        self.end_d = ' '
        self.end = '.'
        self.txt = ''
        self.flag = False
        if args:
            if " " in args[0]:
                strs = args[0].split(" ")
                if len(strs) == 2:
                    self.di = strs[0]
                    self.dah = strs[1]
                elif len(strs) == 3:
                    self.di = strs[0]
                    self.dit = strs[1]
                    self.dah = strs[2]
                else:
                    self.di = strs[0]
                    self.dit = strs[1]
                    self.dah = strs[2]
                    self.end = strs[3]
            else:
                self.end_d = ''
                self.end_w = ' '
                self.end = ''
                if len(args[0]) > 0:
                    self.di = args[0][0]
                    self.dit = args[0][0]
                if len(args[0]) > 1:
                    self.dah = args[0][1]
                if len(args[0]) > 2:
                    self.dit = args[0][1]
                    self.dah = args[0][2]
                if len(args[0]) > 3:
                    self.end = args[0][3]

    def __pos__(self):
        new_m = self
        new_m.txt = self.di + self.end_d + new_m.txt if not self.flag else self.dit + new_m.txt
        new_m.flag = False
        return new_m

    def __neg__(self):
        new_m = self
        new_m.txt = self.dah + self.end_d + new_m.txt if not self.flag else self.dah + new_m.txt
        new_m.flag = False
        return new_m

    def __invert__(self):
        new_m = self
        new_m.flag = True
        new_m.txt = new_m.end_w + new_m.end_d + new_m.txt
        return new_m

    def __str__(self):
        if self.txt[len(self.txt) - len(self.di) - 1:len(self.txt) - len(self.end_d)] == self.di:
            self.txt = self.txt[:len(self.txt) - len(self.di) - 1] + self.dit + self.end_d
        return self.txt[:len(self.txt) - len(self.end_d)] + self.end

