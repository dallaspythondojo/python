class MathDojo(object):
    def __init__ (self):
        self.value = 0
    def add(self, *val):
        for i in val:
            if type(i) is list:
                for x in i:
                    self.value += x
            if type(i) is tuple:
                for x in i:
                    self.value += x
            if type(i) is int:
                self.value += i
        return self
    def subtract(self, *val):
        for i in val:
            if type(i) is list:
                for x in i:
                    self.value -= x
            if type(i) is tuple:
                for x in i:
                    self.value -= x
            if type(i) is int:
                self.value -= i
        return self
    def result(self):
        print self.value
        return self
md = MathDojo()
md.add(1, 2, [1,2,3]).add((2,2)).subtract(2, (2,2), [2,2,2]).result()
